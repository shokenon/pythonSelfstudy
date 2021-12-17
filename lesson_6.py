# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:16:54 2021

@author: user
"""

ismlar = [ 'Abdulloh', 'Nurulloh', 'Mahmudjon']

print(ismlar[0], 'qalesan orto yaxshimisan')
print(ismlar[1], 'qalesan orto yaxshimisan')
print(ismlar[2], 'qalesan orto yaxshimisan')


sonlar = [1, -4, 5, 2.5,]

print(sonlar[0]-sonlar[2])


sonlar[0] = 11

print(sonlar)

sonlar.insert(0, 12222)
print(sonlar)

sonlar.pop(2)
print(sonlar)



t_shaxslar = ['Zahiriddin Muhammad Bobur', 'Albert Einshtein', 'Nikolo Tesla', 'Isaak Nyuton']

z_shaxslar = ['Elon Mask' , 'Bobur Akilxanov' , 'Bill Geyts']

print('Tarixdagi  eng adolatli qirol - ', t_shaxslar.pop(0))



friends = []

friends.append('Abror')
friends.append('Safina')
friends.append('Qobil')
friends.append('Mahmudjon')
friends.append('Abdulloh')

print(friends)


friends.remove('Qobil')

print(friends)


friends.insert(0, 'Murod')

friends.insert(2 , 'Nurilloh')

friends.append('Abdurahmon')

print(friends)


guests = []

dost1 = friends.pop(0)

guests.append(dost1)

print(guests)

