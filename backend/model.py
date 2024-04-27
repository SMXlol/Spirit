import json
import os
from tkinter import *
from tkinter import filedialog as fdilog


def open_database(name_db):
    with open(name_db, 'r', encoding='utf-8') as data:
        db = json.load(data)
        return db


database_pet = open_database("bd_pet.json")
database_volunteers = open_database("bd_volunteers.json")
database_users = open_database("bd_users.json")


def save_data(db, name_db):
    with open(name_db, 'w', encoding='utf-8') as file:
        json.dump(db, file, indent=4, ensure_ascii=False)


def get_item(db, pet_id):
    items = [user for user in db["items"]]
    info_pet = []

    for i in items:
        if i["id"] == pet_id:
            for key, value in i.items():
                info_pet.append(value)

    return info_pet


info = get_item(database_pet, 0)
print(info)


def add_or_edit(db, name, balance, fodder, readme, image_url, food, weight_food):
    db["items"] = [item for item in db["items"] if item["name"] != name]
    if name not in db["items"]:
        db['items'].append({
            "id": len(db["items"]),
            "name": name.capitalize(),
            "balance": balance,
            "fodder": fodder,
            "readme": readme.capitalize(),
            "image_url": image_url,
            "all_rating": 0,
            "rating": [],
            "count_rate": 0,
            "walk": False,
            "rent": [],
            "recommended_food": food,
            "recommended_food_weight": weight_food
        })
    save_data(db, "bd_pet.json")


# name, balance, fodder, readme, image_url = input().capitalize(), float(input()), float(input()), input(), fdilog.askopenfile().name


def get_rating(db, id_pet, rate):
    for i in db['items']:
        if i.get("id") == id_pet:
            i["rating"].append(rate)
            i["count_rate"] += 1
            i["all_rating"] = sum(i["rating"]) / i["count_rate"]
            save_data(db, "bd_pet.json")


def delete_item(db, id_pet):
    db["items"] = [item for item in db["items"] if item["id"] != id_pet]
    save_data(db, "bd_pet.json")


def all_fodder(db, fodder):
    for i in db['donation']:
        for j in i.keys():
            if j == "fodder":
                i["fodder"] += fodder
                save_data(db, "bd_pet.json")


def all_balance(db, balance):
    for i in db['donation']:
        for j in i.keys():
            if j == "balance":
                i["balance"] += balance
                save_data(db, "bd_pet.json")


def edit_image(db, id_item, image_url, name_db):
    for i in db['items']:
        if i.get("id") == id_item:
            i["image_url"] = image_url
            save_data(db, name_db)


def distribution_balance(db):
    arr_balance = []
    for i in db["items"]:
        if i.get("balance") > 0:
            arr_balance.append(i.get("balance"))
            i["balance"] = 0
            save_data(db, "bd_pet.json")

    for j in db["donation"]:
        for _ in j.keys():
            if _ == "balance":
                j["balance"] += sum(arr_balance)
                arr_balance.clear()
                arr_balance.append(j["balance"])
                save_data(db, "bd_pet.json")

    for m in db["items"]:
        for n in m:
            if n == "balance":
                m[n] = sum(arr_balance) // len(db["items"])
                save_data(db, "bd_pet.json")


def distribution_fodder(db):
    arr_fodder = []
    for i in db["items"]:
        if i.get("fodder") > 0:
            arr_fodder.append(i.get("balance"))
            i["fodder"] = 0
            save_data(db, "bd_pet.json")

    for j in db["donation"]:
        for _ in j.keys():
            if _ == "fodder":
                j["fodder"] += sum(arr_fodder)
                arr_fodder.clear()
                arr_fodder.append(j["fodder"])
                save_data(db, "bd_pet.json")

    for m in db["items"]:
        for n in m:
            if n == "fodder":
                m[n] = sum(arr_fodder) // len(db["items"])
                save_data(db, "bd_pet.json")


def sort_rating(db):
    dict_rating = {}
    for items in db["items"]:
        dict_rating[items["name"]] = items.get("all_rating")

    items_id = [id_item for id_item in dict_rating.keys()]
    items_rate = [rate_item for rate_item in dict_rating.values()]

    flag = True
    while flag:
        flag = False
        for i in range(len(items_id) - 1):
            if items_rate[i] > items_rate[i + 1]:
                items_rate[i], items_rate[i + 1] = items_rate[i + 1], items_rate[i]
                items_id[i], items_id[i + 1] = items_id[i + 1], items_id[i]
                flag = True

    for i in range(len(items_id)):
        dict_rating[items_id[i]] = items_rate[i]

    print(dict_rating)


def add_or_edit_volunteers(db, name, pet_id, image_url):
    db["volunteers"] = [item for item in db["volunteers"] if item["name"] != name]
    if name not in db["volunteers"]:
        db['volunteers'].append({
            "id": len(db["items"]),
            "name": name.capitalize(),
            "pets": pet_id,
            "image_url": image_url
        })
    save_data(db, "bd_volunteers.json")


def delete_volunteers(db, id_vol):
    db["volunteers"] = [item for item in db["volunteers"] if item["id"] != id_vol]
    save_data(db, "bd_volunteers.json")


def add_pet(db, pet_id):
    for i in db["volunteers"]:
        for j in i:
            if j == "pets":
                i[j].append(pet_id)
                save_data(db, "bd_volunteers.json")


def set_walk(db, id_pet):
    for i in db["items"]:
        for j in i:
            if i.get("id") == id_pet:
                if j == "walk":
                    if not i.get("walk"):
                        i[j] = True
                    else:
                        i[j] = False
                    save_data(db, "bd_pet.json")


def set_add_food(db, id_pet, food):
    for i in db["items"]:
        for j in i:
            if i.get("id") == id_pet:
                if j == "recommended_food":
                    for eat in food:
                        i[j].append(eat.capitalize())
    save_data(db, "bd_pet.json")


def del_food(db, id_pet, food):
    for i in db["items"]:
        for j in i:
            if i.get("id") == id_pet:
                if j == "recommended_food":
                    for eat in food:
                        if eat in i.get("recommended_food"):
                            for m in range(len(i.get("recommended_food"))):
                                if i.get("recommended_food")[m] == eat:

                                    i[j].pop(m)
    save_data(db, "bd_pet.json")


def set_weight_food(db, id_pet, food):
    for i in db["items"]:
        for j in i:
            if i.get("id") == id_pet:
                if j == "recommended_food_weight":
                    i[j] = food
    save_data(db, "bd_pet.json")


def rent_pet(db, db_users, id_pet, hour, minutes, id_user):
    names, values = [], []
    for i in db["items"]:
        for j in i:
            if i.get("id") == id_pet:
                if j == "rent":
                    i[j][f"{hour}:{minutes}"] = id_user

    for user in db_users["users"]:
        for j in user:
            if user.get("id") == id_user:
                if j == "rent_pets":
                    user[j][f"{hour}:{minutes}"] = id_pet

    db_users["walkers"].append({"time": f"{hour}:{minutes}", "pet_id": id_pet, "user_id": id_user})

    save_data(db, "bd_pet.json")
    save_data(db_users, "bd_users.json")


def del_rent_pet(db, db_users, id_pet, hour, minutes, id_user):
    for i in db["items"]:
        for j in i:
            if i.get("id") == id_pet:
                if j == "rent":
                    del i[j][f"{hour}:{minutes}"]

    for user in db_users["users"]:
        for j in user:
            if user.get("id") == id_user:
                if j == "rent_pets":
                    del user[j][f"{hour}:{minutes}"]

    save_data(db, "bd_pet.json")
    save_data(db_users, "bd_users.json")
