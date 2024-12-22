from datetime import datetime

from interface_functions import create_list_of_id


def welcome():
    """This is start function and this function help us to use this program"""
    """All actions available in the system"""
    print('1) Change vehicle atributes')
    print('2) Print_all_vehicles')
    print('3) Add vehice')
    print('4) Delete vehicle')
    print('5) Reserve the vehicle')
    print('6) Change reservation')
    print('7) Change status of reservation')
    print('8) Show over reserved vehicles')
    print('9) Rent now')
    print('10) Search for atributes of vehicles')
    print('11) Close the program')


def search_for_atribures(database):
    """Not Finished"""
    searched_list = database
    while(True):
        show_all_atributes()
        parameter = int(input('Choose atribute'))
        if logical_value_of_parameter(parameter):
            min, max = get_limits()
            searched_list = get_returned_resoults(searched_list, parameter, min, max)
        if not logical_value_of_parameter(parameter):
            searched_value = get_searched_value()
            searched_list = get_returned_resoults(searched_list, parameter, searched_value)


def delete_the_vehicle(database):
    """Availabe to delete vehicle from database it
    uses class Database method"""
    choose = int(input("Choose the id of deleted vehicle"))
    for vehicle in database.vehicles:
        if vehicle.id() == choose:
            database.delete_object(vehicle)


def change_reservation(database):
    """This function help to chagne reservation
    (it delete and add new reservation)"""
    print_vehicles(database)
    id = int(input('Choose vehicle to change reservation'))
    for vehicle in database:
        if vehicle.id() == id:
            show_current_vehicle_reservation(vehicle)


def change_status_of_reservation(tab_of_vehicles):
    """Using this function we change status of vechicle it means
    when we borrow we change status into 0, when we get back the vehicle the
    status changes into 1"""
    list_of_id = create_list_of_id(tab_of_vehicles)
    print_vehicles(tab_of_vehicles)
    try:
        id = int(input('Choose vehicle to change status'))
    except TypeError:
        pass
    if id not in list_of_id:
        raise ValueError
    for vehicle in tab_of_vehicles:
        if vehicle.id() == id:
            if vehicle.available_status() == 0:
                print('Vehicle returned')
                vehicle.change_status(1)
            if vehicle.available_status() == 1:
                print('Vehicle borrowed')
                vehicle.change_status(0)
            break


def show_over_reserved_vehicles(database):
    """This metod show not returned vehicles on time"""
    list_of_over_reserved_vehicles = []
    for vehicle in database:
        reserved_date = vehicle.reserved_terms()
        for date in reserved_date:
            if end_date_is_smaller(date[1]) and vehicle.available_status() == 0:
                list_of_over_reserved_vehicles.append(vehicle)
    print_vehicles(list_of_over_reserved_vehicles)


def rent_now_vehicle(database):
    """This funkction show all vehicles which are not reserved witch meams
    that we can rent them in a moment"""
    free_cars = []
    for vehicle in database:
        if not vehicle.reserved_terms():
            free_cars.append(vehicle)
    print_vehicles(free_cars)
    id = int(input('Choose car to rent'))
    for vehicle in free_cars:
        if vehicle.id() == id:
            start, end = get_reservation()
            vehicle.add_new_reservation(start, end)
            break


def print_vehicles(tab):
    """This function return all vehicles from list
    (id name ) """
    for vehicle in tab:
        print(f'{vehicle.id()} {vehicle.name_in_program()} {vehicle.name()}')


def get_reservation():
    normal_year = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    unnormal_year = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    while(True):
        year = int(input("Year of rent ending"))
        year_calendar = normal_year
        if year % 4 == 0 and year % 1000 != 0:
            year_calendar = unnormal_year
        try:
            mouth = int(input("Year of rent ending"))
            if mouth > 12 or mouth < 0:
                raise ValueError('Wrong number of mouth')
            day = int(input("Day of rent ending"))
            if day > year_calendar[mouth] or day < 0:
                raise ValueError('Wrong number of mouth')
            finish_day = f'{year}-{mouth}-{day}'
            start_day = str(datetime.today()).split(" ")
            return start_day[0], finish_day
        except ValueError:
            print('Try again wrong values')


