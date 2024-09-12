# wiersze=open('mecz_przyklad.txt','r')
# tab=[]
# tab2=[]
# count=0
# for wiersz in wiersze:
#     cos=str(wiersz.strip())
#
# for i in range(len(cos)-1):
#     if cos[i]!=cos[i+1]:
#        count+=1
#
# print(count)
#
# licznik_a=0
# licznik_b=0
# for i in range(len(cos)):
#     if cos[i]=="A":
#         licznik_a+=1
#     if cos[i]=='B':
#         licznik_b+=1
#     if (licznik_a>=1000 and (licznik_a-licznik_b)>=3):
#         print("wygrana A")
#         print(licznik_a , ":" , licznik_b)
#         break
#     if (licznik_b >= 1000 and (licznik_b - licznik_a) >= 3):
#         print("wygrana B")
#         print(licznik_a, ":", licznik_b)
#         break
#
# druzyna=''
# licznik_dobrej_passy=0
# licznik=1
# max_licznik=0
# for i in range(len(cos)-1):
#     if cos[i]==cos[i+1]:
#         licznik+=1
#         if licznik==10:
#             licznik_dobrej_passy+=1
#         if licznik>max_licznik:
#             max_licznik=licznik
#             druzyna=cos[i]
#     else:
#         licznik=1
#
# print(max_licznik)
# print(druzyna)
tab=[]
wiersze=open('pary.txt','r')
for wiersz in wiersze:
    tab.append(wiersz.strip().split())
print(tab)



