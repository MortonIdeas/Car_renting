import json
from datetime import datetime
from vehicles import (
    Car,
    Bicycle,
    Lorry,
    Limousine,
    Sport_car,
    RV
)


def get_today_data():
    """This function return the current data"""
    a = str(datetime.now())
    parts = a.split(" ")
    return parts[0]


def read_from_json_file(file_handle):
    """This functiorn read from the file vehicles.json"""
    vehicles = []
    data = json.load(file_handle)
    for vehicle in data:
        try:
            name_in_program = vehicle["name_in_program"]
            if name_in_program == 'Car':
                new_vehicle = add_car_vehicle(vehicle)
            elif name_in_program == 'Bicycle':
                new_vehicle = add_bicycle_vehicle(vehicle)
            elif name_in_program == 'Lorry':
                new_vehicle = add_lorry_vehicle(vehicle)
            elif name_in_program == 'Limousine':
                new_vehicle = add_limousine_vehicle(vehicle)
            elif name_in_program == 'sport car':
                new_vehicle = add_sport_car_vehicle(vehicle)
            elif name_in_program == 'RV':
                new_vehicle = add_rv_vehicle(vehicle)
        except KeyError:
            pass
        except Exception:
            pass
        vehicles.append(new_vehicle)
    return vehicles


def write_to_json_file(file_handle, vehicles):
    """This type of function write the data to vehicle.json"""
    data = []
    for vehicle in vehicles:
        type_of_vehicle = vehicle.name_in_program()
        vehicle_data = return_json_for_vehicle(vehicle, type_of_vehicle)
        data.append(vehicle_data)
    json.dump(data, file_handle, indent=4)


def return_json_for_vehicle(vehicle, type_of_vehicle):
    """This function decide what kind of vehicle we decided to create"""
    if type_of_vehicle == 'Car':
        vehicle_data = create_car_object_into_json(vehicle)
    elif type_of_vehicle == 'Bicycle':
        vehicle_data = create_bicycle_object_into_json(vehicle)
    elif type_of_vehicle == 'Lorry':
        vehicle_data = create_lorry_object_into_json(vehicle)
    elif type_of_vehicle == 'Limousine':
        vehicle_data = create_limousine_object_into_json(vehicle)
    elif type_of_vehicle == 'sport car':
        vehicle_data = create_sport_car_object_into_json(vehicle)
    elif type_of_vehicle == 'RV':
        vehicle_data = create_RV_object_into_json(vehicle)
    return vehicle_data


def create_car_object_into_json(vehicle):
    """This function create car object using data from json"""
    name_in_program = vehicle.name_in_program()
    heigh = vehicle.heigh()
    combustion = vehicle.combustion()
    name = vehicle.name()
    id = vehicle.id()
    places = vehicle.places()
    trunk_spaces = vehicle.trunk_space()
    available_status = vehicle.available_status()
    reserved_terms = vehicle.reserved_terms()
    vehicle_data = {
        'available_status': available_status,
        'reserved_terms': reserved_terms,
        'name_in_program': name_in_program,
        'heigh': heigh,
        'combustion': combustion,
        'name': name,
        'id': id,
        'places': places,
        'trunk_spaces': trunk_spaces
    }
    return vehicle_data


def create_bicycle_object_into_json(vehicle):
    """This function create bicycle object using data from json"""
    name_in_program = vehicle.name_in_program()
    name = vehicle.name()
    id = vehicle.id()
    type_of_bicycle = vehicle.type_of_bicycle()
    tyres_size = vehicle.tyres_size()
    available_status = vehicle.available_status()
    reserved_terms = vehicle.reserved_terms()
    vehicle_data = {
        'name_in_program': name_in_program,
        'name': name,
        'id': id,
        'type_of_bicycle': type_of_bicycle,
        'tyres_size': tyres_size,
        'available_status': available_status,
        'reserved_terms': reserved_terms
    }
    return vehicle_data


def create_lorry_object_into_json(vehicle):
    """This function create lorry object using data from json"""
    name_in_program = vehicle.name_in_program()
    heigh = vehicle.heigh()
    combustion = vehicle.combustion()
    name = vehicle.name()
    id = vehicle.id()
    places = vehicle.places()
    trunk_spaces = vehicle.trunk_space()
    lorry_capacity = vehicle.lorry_capacity()
    available_status = vehicle.available_status()
    reserved_terms = vehicle.reserved_terms()
    vehicle_data = {
        'name_in_program': name_in_program,
        'heigh': heigh,
        'combustion': combustion,
        'name': name,
        'id': id,
        'places': places,
        'trunk_spaces': trunk_spaces,
        'lorry_capacity': lorry_capacity,
        'available_status': available_status,
        'reserved_terms': reserved_terms
    }
    return vehicle_data


