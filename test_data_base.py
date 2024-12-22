from Database_of_vehicles import (
     Database,
     There_is_no_that_vehicle
)
from vehicles import Car
import pytest


def test_data_base_add_vehicle():
    d1 = Database()
    c1 = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    d1.add_object(c1)
    assert len(d1.vehicles) == 1


def test_data_base_delete_the_vehicle():
    d1 = Database()
    c1 = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    d1.add_object(c1)
    assert len(d1.vehicles) == 1
    d1.delete_object(c1)
    assert len(d1.vehicles) == 0


def test_delete_from_database_vehicle_not_from_list():
    d1 = Database()
    c1 = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    c2 = Car([], 1, 2.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    d1.add_object(c1)
    with pytest.raises(There_is_no_that_vehicle):
        d1.delete_object(c2)


def test_search_value_from_database():
    d1 = Database()
    c1 = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    c2 = Car([], 1, 2.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    d1.add_object(c1)
    d1.add_object(c2)
    assert len(d1.vehicles) == 2
