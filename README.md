# bsm-file-nonitor
"A Python service to monitor directory changes and log them in JSON format."
# BSM File Monitor Projesi  

Bu proje, bir Linux dizinindeki dosya değişikliklerini izleyen ve bu değişiklikleri JSON formatında bir log dosyasına kaydeden bir Python servisini kapsamaktadır. Servis, Linux'ta bir **systemd** servisi olarak yapılandırılmıştır ve sistem açıldığında otomatik olarak çalışmaktadır.  

## **Proje Özeti**  
- Python scripti ile dizindeki dosya ekleme, silme ve değiştirme işlemleri izlenir.  
- İzlenen değişiklikler **`/home/kali/bsm/logs/changes.json`** dosyasına kaydedilir.  
- Proje, GitHub'da bir repository olarak paylaşılmıştır.  

## **Kurulum Adımları**  

### **1. Python Script**  
- Python 3.8 veya üzeri bir sürüm kurulu olduğundan emin olun.  
- Proje dizinine gidin ve gerekli kütüphaneleri yüklemek için şu komutu çalıştırın:  
  ```bash
  pip install watchdog
Python scripti file_monitor.py şu işlemleri yapar:

/home/kali/bsm/test dizinindeki değişiklikleri izler.

Değişiklikleri JSON formatında loglar.

2. Systemd Servis Yapılandırması

Projenin sürekli çalışmasını sağlamak için bir systemd servisi tanımlanmıştır:

Servis dosyası: /etc/systemd/system/file-monitor.service

Servis, sistem açıldığında otomatik olarak başlar.

3. Kullanım Talimatları

Servisi başlatmak için şu komutları kullanabilirsiniz:
bash
Kodu kopyala
sudo systemctl start file-monitor.service
sudo systemctl enable file-monitor.service
Servisin durumunu kontrol etmek için:

bash
Kodu kopyala
sudo systemctl status file-monitor.service
Servisi durdurmak için:

bash
Kodu kopyala
sudo systemctl stop file-monitor.service
4. GitHub'a Yükleme
Proje GitHub'da şu adreste paylaşılmıştır:
GitHub Proje Linki
Dosya Yapısı
bash
Kodu kopyala
/home/kali/bsm/
├── logs/
│   └── changes.json      # JSON formatında log dosyası  
├── test/                 # İzlenen dizin  
├── file_monitor.py       # Python scripti  
└── README.md             # Proje açıklama dosyası  
Sistem Gereksinimleri

Linux İşletim Sistemi

Python 3.8 veya üzeri

Watchdog Kütüphanesi

Yazar Bilgisi
Ad Soyad: Berfin Zümra Karacakaya
GitHub Kullanıcı Adı: zumrakrcky1
