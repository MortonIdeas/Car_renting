from vehicles import Sport_car, RV, Vehicle, Date_Conflict_Error
import pytest


def test__create_Sport_car():
    sport_car = Sport_car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 3.34)
    assert sport_car.heigh() == 1.45
    assert sport_car.combustion() == 2.45
    assert sport_car.name() == 'Toyota Yariss'
    assert sport_car.id() == 34
    assert sport_car.trunk_space() == 23
    assert sport_car.zero_to_60() == 3.34
    assert sport_car.name_in_program() == 'sport car'

def test_create_sport_car_zero_to_60_string_error():
    with pytest.raises(TypeError):
        sport_car = Sport_car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 'trzy_sekundy')


def test_create_sport_car_zero_to_60_int():
    sport_car = Sport_car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 3)
    assert sport_car.zero_to_60() == 3.00


def test_create_sport_car_zero_to_60_negative_int():
    sport_car = Sport_car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, -3)
    assert sport_car.zero_to_60() == 3.00


def test_create_sport_car_zero_to_60_negative_float():
    sport_car = Sport_car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, -3.34)
    assert sport_car.zero_to_60() == 3.34


def test_change_zero_to_60_typically():
    sport_car = Sport_car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 3.34)
    sport_car.change_zero_to_60(4.35)
    assert sport_car.zero_to_60() == 4.35


def test_change_zero_to_60_int():
    sport_car = Sport_car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 3.34)
    sport_car.change_zero_to_60(4)
    assert sport_car.zero_to_60() == 4.00


def test_change_zero_to_60_negative_value_int():
    sport_car = Sport_car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 3.34)
    sport_car.change_zero_to_60(-3)
    assert sport_car.zero_to_60() == 3.00


def test_change_zero_to_60_negative_value_float():
    sport_car = Sport_car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 3.34)
    sport_car.change_zero_to_60(-3.65)
    assert sport_car.zero_to_60() == 3.65


