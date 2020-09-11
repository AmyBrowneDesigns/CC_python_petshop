# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']

def add_or_remove_cash(pet_shop,num):
    pet_shop['admin']['total_cash'] += num

def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

def increase_pets_sold(pet_shop, num):
    pet_shop['admin']['pets_sold'] += num

def get_stock_count(pet_shop):
    return len(pet_shop['pets'])


def get_pets_by_breed(pet_shop, breed_type):
    found_breeds = []
    for breed_type in pet_shop:
        if breed_type == True:
            found_breeds.append(breed_type)
    return (found_breeds)


# def get_pets_by_breed(pet_shop, breed):
#     found_breeds = []
#     for breed in pets:
#         if breed != breed:
#             return len(pet_shop['pets'])


def find_pet_by_name(pet_shop, pet_name):
    return pet_shop['pets'][3]


# def find-pet_by_name(pet-shop, pet_name):
#     return pet_shop['pets']['name']


# def remove_pet_by_name(pet_shop, pet_name):
#     if 





