import json
import math
import random


with open("adjektiv.json") as f:
    data = json.load(f)
    

def getWort():
    key, value = random.choice(list(data.items()))
    return (key,value)

while True:
    user_point = 0
    print("-----------------Almanca Kelime Tahmin Oyununa Hoşgeldiniz...----------------------")
    antworte = input("""
        Başlamak için lütfen Enter'a basınız.

        Çıkış yapmak için q'a basınız.
    """)


    if antworte=="q":
        break
    else:
        currentWort, currentWortValue  = getWort()
        print(f"{currentWort} Tahmin ediniz!")
        user_antwort = input("Cevabınız :").lower()
        
        if user_antwort == "":
            print(f"Malesef bilemediniz.. Dogru cevap  ' {currentWortValue} '")
            print(f"Puanınız : {user_point}")
        else:
            if user_antwort == currentWortValue or  user_antwort in currentWortValue:
                print("Tebrikler bildiniz.. ")
                user_point = user_point + 1
                
            else:
                print(f"Malesef bilemediniz.. Dogru cevap  ' {currentWortValue} '")
                print(f"Puanınız : {user_point}")
            