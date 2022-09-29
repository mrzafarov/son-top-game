import random

def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print('Keling "Son topish" o\'yinini o\'ynaymiz!\n')
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
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


def sontop_pc(x=10):
    print("Endi siz son o'ylang va men topishga harakat qilib ko'raman!\n")
    input(f"1 dan {x} gacha son o'ylang va ENTER tugmasini bosing.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Taxminimcha siz {taxmin} sonini o'yladingiz. Agar to'g'ri bo'lsa (T),"
                      f" siz o'ylagan son bundan kattaroq bo'lsa (+), kichikroq bo'lsa (-) ni kiriting: ")
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"\nTOPDIM! {taxminlar} ta taxmin bilan topdim.")
    return taxminlar
