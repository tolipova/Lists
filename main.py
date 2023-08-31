country=['Italiya','Moskva','Hindiston','Antaliya','Uzbekiston','Amerika']
print("Mamlakatlar soni:",len(country))
print("Tartiblangan ruyxat:",sorted(country,reverse=True))
print("Asl ruyxat:",country)

juft_sonlar=list(range(120,1200,2))
jami=sum(juft_sonlar)
kichik=min(juft_sonlar)
katta=max(juft_sonlar)
print("Juft sonlar:", juft_sonlar)
print("sonlar yig'indisi:",jami," ","Eng katta va kichik son ayirmasi:", katta-kichik)
print("elementlar soni",len(juft_sonlar))

taomlar=['osh','manti','shurva','norin','kabob']
nonushta=taomlar[:]
del nonushta[0]
del nonushta[1]
nonushta.append('choy')
nonushta.append('non')
print(nonushta)