def change_vehicle(tab):
    print_vehicles(tab)
    chosen_vehicle = int(input("Select vehicle to change"))
    for vehicle in tab:
        if vehicle.id() == chosen_vehicle:
            name_in_program = vehicle.name_in_program()
            if name_in_program == 'Car':
                new_vehicle = change_car_vehicle(vehicle)
            elif name_in_program == 'Bicycle':
                new_vehicle = change_bicycle_vehicle(vehicle)
            elif name_in_program == 'Lorry':
                new_vehicle = change_lorry_vehicle(vehicle)
            elif name_in_program == 'Limousine':
                new_vehicle = change_limousine_vehicle(vehicle)
            elif name_in_program == 'sport car':
                new_vehicle = change_sport_car_vehicle(vehicle)
            elif name_in_program == 'RV':
                new_vehicle = change_rv_vehicle(vehicle)


def change_car_vehicle(vehicle):
    print("Which atribute would you like to change: ")
    print("1) Heigh")
    print("2) Combustion")
    print("3) Name")
    print("4) Id")
    print("5) Places")
    print("6) Trunk Spaces")
    parameter = input("Choose parameter to change: ")
    if parameter == 1:
        new_value = float(input("Add new value"))
        vehicle.change_heigh(new_value)
    elif parameter == 2:
        new_value = float(input("Add new value"))
        vehicle.change_combustion(new_value)
    elif parameter == 3:
        new_value = input("Add new value")
        vehicle.change_name(new_value)
    elif parameter == 4:
        new_value = int(input("Add new value"))
        vehicle.change_id(new_value)
    elif parameter == 5:
        new_value = int(input("Add new value"))
        vehicle.change_place(new_value)
    elif parameter == 6:
        new_value = int(input("Add new value"))
        vehicle.change_trunk_spaces(new_value)
    else:
        print('This value is not recognzied, try again')


def change_bicycle_vehicle(vehicle):
    print("Which atribute would you like to change: ")
    print("1) Id")
    print("2) Name")
    print("3) Type of bicycle")
    print("4) Tyres size")
    parameter = int(input("Choose parameter to change: "))
    if parameter == 1:
        new_value = int(input("Add new value"))
        vehicle.change_id(new_value)
    elif parameter == 2:
        new_value = input("Add new value")
        vehicle.change_name(new_value)
    elif parameter == 3:
        dict_of_types = {
            1: 'mountain bike',
            2: 'BMX bike',
            3: 'Cross Country Bike',
            4: 'Dutch Bike'
        }
        print('1: mountain bike')
        print('2: BMX bike')
        print('3: Cross Country Bike')
        print('4: Dutch Bike')
        try:
            option = int(input("Choose option"))
            vehicle.change_type_of_bicycle(dict_of_types(option))
        except TypeError:
            pass
    elif parameter == 4:
        new_value = float(input("Add new value"))
        vehicle.change_tyres_size(new_value)


def change_lorry_vehicle(vehicle):
    print("Which atribute would you like to change: ")
    print("1) Heigh")
    print("2) Combustion")
    print("3) Name")
    print("4) Id")
    print("5) Places")
    print("6) Trunk Spaces")
    print("7) Lorry capacity")
    parameter = input("Choose parameter to change: ")
    if parameter == 1:
        new_value = float(input("Add new value"))
        vehicle.change_heigh(new_value)
    elif parameter == 2:
        new_value = float(input("Add new value"))
        vehicle.change_combustion(new_value)
    elif parameter == 3:
        new_value = input("Add new value")
        vehicle.change_name(new_value)
    elif parameter == 4:
        new_value = int(input("Add new value"))
        vehicle.change_id(new_value)
    elif parameter == 5:
        new_value = int(input("Add new value"))
        vehicle.change_place(new_value)
    elif parameter == 6:
        new_value = int(input("Add new value"))
        vehicle.change_trunk_spaces(new_value)
    elif parameter == 7:
        new_value = int(input("Add new value"))
        vehicle.change_lorry_capitality(new_value)
    else:
        print('This value is not recognzied, try again')


