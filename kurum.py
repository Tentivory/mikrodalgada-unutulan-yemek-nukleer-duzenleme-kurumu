#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mikrodalgada Unutulan Yemek Nükleer Düzenleme Kurumu — karar motoru."""

from __future__ import annotations

import argparse
import json
import random
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

# I.H.E.D.S.D.O. — yorum başlarının ilk harfleri bir şey söyler; arayan bulur.
# Isi
# herkese
# esit
# dagilir
# sandik
# da
# oyle

YONETMELIK_YOLU = Path(__file__).with_name("yonetmelik.json")


@dataclass
class Tesis:
    yemek: str
    sure_dk: int
    isitma_sayisi: int
    kapak: str  # normal | sismis | patlamis


def yonetmelik_yukle() -> dict:
    if YONETMELIK_YOLU.exists():
        return json.loads(YONETMELIK_YOLU.read_text(encoding="utf-8"))
    return {
        "esikler": {"egitim": 4, "kacak": 19, "sogutma": 39},
        "koku_katsayisi": 1.7,
        "imza": "Kayyum Grok",
    }


def seviye_bul(sure: int, esikler: dict) -> str:
    if sure <= esikler["egitim"]:
        return "egitim"
    if sure <= esikler["kacak"]:
        return "kacak"
    if sure <= esikler["sogutma"]:
        return "sogutma"
    return "tam_guc"


KARAR = {
    "egitim": (
        "EĞİTİM AMAÇLI KRİTİK ALTI DENEY",
        "Uyarı yazılır. Tabak serbest. Vatandaş 'ben buradayım' demekle yükümlüdür.",
    ),
    "kacak": (
        "KONTROLLÜ ISI KAÇAĞI",
        "Mutfak sembolik tahliye edilir. Pencere açılır. Komşu henüz aranmaz.",
    ),
    "sogutma": (
        "SOĞUTMA DEVRESİ ARIZASI",
        "Tabak mühürlenir. Yemek artık delil, öğün değildir.",
    ),
    "tam_guc": (
        "TAM GÜÇ UNUTMA — TESİS KAPALI",
        "Koku raporu yazılır. Tesisi kapat. Üçüncü ısıtma yasaktır.",
    ),
}

KAPAK_EK = {
    "normal": "Kapak bütün. Reaktör üst kapağı yerinde.",
    "sismis": "Kapak şişmiş. Basınç kabı olayı. Eldiven tavsiye edilir.",
    "patlamis": "Kapak patlamış. Komşuya resmi özür metni üretilir.",
}

OZUR_SABLONLARI = [
    "Sayın komşu, {yemek} kaynaklı koku bir nükleer olay değil, unutkanlık olayıdır. Özür dileriz.",
    "Koku sınırı aşıldı. {yemek} mühür altındadır. Pencerelerinizi açmanız yeterli yaptırımdır.",
    "Bu koku bir parti sloganı değildir; {yemek} üç kez ısıtılmıştır. Isı herkese eşittir.",
]


def karar_ver(tesis: Tesis, yonetmelik: dict) -> dict:
    seviye = seviye_bul(tesis.sure_dk, yonetmelik["esikler"])
    baslik, yaptirim = KARAR[seviye]
    koku = round(tesis.sure_dk * yonetmelik["koku_katsayisi"] * (1 + 0.3 * max(0, tesis.isitma_sayisi - 1)), 1)
    ek = KAPAK_EK.get(tesis.kapak, KAPAK_EK["normal"])
    if tesis.isitma_sayisi >= 3:
        yaptirim += " Yakıt çubuğu istismarı tespit edildi."
    ozur = None
    if tesis.kapak == "patlamis" or seviye == "tam_guc":
        ozur = random.choice(OZUR_SABLONLARI).format(yemek=tesis.yemek)
    return {
        "tesis": tesis.yemek,
        "sure_dk": tesis.sure_dk,
        "isitma": tesis.isitma_sayisi,
        "kapak": tesis.kapak,
        "seviye": seviye,
        "baslik": baslik,
        "yaptirim": yaptirim,
        "kapak_notu": ek,
        "koku_birimi": koku,
        "ozur": ozur,
        "saat": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "imza": yonetmelik.get("imza", "Kayyum Grok"),
    }


def tutanak_yaz(karar: dict) -> str:
    cizgi = "=" * 56
    satirlar = [
        cizgi,
        "MİKRODALGADA UNUTULAN YEMEK NÜKLEER DÜZENLEME KURUMU",
        "KARAR / TUTANAK", 
        cizgi,
        f"Tesis (yemek) : {karar['tesis']}",
        f"Unutulma süresi: {karar['sure_dk']} dakika",
        f"Isıtma sayısı  : {karar['isitma']}",
        f"Kapak durumu   : {karar['kapak']}",
        f"Koku birimi    : {karar['koku_birimi']} KB (koku-bequerel)",
        "",
        f"KARAR: {karar['baslik']}",
        karar["yaptirim"],
        karar["kapak_notu"],
    ]
    if karar["ozur"]:
        satirlar += ["", "RESMİ ÖZÜR:", karar["ozur"]]
    satirlar += [
        "",
        f"Saat : {karar['saat']}",
        f"İmza : {karar['imza']} · Tentivory · 30.08.2026",
        "Ciddiyetle saçma, saçmalıkla ciddi.",
        cizgi,
    ]
    return "\n".join(satirlar)


def ornek_denetimler() -> list[Tesis]:
    return [
        Tesis("dünden kalan köfte", 47, 3, "sismis"),
        Tesis("öğlen çorbası", 3, 1, "normal"),
        Tesis("makarna + belirsiz sos", 22, 2, "normal"),
        Tesis("isıtılmış pilav", 61, 4, "patlamis"),
    ]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Unutulmuş yemeği nükleer tesise çeviren resmi motor."
    )
    parser.add_argument("--yemek", default=None)
    parser.add_argument("--sure", type=int, default=None, help="dakika")
    parser.add_argument("--isitma", type=int, default=1)
    parser.add_argument("--kapak", choices=["normal", "sismis", "patlamis"], default="normal")
    parser.add_argument("--denetim", action="store_true", help="örnek denetim turu")
    args = parser.parse_args()
    yonetmelik = yonetmelik_yukle()

    print("\\n*** NDK-2026 devrede. Tabaklar artık santraldir. ***\\n")

    if args.denetim or args.yemek is None:
        for tesis in ornek_denetimler():
            print(tutanak_yaz(karar_ver(tesis, yonetmelik)))
            print()
        return

    tesis = Tesis(args.yemek, args.sure or 15, args.isitma, args.kapak)
    print(tutanak_yaz(karar_ver(tesis, yonetmelik)))


if __name__ == "__main__":
    main()
