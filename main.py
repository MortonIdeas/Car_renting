from Database_of_vehicles import Database
import time


from interface_fun import (
    delete_the_vehicle,
    print_vehicles,
    change_vehicle,
    search_for_atribures,
    welcome,
    change_status_of_reservation,
    show_over_reserved_vehicles,
    reserve_vehicle,
    rent_now_vehicle,
    change_reservation
    )

from interface_functions import (
    add_vehicle
)
# from interface_fun import welcome
d1 = Database()
d1.load_from_file()
while(True):
    time.sleep(5)
    print("__________________________________________")
    welcome()
    tab_of_vehicles = d1.vehicles
    try:
       choosen = int(input('Choose an action:'))
    except ValueError:
        continue
    if choosen == 1:
       change_vehicle(tab_of_vehicles)
    elif choosen == 2:
        print_vehicles(tab_of_vehicles)
    elif choosen == 3:
        add_vehicle(d1)
    elif choosen == 4:
        delete_the_vehicle(d1)
    elif choosen == 5:
        reserve_vehicle(d1)
    elif choosen == 6:
        change_reservation(tab_of_vehicles)
    elif choosen == 7:
        change_status_of_reservation(tab_of_vehicles)
    elif choosen == 8:
        show_over_reserved_vehicles(tab_of_vehicles)
    elif choosen == 9:
        rent_now_vehicle(tab_of_vehicles)
    elif choosen == 10:
        search_for_atribures(tab_of_vehicles)
    elif choosen == 11:
        break
    else:
        print('This value is not recognzied, try again')
    d1.save_to_file()
d1.save_to_file()