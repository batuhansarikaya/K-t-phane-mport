from plyer import notification

try:
   
    baslik = input("Bildirim başlığını girin: ")
    mesaj = input("Bildirim mesajını girin: ")

    notification.notify(
        title=baslik,
        message=mesaj,
        app_name="Bildirim Uygulaması",
        timeout=30
    )

    print("Bildirim gönderildi.")  

except Exception as hata:
    print("Bildirim gönderiminde bir hata oluştu:", hata)
