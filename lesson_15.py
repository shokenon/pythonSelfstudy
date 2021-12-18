# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 13:12:44 2021

@author: user
"""
# talaba_0 = {
#     'ism': 'alijon',
#     'familiya': 'shamshiyev',
#     'yosh': 22,
#     'fakultet': 'mathematic',
#     'kurs':4
#     }

# print(talaba_0.items())

# for key, value in talaba_0.items():
#    print(f"Kalit: {key}")
#    print(f"Qiymat: {value} \n")
   
telefonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310',
    'hamida': 'huawei p30',
    'maryam': 'artel',
    'tohir': 'iphone x',
    'umar' : 'iphone x'
    }


print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)
    
    
toys = {"ball", "car", "lamp", "ball" , "car" , "ball"}

print(type(toys))
print(toys)


# print(telefonlar.values())



# for k,q in telefonlar.items():
#     print(f"{k.title()}ning telefon {q}")

# mahsulotlar = {
#     'olma': 10000,
#     'anor': 20000,
#     'uzum': 40000,
#     'anjir': 25000,
#     'shaftoli': 30000
#     }

# print(mahsulotlar.keys())

# print('D\'kondagi mahsulotlar: ')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
    
# print('D\'kondagi mahsulotlar: ')
# for mahsulot in mahsulotlar:
#    print(mahsulot.title())

# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")

# lug'at elementlarini tartib bilan chaqirish

# print(mahsulotlar.keys())

# print("Do'konimizdagi mahsulotlar:")

# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())





















