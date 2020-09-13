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
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_type:
            found_breeds.append(breed_type)
    return found_breeds


def find_pet_by_name(pet_shop, pet_name):
        return pet_shop['pets'][3]


# def find_pet_by_name(pet_shop, pet_name):
#     for pet in pet_shop['pets']:
#         if pet == pet_name:
#             return pet

def find_pet_by_name(pet_shop,pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop['pets']:
        if pet['name'] == pet_name:
            pet_shop['pets'].remove(pet)



def add_pet_to_stock(pet_shop, new_pet):
    pet_shop['pets'].append(new_pet) 



# def get_customer_cash(customers, num):
#     pet_shop[customer[0]]+= num


# def remove_pet_by_name(pet_shop, pet_name):
#     for pet in pet_shop['pets']:
#         if pet['name'] == pet_name:
#             pet_shop['pets'].remove(pet)




def remove_customer_cash(pet_shop, num):
    pet_shop["cash"] -= num



def customer_pet_count(customers):
    return pet_shop[customers][0]



def add_pet_to_customer(customers, new_pet):
    customers[0] += new_pet
    
# def increase_pets_sold(pet_shop, num):
#     pet_shop['admin']['pets_sold'] += num

