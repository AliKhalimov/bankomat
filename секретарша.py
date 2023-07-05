documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}



def find_name(directories,documents):
    komanda = input("введите номер документа: ")
    for i in documents:
        if i["number"] == komanda:
            print(f"Владелец документа {i['name']}")
            break
    else:
        print("такого документа не существует")


def find_polka(directories,documents):
    komanda = input("введите номер документа: ")
    for key, value in directories.items():
        if komanda in value:
            print(f"документ хранится на полке: {key}")
            break
    else:
        print("Документ не найден в базе")


def raspechatka(directories,documents):
    for i in documents:
        for polka, nomera in directories.items():
            if i["number"] in nomera:
                print(f"№: {i['number']}, тип: {i['type']}, владелец: {i['name']}, полка хранения: {polka}")


def new_polka(directories,documents):
    new_p = input("введите номер полки: ")
    if new_p in directories:
        polki = ",".join(directories.keys())
        print(f"такая номер полки уже существует. перечень полок: {polki}")
    else:
        directories[new_p] = []
        polki = ",".join(directories.keys())
        print(f"полка добавлена. текущая перечень полок: {polki}")


def del_polka(directories,documents):
    del_p = input("введите номер полки: ")
    if del_p not in directories:
        polki = ",".join(directories.keys())
        print(f"такой полки не существует, текущая перечень полки: {polki}")
    elif directories[del_p] == []:
        del directories[del_p]
        polki = ",".join(directories.keys())
        print(f"полка удалена, текущая перечень полое: {polki}")
    elif directories[del_p] != []:
        polki = ",".join(directories.keys())
        print(f"на полке есть документы, удалить их нельзя. текущая перечень полок: {polki}")


def new_doc(directories,documents):
    name = input("введите владелец документа: ")
    number = input("введите номер документа: ")
    type_e = input("введите тип документа: ")
    polka = input("введите номер полки: ")
    if polka not in directories:
        print(f"такой полки не существует. используйте командой ads. \n Текущий список документов: \n")
        raspechatka(directories,documents)
    else:
        documents.append({'type': type_e, 'number': number, 'name': name})
        directories[polka].append(number)
        print("Документ добавлен. Текущий списко докумнтов: ")
        raspechatka(directories,documents)


def del_doc(directories,documents):
    del_number = input("введите номер документа: ")
    for i in documents:
        if i["number"] == del_number:
            documents.remove(i)
            for key, value in directories.items():
                if del_number in value:
                    value.remove(del_number)
            print("Документ удален \n Текущий список документов: \n")
            raspechatka(directories,documents)
            break
    else:
        print(f'Документ не найден в базе \n Текущий список документов: \n')
        raspechatka(directories,documents)
# directories = {
#     '1': ['2207 876234', '11-2'],
#     '2': ['10006'],
#     '3': []

def peremen_s_polki(directories,documents):
    nomer_polki = input("введите номер полки: ")
    nomer_doc = input("введите номер документа: ")
    if nomer_polki not in directories:
        polki = ",".join(directories.keys())
        print(f'Такой полки не существует. перечень полок: {polki}')
    # znachenie = directories[nomer_polki]
    # znachenie.append(nomer_doc)
    else:
        for key, value in directories.items():
            if nomer_doc in value:
                value.remove(nomer_doc)
                directories[nomer_polki].append(nomer_doc)
                print(f'Документ перемещен. \nтекущий список документов: ')
                raspechatka(directories,documents)
                break
        else:
            print("такой документ не существует")




while True:
    spros = input("введите команду(команда p, q, s, l, ads, ds, ad, d, m): ")
    secretarsha = {"p": find_name, "s": find_polka, "l": raspechatka, "ads": new_polka,
                  "ds": del_polka, "ad": new_doc, "d": del_doc, "m": peremen_s_polki }

    if spros == "q":
        break

    secretarsha[spros](directories, documents)
