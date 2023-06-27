def proverki_parola():
    with open("pasword.txt", "r") as parol:
        parol2 = parol.readline()
        if parol2 == "заблокировано":
            print("ваша карта заблокировано")
            return False
    popitka = 3
    while True:
        pas = input("введите пароль: ")
        if pas == parol2:
            print(f"Добро пожаловать Олег")
            return True
        else:
            popitka -= 1
            print("пароль не верный")
            if popitka == 1:
                print("у вас осталось одна попытка")
            elif popitka == 0:
                print("ваша карта заблокировано")
                with open("pasword.txt", "w") as zablokirovanno:
                    zablokirovanno.write("заблокировано")
                    return False


def snyat(chislo):
    with open("bablo.txt", "r") as babki:
        balance = int(babki.readline())
    if chislo > balance:
        print("не достаточно средств на счету :-(")
    else:
        balance -= chislo
        print(f"остаток на балансе {balance} рублей")
        with open("bablo.txt", "w") as ostatok:
           ostatok.write(str(balance))

def popolnit(balance_p):
    with open("bablo.txt", "r") as popolni:
        popolni2 = int(popolni.readline())
        popolni2 += balance_p
        print(f"остаток на вашем балансе {popolni2} рублей")
        with open("bablo.txt", "w") as zap:
            zap.write(str(popolni2))


def balance():
    with open("bablo.txt", "r") as ostatok:
        ostatok2 = ostatok.readline()
        print(f"на вашем счету {ostatok2} рублей")


cont = proverki_parola()
if cont == True:
    while True:
        deystvia = input("введите команду(снять, пополнить, баланс, выход): ")
        if deystvia == "снять":
            chislo = int(input("напишите сумму: "))
            snyat(chislo)
        elif deystvia == "пополнить":
            balance_p = int(input("напишите сумму: "))
            popolnit(balance_p)
        elif deystvia == "баланс":
            balance()
        elif deystvia == "выход":
            break
# Всем привет