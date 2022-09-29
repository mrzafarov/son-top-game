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
