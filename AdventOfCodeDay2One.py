# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 19:39:37 2021

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
    
    for letter in userPassword:
        if letter == requiredLetter:
            letterUsage += 1
    
    if letterUsage >= int(minimum) and letterUsage <= int(maximum):
        validPasswords += 1
        
    
print(validPasswords)