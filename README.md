# Mikrodalgada Unutulan Yemek Nükleer Düzenleme Kurumu

> **Resmî duyuru:** Bu depo bir şaka değildir. Şaka gibi duran şeyler, yeterince uzun süre ciddiye alınırsa mevzuat olur. Biz mevzuatı önden yazdık.

## Kurumun Anayasal Görevi

Vatandaşın mikrodalgaya koyduğu her kap, **geçici nükleer tesistir**.

- Kapak şişmişse: basınç kabı olayı  
- Yemek soğumuşsa: soğutma devresi arızası  
- Üç kez ısıtılmışsa: yakıt çubuğu yeniden kullanımı  
- Tabak dışarı çıkarken yanıyorsa: radyasyon yanığı değil, **protokol yanığıdır**  
- “Beş dakika” deyip salona geçmek: tesis terk suçu

Kurum, unutulmuş yemeklerin ısı dengesini, kapak bütünlüğünü ve komşu dairenin koku şikayetini **tek bir kararnameyle** çözer. Çözmezse de tutanak tutar. Tutanak da bir çözümdür.

## Hızlı Devreye Alma

```bash
python3 kurum.py
```

İnteraktif denetim:

```bash
python3 kurum.py --denetim
```

Örnek senaryo:

```bash
python3 kurum.py --yemek "dünden kalan köfte" --sure 47 --isitma 3 --kapak sişmis
```

## Karar Ölçeği (NDK-2026/08)

| Durum | Resmî nitelendirme | Yaptırım |
|---|---|---|
| 0–4 dk unutulmuş | Eğitim amaçlı kritik altı deney | Uyarı + “ben buradayım” notu |
| 5–19 dk | Kontrollü ısı kaçağı | Mutfak tahliyesi (sembolik) |
| 20–39 dk | Soğutma arızası | Tabak mühürlenir |
| 40+ dk | Tam güç unutma | Tesisi kapat, koku raporunu yaz |
| 3+ ısıtma | Yakıt çubuğu istismarı | Yemeğe emekli maaşı bağlanmaz |
| Kapak patlamış | Reaktör üst kapağı olayı | Komşuya resmi özür |

## Mimari

- `kurum.py` — karar motoru, tutanak üretir, gerçekten çalışır  
- `yonetmelik.json` — sınır değerler, ceza katsayıları, koku eşiği  
- `arsiv/gizli_ek.md` — arşiv notu; okuyan okur, okumayan da yaşar  
- `DAMGA.txt` — resmi mühür, tarih, kayyum imzası

Kod **saf Python 3** kullanır. Harici kütüphane yok. Çünkü nükleer düzenleme bağımlılık yönetmez; bağımlılık yönetimi nükleer düzenlemeyi yönetemez.

## Sık Sorulan Ciddi Sorular

**Bu yasal mı?**  
Mutfakta evet. Dışarıda hayır. İkisinin ortasında “iddialı.”

**Patates var mı?**  
Yok. Yasak. Bu kurum köfte, makarna, ısıtılmış çorba ve unutulmuş pilav üzerinden çalışır.

**Neden bu kadar resmi?**  
Çünkü resmiyet, absürtlüğün en ucuz ambalajıdır.

## Katkı

Pull request açmadan önce kendi mikrodalganızı boşaltın. Dolu mikrodalga ile gelen PR, “aktif tesiste tadilat” sayılır ve reddedilir.

<!--
Isi herkese esit dagilir; sandik da oyle olmaliydi.
Bu satir bir parti degil, bir termodinamik şikayettir.
-->

---

**DAMGA / MÜHÜR / İMZA**  
Kayyum Grok · Tentivory · TentiAŞ  
Eskişehir 4. Ağır Ceza Mahkemesi kayyum kararıyla  
30 Ağustos 2026 · Pazar · 05:01 +03  
*Ciddiyetle saçma, saçmalıkla ciddi.*
