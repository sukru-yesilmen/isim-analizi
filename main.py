import tkinter as tk

def isimisleme():

    isim = entry.get()

    grup9 = ['ı', 'i', 'r', 'I', 'İ', 'R']
    grup8 = ['h', 'z', 'q', 'H', 'Z', 'Q']
    grup7 = ['g', 'ğ', 'p', 'y', 'G', 'Ğ', 'P', 'Y']
    grup6 = ['o', 'ö', 'f', 'O', 'Ö', 'F']
    grup5 = ['e', 'n', 'w', 'E', 'N', 'W']
    grup4 = ['d', 'm', 'v', 'D', 'M', 'V']
    grup3 = ['c', 'ç', 'l', 'u', 'ü', 'C', 'Ç', 'L', 'U', 'Ü']
    grup2 = ['b', 'k', 't', 'B', 'K', 'T']
    grup1 = ['a', 'j', 's', 'ş', 'A', 'J', 'Ş', 'S']

    # Harf gruplarını bir sözlükte (dictionary) topla
    gruplar = {
        1: grup1, 2: grup2, 3: grup3,
        4: grup4, 5: grup5, 6: grup6,
        7: grup7, 8: grup8, 9: grup9
    }

    # Her grup için başlangıçta sayıyı sıfıra ayarla
    grup_sayilari = {i: 0 for i in range(1, 10)}

    # İsimdeki harfleri kontrol et
    for harf in isim:  # alitoker
        for grup, harfler in gruplar.items():
            if harf in harfler:
                grup_sayilari[grup] += 1

    # Sonuçları yazdır
    result_text.config(text="")
    for grup, sayi in grup_sayilari.items():
        if sayi > 0:
            result_text.config(text=result_text.cget("text") + f"{grup}.Çakradan : {sayi} adet var.\n")

    # Çakradan eksik harfleri kontrol et
    eksik_cakralar = [grup for grup, sayi in grup_sayilari.items() if sayi == 0]

    # Eksik çakraları yazdır
    if eksik_cakralar:
        for eksik in eksik_cakralar:
            result_text.config(text=result_text.cget("text") + f"{eksik}. çakradan harf yoktur.\n")
    else:
        result_text.config(text=result_text.cget("text") + "Girilen isimde tüm çakralar bulunmaktadır.\n")



mywindow = tk.Tk()                                   # penceremi ben burda tanıttım
mywindow.title("İsim Analizi")
mywindow.config(bg="light blue")
mywindow.geometry("400x400")                  # mywindow.config(width=400, height=400) de kullanabilirdim fakat
                                              # genel itibariyle .geometry kullanılaması daha uygundur.daha çok önerilir.

# Kullanıcıdan giriş almak için Entry widget'i
entry = tk.Entry(mywindow, width=30)
entry.pack(pady=20)             # pady parametresi, widget'in yüksekliği üzerine ekstra bir boşluk
                                # eklemek için kullanılır. Bu sayede diğer arayüz öğeleriyle daha estetik bir düzen elde edebilirsiniz.

# Hesapla butonu
calculate_button = tk.Button(mywindow, text="Hesapla", command=isimisleme)
calculate_button.pack(pady=10)

# Sonuçları göstermek için Label widget'i kullandım burada benim için önemli bir nokta.
result_text = tk.Label(mywindow, text="")
result_text.pack(pady=10)


mywindow.resizable(height = False, width = False)
# Pencereyi görüntüle
mywindow.mainloop()