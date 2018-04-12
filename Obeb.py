sayı1=int(input("Sayı 1:"))
sayı2=int(input("Sayı 2:"))

flag=True
while flag==True:
    if sayı1>sayı2:
        buyuksayı=sayı1
        kucuksayı=sayı2
    else:
        buyuksayı=sayı2
        kucuksayı=sayı1

    for i in range(1,buyuksayı):
        if (buyuksayı and kucuksayı)%i == 0:
            obeb=i
    print (obeb)