def create_limousine_object_into_json(vehicle):
    """This function create limousine object using data from json"""
    name_in_program = vehicle.name_in_program()
    heigh = vehicle.heigh()
    combustion = vehicle.combustion()
    name = vehicle.name()
    id = vehicle.id()
    places = vehicle.places()
    trunk_spaces = vehicle.trunk_space()
    colour = vehicle.colour()
    length = vehicle.length()
    available_status = vehicle.available_status()
    reserved_terms = vehicle.reserved_terms()
    vehicle_data = {
        'name_in_program': name_in_program,
        'heigh': heigh,
        'combustion': combustion,
        'name': name,
        'id': id,
        'places': places,
        'trunk_spaces': trunk_spaces,
        'colour': colour,
        'length': length,
        'available_status': available_status,
        'reserved_terms': reserved_terms
    }
    return vehicle_data


def create_sport_car_object_into_json(vehicle):
    """This function create sport car object using data from json"""
    name_in_program = vehicle.name_in_program()
    heigh = vehicle.heigh()
    combustion = vehicle.combustion()
    name = vehicle.name()
    id = vehicle.id()
    places = vehicle.places()
    trunk_spaces = vehicle.trunk_spaces()
    zero_to_60 = vehicle.zero_to_60()
    available_status = vehicle.available_status()
    reserved_terms = vehicle.reserved_terms()
    vehicle_data = {
        'name_in_program': name_in_program,
        'heigh': heigh,
        'combustion': combustion,
        'name': name,
        'id': id,
        'places': places,
        'trunk_spaces': trunk_spaces,
        'zero_to_60': zero_to_60,
        'available_status': available_status,
        'reserved_terms': reserved_terms
    }
    return vehicle_data


def create_RV_object_into_json(vehicle):
    """This function create RV object using data from json"""
    name_in_program = vehicle.name_in_program()
    heigh = vehicle.heigh()
    combustion = vehicle.combustion()
    name = vehicle.name()
    id = vehicle.id()
    places = vehicle.places()
    trunk_spaces = vehicle.trunk_spaces()
    ability_to_pass_obstacles = vehicle.ability_to_pass_obstacles()
    available_status = vehicle.available_status()
    reserved_terms = vehicle.reserved_terms()
    vehicle_data = {
        'name_in_program': name_in_program,
        'heigh': heigh,
        'combustion': combustion,
        'name': name,
        'id': id,
        'places': places,
        'trunk_spaces': trunk_spaces,
        'ability_to_pass_obstacles': ability_to_pass_obstacles,
        'available_status': available_status,
        'reserved_terms': reserved_terms
    }
    return vehicle_data


def add_car_vehicle(vehicle):
    """Function add car to the DataBase"""
    available_status = vehicle['available_status']
    reserved_terms = vehicle['reserved_terms']
    heigh = vehicle['heigh']
    combustion = vehicle['combustion']
    name = vehicle['name']
    id = vehicle['id']
    places = vehicle['places']
    trunk_spaces = vehicle['trunk_spaces']
    new_vehicle = Car(
        reserved_terms,
        available_status,
        heigh,
        combustion,
        name,
        id,
        places,
        trunk_spaces
    )
    return new_vehicle


def add_bicycle_vehicle(vehicle):
    """Function add bicycle to the DataBase"""
    available_status = vehicle['available_status']
    reserved_terms = vehicle['reserved_terms']
    name = vehicle['name']
    id = vehicle['id']
    type_of_bicycle = vehicle['type_of_bicycle']
    tyres_size = vehicle['tyres_size']
    vehicle = Bicycle(
        reserved_terms,
        available_status,
        id,
        name,
        type_of_bicycle,
        tyres_size
    )
    return vehicle


def add_lorry_vehicle(vehicle):
    """Function add lorry to the DataBase"""
    available_status = vehicle['available_status']
    reserved_terms = vehicle['reserved_terms']
    heigh = vehicle['heigh']
    combustion = vehicle['combustion']
    name = vehicle['name']
    id = vehicle['id']
    places = vehicle['places']
    trunk_spaces = vehicle['trunk_spaces']
    lorry_capacity = vehicle['lorry_capacity']
    vehicle = Lorry(
        reserved_terms,
        available_status,
        heigh,
        combustion,
        name,
        id,
        places,
        trunk_spaces,
        lorry_capacity
    )
    return vehicle


