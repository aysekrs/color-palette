\#  Kelimeden Renk Paleti Üretici 



Bu proje, kullanıcının girdiği kelimenin anlamını (temasını) analiz ederek, o temaya uygun, algoritmik olarak türetilmiş 3x3 (9 renkli) bir monokromatik renk paleti üreten basit bir Python uygulamasıdır. Palet, terminalde renkli olarak gösterilir.



\## Algoritma Nasıl Çalışır



1\.  \*\*Kelime/Tema Eşleştirme:\*\* Kullanıcının girdiği kelime (`aşk`, `deniz` vb.), dahili bir SQLite veritabanındaki anahtar kelimelerle eşleştirilerek bir \*\*Temel Renk Tonu (Hue)\*\* bulunur.

2\.  \*\*Rastgele Varyasyon:\*\* Temanın "hissiyatını" vermek için, temel tona yakın küçük bir rastgele Ton (Hue) varyasyonu eklenir.

3\.  \*\*Palet Üretimi:\*\* Seçilen Hue değeri sabit tutularak, 3 farklı \*\*Doygunluk (Saturation)\*\* ve 3 farklı \*\*Parlaklık (Lightness)\*\* seviyesi çaprazlanarak 9 benzersiz renk tonu (Monokromatik Palet) elde edilir.

4\.  \*\*Görsel Çıktı:\*\* Üretilen HEX kodları, `colorama` kütüphanesi yardımıyla terminalde renkli bloklar halinde 3x3 bir tablo şeklinde gösterilir.



\##  Kurulum ve Çalıştırma



Projeyi çalıştırmadan önce \*\*Python\*\* ve \*\*pip\*\*'in sisteminizde kurulu olduğundan emin olun.



\### 1. Gerekli Kütüphaneleri Kurma



```bash

\# colorama kütüphanesini kur

pip install colorama



\# Eğer "pip" hatası alırsanız:

\# python -m pip install colorama

