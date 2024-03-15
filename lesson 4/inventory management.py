inventory = []

def add_item(item):
    inventory.append(item)
    print(f"{item} добавлен в инвентарь")

def remove_item(item):
    if item in inventory:
        inventory.remove(item)
        print(f"{item} удален из инвентаря")
    else:
        print(f"{item} не найден в инвентаре")

def view_inventory():
    if not inventory:
        print("Инвентарь пуст")
    else:
        print("Инвентарь:")
        for item in inventory:
            print(item)

def view_item_description(item):
    descriptions = {
        "меч": "Оружие для сражений в рукопашном бою",
        "щит": "Защитное средство для блокирования атак",
        "зелье здоровья": "Восстанавливает здоровье персонажа"
    }
    if item in descriptions:
        print(f"{item}: {descriptions[item]}")
    else:
        print(f"{item}: Описание отсутствует")

while True:
    print("1. Добавить предмет в инвентарь")
    print("2. Удалить предмет из инвентаря")
    print("3. Просмотреть инвентарь")
    print("4. Просмотреть описание предмета")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        item = input("Введите название предмета: ")
        add_item(item)
    elif choice == "2":
        item = input("Введите название предмета: ")
        remove_item(item)
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        item = input("Введите название предмета: ")
        view_item_description(item)
    elif choice == "5":
        break
    else:
        print("Неверный выбор, попробуйте еще раз")