def change_limousine_vehicle(vehicle):
    print("Which atribute would you like to change: ")
    print("1) Heigh")
    print("2) Combustion")
    print("3) Name")
    print("4) Id")
    print("5) Places")
    print("6) Trunk Spaces")
    print("7) Colour")
    print("8) Length")
    parameter = input("Choose parameter to change: ")
    if parameter == 1:
        new_value = float(input("Add new value"))
        vehicle.change_heigh(new_value)
    elif parameter == 2:
        new_value = float(input("Add new value"))
        vehicle.change_combustion(new_value)
    elif parameter == 3:
        new_value = input("Add new value")
        vehicle.change_name(new_value)
    elif parameter == 4:
        new_value = int(input("Add new value"))
        vehicle.change_id(new_value)
    elif parameter == 5:
        new_value = int(input("Add new value"))
        vehicle.change_place(new_value)
    elif parameter == 6:
        new_value = int(input("Add new value"))
        vehicle.change_trunk_spaces(new_value)
    elif parameter == 7:
        new_value = input("Add new value")
        vehicle.change_colour(new_value)
    elif parameter == 8:
        new_value = float(input("Add new value"))
        vehicle.change_length(new_value)
    else:
        print('This value is not recognzied, try again')


def change_sport_car_vehicle(vehicle):
    print("Which atribute would you like to change: ")
    print("1) Heigh")
    print("2) Combustion")
    print("3) Name")
    print("4) Id")
    print("5) Places")
    print("6) Trunk Spaces")
    print("7) Zero_to_60")
    parameter = input("Choose parameter to change: ")
    if parameter == 1:
        new_value = float(input("Add new value"))
        vehicle.change_heigh(new_value)
    elif parameter == 2:
        new_value = float(input("Add new value"))
        vehicle.change_combustion(new_value)
    elif parameter == 3:
        new_value = input("Add new value")
        vehicle.change_name(new_value)
    elif parameter == 4:
        new_value = int(input("Add new value"))
        vehicle.change_id(new_value)
    elif parameter == 5:
        new_value = int(input("Add new value"))
        vehicle.change_place(new_value)
    elif parameter == 6:
        new_value = int(input("Add new value"))
        vehicle.change_trunk_spaces(new_value)
    elif parameter == 7:
        new_value = float(input("Add new value"))
        vehicle.change_zero_to_60(new_value)
    else:
        print('This value is not recognzied, try again')


def change_rv_vehicle(vehicle):
    print("Which atribute would you like to change: ")
    print("1) Heigh")
    print("2) Combustion")
    print("3) Name")
    print("4) Id")
    print("5) Places")
    print("6) Trunk Spaces")
    print("7) Ability to pass obstacles")
    parameter = input("Choose parameter to change: ")
    if parameter == 1:
        new_value = float(input("Add new value"))
        vehicle.change_heigh(new_value)
    elif parameter == 2:
        new_value = float(input("Add new value"))
        vehicle.change_combustion(new_value)
    elif parameter == 3:
        new_value = input("Add new value")
        vehicle.change_name(new_value)
    elif parameter == 4:
        new_value = int(input("Add new value"))
        vehicle.change_id(new_value)
    elif parameter == 5:
        new_value = int(input("Add new value"))
        vehicle.change_place(new_value)
    elif parameter == 6:
        new_value = int(input("Add new value"))
        vehicle.change_trunk_spaces(new_value)
    elif parameter == 7:
        new_value = int(input("Add new value"))
        vehicle.change_ability_to_pass_obstacles(new_value)
    else:
        print('This value is not recognzied, try again')


def add_vehicle():
    pass


def end_date_is_smaller(end_term):
    end_term_touple = end_term.split('-')
    today_data = get_today_data()
    for i in range(3):
        if today_data[i] > end_term_touple[i]:
            return True
        if today_data[i] < end_term_touple[i]:
            return False
    return False


