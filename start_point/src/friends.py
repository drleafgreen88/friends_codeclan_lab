def get_name(x):
    first_friend = x["name"]
    return first_friend

def get_favourite_tv_show(tvshow):
    return tvshow["favourites"]["tv_show"]

def likes_to_eat(person, food_to_find):
    person_food=person["favourites"]["snacks"]
    found_snack = False
    for food in person_food:
        if food == food_to_find:
            found_snack = True
    return found_snack

def add_friend (lonely_person, new_friend):
    lonely_person["friends"].append(new_friend)

def remove_friend (sad_person, lost_friend):
    sad_person["friends"].remove(lost_friend)


def total_money (how_much):
    total = 0
    for mon in how_much:
        total += mon["monies"]
    return total

def lend_money (give_person, take_person, amount):
    give_person["monies"] -= amount
    take_person["monies"] += amount

def all_favourite_foods (food_gathering):
    total_food = []
    for sub_food in food_gathering:
        for snack in sub_food["favourites"]["snacks"]:
            total_food.append(snack)
    return total_food

def find_no_friends (friends_list):
    no_friends_list = []
    for person in friends_list:
        if len(person["friends"]) == 0:
            no_friends_list.append(person)
    return no_friends_list

def unique_favourite_tv_shows (tv_list):
    fav_tv_list = []
    for show in tv_list:
        fav_tv_list.append(show["favourites"]["tv_show"])
    set_fav = set(fav_tv_list)
    list_fav = sorted(set_fav)
    return list_fav




    