✨ Echoturk Kurulum ve Çalıştırma Rehberi

Bu rehber, Echoturk uygulamasını ilk kez kurmak ve çalıştırmak isteyen kullanıcılar içindir.

📁 Dizin Uyarısı

Kurulum komutlarında geçen dizinler (C:\Users\baran\OneDrive\Desktop\Echoturk) örnek yol adlarıdır.
Kendi bilgisayarınızdaki klasör konumuna göre uyarlayın.
Örneğin: C:\Kullanicilar\Ahmet\Masaüstü\Echoturk veya D:\Projeler\Echoturk gibi.

🔧 1. Kurulum (Otomatik)

Proje klasörüne girin.

setup.bat dosyasına çift tıklayın veya terminal/Powershell üzerinden şu komutla çalıştırın:

.\setup.bat

Bu komutlar:

Sanal ortam (venv) oluşturur,

Gerekli Python kütüphanelerini yükler,

Masaüstüne uygulama için bir kısayol oluşturur.

🛠 2. Sanal Ortamı Manuel Aktif Etme (setup.bat işe yaramazsa)

Eğer setup.bat sanal ortamı aktifleştiremezse, manuel olarak şu adımları izleyin:

PowerShell Kullanıcıları için:

.\venv\Scripts\Activate.ps1

Komut İstemi (CMD) Kullanıcıları için:

venv\Scripts\activate.bat

Aktifleştirme başarılıysa terminalin başında (venv) ifadesi görünmelidir.

📦 3. Gereksinimleri Manuel Yükleme (Gerekirse)

Eğer kütüphaneler eksikse, şu komutu manuel çalıştırabilirsiniz:

pip install flask gtts transformers sentencepiece torch protobuf

▶️ 4. Uygulamayı Çalıştırma

Sanal ortam aktif iken uygulamayı şu komutla başlatabilirsiniz:

python app.py

ℹ️ Notlar

Klasör adlarında Türkçe karakter (ü, ş, ğ, ç vb.) kullanmaktan kaçının. Bu, Python dosya yollarında sorunlara yol açabilir.

Eğer protobuf eksik uyarısı alırsanız:

pip install protobuf

