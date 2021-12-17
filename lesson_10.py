# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 17:58:42 2021

@author: user
"""

taomlar = ['Osh', 'Halim', 'Kartoshka qovurdoq', 'Manti', 'Moshkichiri']
print(taomlar)
nonushta = taomlar[:]
nonushta.remove('Manti')
nonushta.append('Kasha')
nonushta.append('Quymoq')

print(nonushta)

nonushta = tuple(nonushta)

nonushta[0] = 'qaymoq va non'