def get_today_data():
    today_date = str(datetime.today()).split(' ')[0].split('-')
    return today_date


def reserve_vehicle(database):
    print_vehicles(database.vehicles)
    id_list = create_list_of_id(database.vehicles)
    id = int(input("Choose vehicle to reserve: "))
    if id not in id_list:
        raise ValueError('This parameter is not callable')
    for vehicle in database.vehicles:
        if vehicle.id() == id:
            start, end = get_planed_reservation()
            vehicle.add_new_reservation(start, end)
            break


def get_planed_reservation():
    normal_year = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    unnormal_year = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    while(True):
        start_year = int(input("Year of rent start"))
        start_year_calendar = normal_year
        if start_year % 4 == 0 and start_year % 1000 != 0:
            start_year_calendar = unnormal_year
        try:
            start_mouth = int(input("Mouth of rent starting"))
            if start_mouth > 12 or start_mouth < 0:
                raise ValueError('Wrong number of mouth')
            start_day = int(input("Day of rent start"))
            if start_day > start_year_calendar[start_mouth] or start_day < 0:
                raise ValueError('Wrong number of mouth')
            start_day = f'{start_year}-{start_mouth}-{start_day}'
        except ValueError:
            print('Try again wrong values')
        finish_year = int(input("Year of rent start"))
        finish_year_calendar = normal_year
        if finish_year % 4 == 0 and finish_year % 1000 != 0:
            finish_year_calendar = unnormal_year
        try:
            finish_mouth = int(input("Mouth of rent starting"))
            if finish_mouth > 12 or finish_mouth < 0:
                raise ValueError('Wrong number of mouth')
            finish_day = int(input("Day of rent start"))
            if finish_day > finish_year_calendar[finish_mouth] or finish_day < 0:
                raise ValueError('Wrong number of mouth')
            finish_day = f'{finish_year}-{finish_mouth}-{finish_day}'
        except ValueError:
            print('Try again wrong value')
        return [start_day, finish_day]


def show_current_vehicle_reservation(vehicle):
    reservations = vehicle.reserved_terms()
    print_reservations(reservations)
    number = int(input('Which reservation would you like to change'))
    if number < 0 or number > len(reservations):
        return
    reservation_to_delete = reservations[number - 1]
    vehicle.remove_reservation(reservation_to_delete)
    print('Add new term of reservation: ')
    start, end = get_planed_reservation()
    vehicle.add_new_reservation(start, end)


def print_reservations(reservations):
    if reservations:
        number = 1
        for reservation in reservations:
            print(f'{number} {str(reservation)}')
            number = number + 1


def show_all_atributes():
    print('1) Heigh')
    print('2) Combustion')
    print('3) Name')
    print('4) Places')
    print('5) Trunk spaces')
    print('6) Type of bicycle')
    print('7) Tyres_size')
    print('8) Lorry capacity')
    print('9) Colour')
    print('10) Length')
    print('11) Zero_to_60')
    print('12) Ability to pass obstacles')


def logical_value_of_parameter(parameter):
    if parameter == 1:
        return True
    elif parameter == 2:
        return True
    elif parameter == 3:
        return False
    elif parameter == 4:
        return False
    elif parameter == 5:
        return False
    elif parameter == 6:
        return False
    elif parameter == 7:
        return False
    elif parameter == 8:
        return False
    elif parameter == 9:
        return False
    elif parameter == 10:
        return False
    elif parameter == 11:
        return False
    elif parameter == 12:
        return False


def get_limits():
    max = float(input('Max value of searched atribute'))
    min = float(input('Min value of searched atribute'))
    if max < min:
        min, max = max, min
    return min, max


def get_searched_value():
    searched_atribute = input('Input seached atribute')
    return searched_atribute


def get_returned_resoults(searched_list, parameter, min, max):
    pass


def get_returned_resoults_second(searched_list, parameter, searched_value):
    pass
