Kilo = int(input("kilonuz: "))  #kullanıcının kilosu alınır 

girilen = input("(K)g ya da (L)bs: ")    #kullanıcıdan kilosunu hangi ağırlık türünden girdiği sorulur

if (girilen.upper() == "K"):           #girilen değerlerin karşılaştırma ve dönüşüm aşaması
    çevirme = Kilo / 0.45
    print("Kilonuz lbs cinsinden: " + str(çevirme))
    
elif girilen.upper() == "L" :
    çevirme = Kilo * 0.45
    print("Kilonuz kg cinsinden: " + str(çevirme)) 
    
else:      #eğer kullanıcı geçersiz bir karakter girerse bu sonuçla karşılaşır
    print("Geçersiz bir karakter girdiniz, lütfen tekrar deneyiniz")
    
input("Çıkmak için ENTER'a basınız")