# **Chatbot Project**

## Açýklama: 

Bu proje, kullanýcý sorgularýna yanýt verebilen ve sipariþ durumu sorgularý, sipariþ iptalleri, þikayetler, müþteri geri bildirimleri, teslimat süresi tahminleri ve satýþ trendleri raporlarý gibi çeþitli görevleri yerine getirebilen bir sohbet botudur.

### Özellikler:

    Kullanýcý sorgularýna yanýt verme
    Sipariþ durumu takip 
    Sipariþ iptali
    Þikayet kaydý
    Müþteri geri bildirimi
    Teslimat süresi
    Satýþ trendlerini ve en çok satan ürünler

### Kullaným:

    chatbot.py betiðini çalýþtýrýn.
    Sohbet botu sizi selamlayacak ve sorgunuzu veya isteðinizi girmenizi isteyecektir.
    Sorgunuzu veya isteðinizi yazýn ve Enter tuþuna basýn.
    Sohbet botu girdinizi iþleyecek ve buna göre yanýt verecektir.

Baðýmlýlýklar:

    TensorFlow
    Keras
    NLTK
    transformers

Kurulum:

    Gerekli baðýmlýlýklarý pip kullanarak kurun:

Bash

    pip install tensorflow keras nltk transformers



Gerekli NLTK kaynaklarýný indirin:
    python -m nltk.downloader punkt wordnet


Veri:

    Sohbet botu, sýnýrlý bir veri kümesi üzerinde eðitilmiþtir.
    Veri kümesi data dizininde bulunmaktadýr.

Model:

    Sohbet botu, Hugging Face Transformers'dan önceden eðitilmiþ bir dil modeli kullanýr.
    Model, sohbet botu veri kümesi üzerinde ince ayar yapýlýr.
    Eðitilmiþ model models dizininde saklanýr.
