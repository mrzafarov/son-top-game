
import random

oraliq = int(input("Oraliqni kiriting:"))

def sontop():
    tasodifiy_son = random.randint(1,oraliq)
    print('Keling "Son topish" o\'yinini o\'ynaymiz!\n')
    print(f"Men 1 dan {oraliq} gacha son o'yladim. Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>> "))
        if taxmin < tasodifiy_son:
            print("Xato, men o'ylagan son bundan kattaroq. Qaytadan urinib ko'ring:")
        elif taxmin > tasodifiy_son:
            print("Xato, men o'ylagan son bundan kichikroq. Qaytadan urinib ko'ring:")
        else:
             break
    print(f"Tabriklayman TOPDINGIZ! {taxminlar} ta taxmin bilan topdingiz.\n")
    return taxminlar


def sontop_pc():
    print("Endi siz son o'ylang va men topishga harakat qilib ko'raman!\n")
    input(f"1 dan {oraliq} gacha son o'ylang va ENTER tugmasini bosing.")
    quyi = 1
    yuqori = oraliq
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Taxminimcha siz {taxmin} sonini o'yladingiz. Agar to'g'ri bo'lsa (t),"
                      f" siz o'ylagan son bundan kattaroq bo'lsa (+), kichikroq bo'lsa (-) ni kiriting: ")
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"\nTOPDIM! {taxminlar} ta taxmin bilan topdim.")
    return taxminlar
    
def play(x=10):
    yana = True
    while yana:
        user = sontop(x)
        pc = sontop_pc(x)
        if user < pc:
            print(f"\nSiz YUTDINGIZ! Siz {user} ta taxmin bilan topdingiz, men esa {pc} ta taxmin bilan topdim!")
        elif user > pc:
            print(f"\nMen YUTDIM! Men {pc} ta taxmin bilan topdim, siz esa {user} ta taxmin bilan topdingiz!")
        else:
            print(f"\nDURRANG! Ikkimiz ham {user} ta taxmin bilan topdik!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0): "))
             
play()
    
    
