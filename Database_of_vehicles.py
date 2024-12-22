from datetime import datetime
from interface_functions import (
    write_to_json_file,
    read_from_json_file
)
from interface_fun import (
    end_date_is_smaller,
    print_vehicles,
    get_reservation
)


class There_is_no_that_vehicle(ValueError):
    pass


def check_date_and_reservation(reservation):
    current_data = str(datetime.date.today())
    parts_of_data = current_data.split('-')
    parts_reservation = reservation.split('-')
    for i in range(3):
        if parts_reservation[i] < parts_of_data[i]:
            return True
    return False


class Database:
    """This is a class of Database. It is an class which contains information
    about all vehicles wchich we have in our company
    This class contain methods which allow us to load to file and save to file
    (def load_from_file, def save_to_file)
    Other methods:
    add_object > add vehicle to vehicles(list)
    rent_vehicle_now > Show and make reservation from availabe and not
    reserved vehicles delete_object > remove object from vehicle(list)
    Atributes:
    vehicle(list) > This atribute contains all vehicles
    """
    def __init__(self):
        self.vehicles = []
        self.search_vehicles = []

    def load_from_file(self):
        """This method also remove not realized reservations"""
        with open('vehicles.json', 'r') as file_handle:
            self.vehicles = read_from_json_file(file_handle)
            """This part of the function delete unrealized reservations"""
            for vehicle in self.vehicles:
                reservations = vehicle.reserved_terms()
                for reservation in reservations:
                    if end_date_is_smaller(reservation[1]) and vehicle.available_status() == 1:
                        vehicle.remove_reservation(reservation)

    def save_to_file(self):
        with open('vehicles.json', 'w') as file_handle:
            write_to_json_file(file_handle, self.vehicles)

    def delete_object(self, deleted_object):
        if deleted_object not in self.vehicles:
            raise There_is_no_that_vehicle('There is not such object in the database')
        self.vehicles.remove(deleted_object)

    def add_object(self, vehicle):
        self.vehicles.append(vehicle)

    def rent_vehicle_now(self):
        free_cars = []
        id_free_cars = []
        for vehicle in self.vehicles:
            if not vehicle.reserved_terms():
                free_cars.append(vehicle)
                id_free_cars.append(vehicle.id())
        print_vehicles(free_cars)
        while('True'):
            a = int(input('Choose id of vehicle: '))
            if a in id_free_cars:
                for vehicle in self.vehicles:
                    if vehicle.id() == a:
                        vehicle.change_status(1)
                        start, end = get_reservation()
                        vehicle.add_new_reservation(start, end)
                break
            else:
                print('Your number is incorrect try again')
