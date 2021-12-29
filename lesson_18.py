# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 12:29:20 2021

@author: user
"""

savol = "Kiritilgan sonning ildizini qaytaruvchi dastur. \n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    qiymat = int(input(savol))
    if qiymat < 0:
        continue
    elif qiymat == "exit":
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")