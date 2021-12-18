# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 17:26:16 2021

@author: user
"""

"""otam = {'ismi': 'xasan', 'tyil': 1955, 'viloyat': ' xorazm'}


tyil = otam['tyil']

vil = otam['viloyat']

print(f"Otamning ismi  {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} \
      viloyatida tug'ilganlar")
      
      
taomlar = {'birinchi': 'osh', 'ikkinchi': 'sho\'rva', 'uchinchi':'halim', \
           'to\'rtinchi': 'baliq', 'beshinchi': 'manti'
           }
    
sardor = taomlar['birinchi']

ezoza = taomlar['to\'rtinchi']

odilbek = taomlar['beshinchi']


print(f"Sardor {sardor} ni yaxshi ko'radi, E'zoza {ezoza} ni yaxshi ko'radi, Odilbek {odilbek}ni yaxshi ko'radi.")
"""

python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}



kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")