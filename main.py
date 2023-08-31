# country=['Italiya','Moskva','Hindiston','Antaliya','Uzbekiston','Amerika']

# print("Mamlakatlar soni:",len(country))
# print("Tartiblangan ruyxat:",sorted(country,reverse=True))
# print("Asl ruyxat:",country)

# juft_sonlar=list(range(120,1200,2))
# jami=sum(juft_sonlar)
# kichik=min(juft_sonlar)
# katta=max(juft_sonlar)

# print("Juft sonlar:", juft_sonlar)
# print("sonlar yig'indisi:",jami," ","Eng katta va kichik son ayirmasi:", katta-kichik)
# print("elementlar soni",len(juft_sonlar))

# taomlar=['osh','manti','shurva','norin','kabob']
# nonushta=taomlar[:]

# del nonushta[0]
# del nonushta[1]

# nonushta.append('choy')
# nonushta.append('non')

# print(nonushta)

# x=10
# y=4
# c=5
# if x>0 and y>0 and c>6:
#  print('x va y katta 0 dan')
# if x>0 or x<15:
#  print("X katta0dan yoki 15dan kichik")
# else: 
#  print ('xato')

tarjimon = {
 'привет' :    'Salom',
 'ручка' :   'Ruchka',
 'карандаш' :    'Qalam',
 'книга' :    'Kitob',
 'тетрадь' :    'Daftar',
 'машина' : 'Avtomobil',
}

tarjimon_turi=input("tarjimon turini tanlang(1-Rus tili 2-uzbek tili) ")
if tarjimon_turi== '1':
    rus_soz=input('Ruscha soz kiriting:')
    if rus_soz in tarjimon:
        uz_soz=tarjimon[rus_soz]
        print(f"{rus_soz} tarjimasi {uz_soz} boladi")
    else:
        print("kichik if da xatolik")
elif tarjimon_turi== '2':
    uz_sozlar={v:k for k,v in tarjimon.items() }
    uz_soz=input("Uzbekcha soz kriting: ")
    if uz_soz in uz_sozlar:
        rus_soz=uz_sozlar[uz_soz]
        print(f"{uz_soz}tarjimasi {rus_soz}deyiladi")
    else:
        print("tarjima qilinmadi")
else:
    print("Notug'ri tanlov")