def add_limousine_vehicle(vehicle):
    """Function add limousine to the DataBase"""
    available_status = vehicle['available_status']
    reserved_terms = vehicle['reserved_terms']
    heigh = vehicle['heigh']
    combustion = vehicle['combustion']
    name = vehicle['name']
    id = vehicle['id']
    places = vehicle['places']
    trunk_spaces = vehicle['trunk_spaces']
    colour = vehicle['colour']
    length = vehicle['length']
    vehicle = Limousine(
        reserved_terms,
        available_status,
        heigh,
        combustion,
        name,
        id,
        places,
        trunk_spaces,
        colour,
        length
    )
    return vehicle


def add_sport_car_vehicle(vehicle):
    """Function add sport car to the DataBase"""
    available_status = vehicle['available_status']
    reserved_terms = vehicle['reserved_terms']
    heigh = vehicle['heigh']
    combustion = vehicle['combustion']
    name = vehicle['name']
    id = vehicle['id']
    places = vehicle['places']
    trunk_spaces = vehicle['trunk_spaces']
    zero_to_60 = vehicle['zero_to_60']
    vehicle = Sport_car(
        reserved_terms,
        available_status,
        heigh,
        combustion,
        name,
        id,
        places,
        trunk_spaces,
        zero_to_60
    )
    return vehicle


def add_rv_vehicle(vehicle):
    """Function add rv to the DataBase"""
    available_status = vehicle['available_status']
    reserved_terms = vehicle['reserved_terms']
    heigh = vehicle['heigh']
    combustion = vehicle['combustion']
    name = vehicle['name']
    id = vehicle['id']
    places = vehicle['places']
    trunk_spaces = vehicle['trunk_spaces']
    ability_to_pass_obstacles = vehicle['ability_to_pass_obstacles']
    vehicle = RV(
        reserved_terms,
        available_status,
        heigh,
        combustion,
        name,
        id,
        places,
        trunk_spaces,
        ability_to_pass_obstacles
    )
    return vehicle


def delete_over_reserved_vehicles(list_of_vehicles):
    """This function remove not taken car from the fental company"""
    new_list_of_vehicles = []
    return new_list_of_vehicles


def add_vehicle(database):
    """Using this function we decide which category of vehicle we would like
    to add to database"""
    print("1) Car")
    print("2) Bicycle")
    print("3) Lorry")
    print("4) Limousine")
    print("5) Sport Car")
    print("6) RV")
    parameter = int(input("What kind of vehicle would you like to add: "))
    if parameter == 1:
        add_car_from_hand(database)
    elif parameter == 2:
        add_bicycle_from_hand()
    elif parameter == 3:
        add_lorry_from_hand()
    elif parameter == 4:
        add_limousine_from_hand()
    elif parameter == 5:
        add_sport_car_from_hand()
    elif parameter == 6:
        add_rv_car_from_handed()
    else:
        print('This value is not recognzied, try again')


def add_car_from_hand(database):
    """This function help to create a car which we add to database"""
    available_status = 1
    reserved_terms = []
    heigh = float(input(' Set value of hieight: '))
    combustion = float(input(' Set value of compustion: '))
    name = input('Set name of vehicle')
    id = get_new_id(create_list_of_id(database.vehicles))
    places = int(input('Set amount of places in vehicle'))
    trunk_spaces = int(input('Set trunk spaces: '))
    new_vehicle = Car(
        reserved_terms,
        available_status,
        heigh,
        combustion,
        name,
        id,
        places,
        trunk_spaces
    )
    database.add_object(new_vehicle)


def add_bicycle_from_hand(database):
    """This function help to create a bicycle which we add to database"""
    available_status = 1
    reserved_terms = []
    name = input('Set name of vehicle')
    id = get_new_id(create_list_of_id(database))
    type_of_bicycle = choose_type_of_bicycle()
    tyres_size = float(input('Set size of tyres'))
    vehicle = Bicycle(
        reserved_terms,
        available_status,
        id,
        name,
        type_of_bicycle,
        tyres_size
    )
    return vehicle