def test_create_rv_typically():
    rv_car = RV([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 45)
    assert rv_car.heigh() == 1.45
    assert rv_car.combustion() == 2.45
    assert rv_car.name() == 'Toyota Yariss'
    assert rv_car.id() == 34
    assert rv_car.trunk_space() == 23
    assert rv_car.ability_to_pass_obstacles() == 45
    assert rv_car.name_in_program() == 'RV'


def test_create_rv_ability_obstacles_less_than_negavive_100():
    rv_car = RV([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, -145)
    assert rv_car.ability_to_pass_obstacles() == 100


def test_create_rv_ability_obstacles_more_than_100():
    rv_car = RV([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 145)
    assert rv_car.ability_to_pass_obstacles() == 100


def test_create_rv_ability_obstacles_invalid_value_string():
    with pytest.raises(TypeError):
        rv_car = RV([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 'sto')


def test_create_rv_ability_obstacles_less_than_0():
    rv_car = RV([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, -45)
    assert rv_car.ability_to_pass_obstacles() == 45


def test_change_rv_ability_to_pass_obstacles_typicall():
    rv_car = RV([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 45)
    rv_car.change_ability_to_pass_obstacles(34)
    assert rv_car.ability_to_pass_obstacles() == 34


def test_change_rv_ability_to_pass_obstacles_negative_new_value():
    rv_car = RV([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 45)
    rv_car.change_ability_to_pass_obstacles(-34)
    assert rv_car.ability_to_pass_obstacles() == 34


def test_change_rv_ability_to_pass_obstacles_negative_new_value_less_than_100():
    rv_car = RV([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 45)
    rv_car.change_ability_to_pass_obstacles(-134)
    assert rv_car.ability_to_pass_obstacles() == 100


def test_change_rv_ability_to_pass_obstacles_value_more_than_100():
    rv_car = RV([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 45)
    rv_car.change_ability_to_pass_obstacles(134)
    assert rv_car.ability_to_pass_obstacles() == 100


def test_change_rv_ability_to_pass_obstacles_invalid_string_value():
    rv_car = RV([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23, 45)
    with pytest.raises(TypeError):
        rv_car.change_ability_to_pass_obstacles('sto_siedemdziesiat')


def test_vehicle_create_vehicle_typically():
    vehicle = Vehicle([['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']], 1)
    assert vehicle.available_status() == 1
    assert vehicle.reserved_terms() == [['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']]


def test_vehicle_create_vehicle_empty():
    vehicle = Vehicle([], 1)
    assert vehicle.available_status() == 1
    assert vehicle.reserved_terms() == []


def test_vehicle_create_vehicle_wrong_number_negative():
    vehicle = Vehicle([['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']], -1)
    assert vehicle.available_status() == 0
    assert vehicle.reserved_terms() == [['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']]


def test_vehicle_create_vehicle_wrong_number_of_availability_more_than_1():
    vehicle = Vehicle([['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']], 10)
    assert vehicle.available_status() == 1
    assert vehicle.reserved_terms() == [['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']]


def test_vehicle_create_vehicle_wrong_number_of_availability_more_than_0_less_than_1():
    vehicle = Vehicle([['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']], 0.12)
    assert vehicle.available_status() == 0
    assert vehicle.reserved_terms() == [['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']]


def test_vehicle_create_without_data():
    vehicle = Vehicle()
    assert vehicle.available_status() == 1
    assert vehicle.reserved_terms() == []


def test_vehicle_create_not_a_list():
    with pytest.raises(TypeError):
        vehicle = Vehicle('nie jestem lista', 0.12)


def test_vehicle_create_wrong_value_of_terms():
    with pytest.raises(TypeError):
        vehicle = Vehicle(['nie jestem krotka', ('2022-03-06', '2022-03-07')], 0.12)


def test_vehicle_create_wrong_type_od_data_float_status():
    vehicle = Vehicle([['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']], 0.12)
    assert vehicle.available_status() == 0
    assert vehicle.reserved_terms() == [['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']]


def test_vehicle_change_status_typically():
    vehicle = Vehicle([['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']], 0)
    vehicle.change_status(1)
    assert vehicle.available_status() == 1


def test_vehicle_delete_reservation_typically():
    vehicle = Vehicle([['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']], 0)
    vehicle.remove_reservation(['2022-03-04', '2022-03-05'])
    vehicle.reserved_terms() == ['2022-03-06', '2022-03-07']


def test_vehicle_delete_reservation_not_in_list():
    vehicle = Vehicle([['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']], 0)
    with pytest.raises(ValueError):
        vehicle.remove_reservation([['2022-03-04', '2022-03-08']])


def test_change_available_status_negatice_value():
    vehicle = Vehicle([['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']], 0)
    vehicle.change_status(-1)
    assert vehicle.available_status() == 0


def test_change_available_status_str():
    vehicle = Vehicle([['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']], 0)
    with pytest.raises(TypeError):
        vehicle.change_status('a')


def test_change_available_status_too_huge_value():
    vehicle = Vehicle([['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']], 0)
    vehicle.change_status(100)
    assert vehicle.available_status() == 1


def test_add_new_reservation_typically():
    vehicle = Vehicle([['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']], 0)
    vehicle.add_new_reservation('2022-04-04', '2022-04-05')
    assert vehicle.reserved_terms() == [['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07'], ['2022-04-04', '2022-04-05']]


def test_add_new_reservation_wrong_value():
    vehicle = Vehicle([['2022-03-04', '2022-03-05'], ['2022-03-06', '2022-03-07']], 0)
    with pytest.raises(ValueError):
        vehicle.add_new_reservation('nie jestem data','to jest string nie data')


def test_add_new_reservation_date_conflict():
    vehicle = Vehicle([['2022-03-03', '2022-03-05'], ['2022-03-06', '2022-03-07']], 0)
    with pytest.raises(Date_Conflict_Error):
        vehicle.add_new_reservation(['2022-03-04', '2022-04-05'])
