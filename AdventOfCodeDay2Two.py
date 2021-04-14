# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 20:11:33 2021

@author: Joseph Kharzo
"""

import pandas as pd

df = pd.read_csv("Passwords.csv")

passwords = df['Passwords']

validPasswords = 0

for password in passwords:
    letterUsage = 0
    findingMinimum = password.split("-")
    minimum = findingMinimum[0]
    findingMaximum = findingMinimum[1].split()
    maximum = findingMaximum[0]
    findingLetter = findingMaximum[1].split(":")
    requiredLetter = findingLetter[0]
    userPassword = findingMaximum[2]
    
    if userPassword[int(minimum)-1] == requiredLetter and userPassword[int(maximum)-1] != requiredLetter:
        validPasswords += 1
    elif userPassword[int(minimum)-1] != requiredLetter and userPassword[int(maximum)-1] == requiredLetter:
        validPasswords +=1
        
print(validPasswords)