def add_lorry_from_hand(database):
    """This function help to create a lorry(add it's necessary atributes) which we add to database"""
    available_status = 1
    reserved_terms = []
    heigh = float(input(' Set value of hieight'))
    combustion = float(input(' Set value of height'))
    name = float(input('Set name of vehicle'))
    id = get_new_id(create_list_of_id(database))
    places = int(input('Set amount of places in vehicle'))
    trunk_spaces = int(input('Set trunk spaces'))
    lorry_capacity = int(input('Set lorry capacity'))
    new_vehicle = Lorry(
        reserved_terms,
        available_status,
        heigh,
        combustion,
        name,
        id,
        places,
        trunk_spaces,
        lorry_capacity
    )
    database.add_object(new_vehicle)


def add_limousine_from_hand(database):
    """This function help to create a limousine(add it's necessary atributes) which we add to database"""
    available_status = 1
    reserved_terms = []
    heigh = float(input(' Set value of hieight'))
    combustion = float(input(' Set value of height'))
    name = float(input('Set name of vehicle'))
    id = get_new_id(create_list_of_id(database))
    places = int(input('Set amount of places in vehicle'))
    trunk_spaces = int(input('Set trunk spaces'))
    length = float(input('Set lorry capacity'))
    colour = get_colour_of_limusine()
    new_vehicle = Limousine(
        reserved_terms,
        available_status,
        heigh,
        combustion,
        name,
        id,
        places,
        trunk_spaces,
        colour,
        length
    )
    database.add_object(new_vehicle)


def add_sport_car_from_hand(database):
    """This function help to create a sport car(add it's necessary atributes) which we add to database"""
    available_status = 1
    reserved_terms = []
    heigh = float(input(' Set value of height: '))
    combustion = float(input(' Set value of compustion: '))
    name = input('Set name of vehicle')
    id = get_new_id(create_list_of_id(database.vehicles))
    places = int(input('Set amount of places in vehicle'))
    trunk_spaces = int(input('Set trunk spaces: '))
    zero_to_60 = float(input('Set zero_to_60'))
    new_vehicle = Sport_car(
        reserved_terms,
        available_status,
        heigh,
        combustion,
        name,
        id,
        places,
        trunk_spaces,
        zero_to_60
    )
    database.add_object(new_vehicle)


def add_rv_car_from_handed(database):
    """This function help to create a rv(add it's necessary atributes) which we add to database"""
    available_status = 1
    reserved_terms = []
    heigh = float(input(' Set value of hieight: '))
    combustion = float(input(' Set value of compustion: '))
    name = input('Set name of vehicle')
    id = get_new_id(create_list_of_id(database.vehicles))
    places = int(input('Set amount of places in vehicle'))
    trunk_spaces = int(input('Set trunk spaces: '))
    ability_to_pass_obstacles = int(input('Set ability to pass obstacles'))
    new_vehicle = RV(
        reserved_terms,
        available_status,
        heigh,
        combustion,
        name,
        id,
        places,
        trunk_spaces,
        ability_to_pass_obstacles
    )
    database.add_object(new_vehicle)


def get_new_id(tab):
    """This function find the smallest free id number"""
    for i in range(len(tab) + 1):
        if i not in tab:
            return i


def create_list_of_id(database):
    """This function returns used vehicle id in list"""
    list_of_id = []
    for vehicle in database:
        list_of_id.append(vehicle.id())
    return list_of_id


def choose_type_of_bicycle():
    """This function show all permitted bicycles types and return choosen one"""
    print('1) Mountain_bike')
    print('2) BMX bike')
    print('3) Cross Country Bike')
    print('4) Dutch Bike')
    parameter = int(input("Choose type of bicycle to add: "))
    if parameter == 1:
        return 'mountain bike'
    elif parameter == 2:
        return 'BMX bike'
    elif parameter == 3:
        return 'Cross Country Bike'
    elif parameter == 4:
        return 'Dutch Bike'
    else:
        print('This value is not recognzied, try again')


def get_colour_of_limusine():
    """This function show all permitted limousine colours and return choosen one"""
    print('Colours')
    print('1) Black')
    print('2) White')
    print('3) Blue')
    print('4) Orange')
    print('5) Purple')
    print('6) Red')
    print('7) Green ')
    while(True):
        choose = int(input("Choose colour of limusine"))
        if choose == 1:
            return 'black'
        elif choose == 2:
            return 'white'
        elif choose == 3:
            return 'blue'
        elif choose == 4:
            return 'orange'
        elif choose == 5:
            return 'purple'
        elif choose == 6:
            return 'red'
        elif choose == 7:
            return 'green'
        else:
            print('This value is not recognzied, try again')
