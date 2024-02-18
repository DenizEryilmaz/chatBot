# **Chatbot Project**

## A��klama: 

Bu proje, kullan�c� sorgular�na yan�t verebilen ve sipari� durumu sorgular�, sipari� iptalleri, �ikayetler, m��teri geri bildirimleri, teslimat s�resi tahminleri ve sat�� trendleri raporlar� gibi �e�itli g�revleri yerine getirebilen bir sohbet botudur.

### �zellikler:

    Kullan�c� sorgular�na yan�t verme
    Sipari� durumu takip 
    Sipari� iptali
    �ikayet kayd�
    M��teri geri bildirimi
    Teslimat s�resi
    Sat�� trendlerini ve en �ok satan �r�nler

### Kullan�m:

    chatbot.py beti�ini �al��t�r�n.
    Sohbet botu sizi selamlayacak ve sorgunuzu veya iste�inizi girmenizi isteyecektir.
    Sorgunuzu veya iste�inizi yaz�n ve Enter tu�una bas�n.
    Sohbet botu girdinizi i�leyecek ve buna g�re yan�t verecektir.

Ba��ml�l�klar:

    TensorFlow
    Keras
    NLTK
    transformers

Kurulum:

    Gerekli ba��ml�l�klar� pip kullanarak kurun:

Bash

    pip install tensorflow keras nltk transformers



Gerekli NLTK kaynaklar�n� indirin:
    python -m nltk.downloader punkt wordnet


Veri:

    Sohbet botu, s�n�rl� bir veri k�mesi �zerinde e�itilmi�tir.
    Veri k�mesi data dizininde bulunmaktad�r.

Model:

    Sohbet botu, Hugging Face Transformers'dan �nceden e�itilmi� bir dil modeli kullan�r.
    Model, sohbet botu veri k�mesi �zerinde ince ayar yap�l�r.
    E�itilmi� model models dizininde saklan�r.
