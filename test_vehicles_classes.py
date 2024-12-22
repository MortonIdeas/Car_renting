import pytest
from vehicles import (
    Vehicle,
    Car,
    Bicycle,
    Invalid_Type_Of_Bicycle,
    Lorry,
    Limousine,
    Invalid_Colour_Error
)


def test_create_car():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    assert car.heigh() == 1.45
    assert car.combustion() == 2.45
    assert car.name() == 'Toyota Yariss'
    assert car.id() == 34
    assert car.trunk_space() == 23
    assert car.name_in_program() == 'Car'


def test_create_car_empty_name():
    with pytest.raises(ValueError):
        car = Car([], 1, 1.45, 2.45, '', 34, 5, 23)


def test_create_car_wrong_high_type_string():
    with pytest.raises(TypeError):
        car = Car('metrszescdziesiattrzy', 2.45, 'Toyota Yariss', 34, 5, 23)


def test_create_car_high_int_type():
    car = Car([], 1,2, 2.45, 'Toyota Yariss', 34, 5, 23)
    assert car.heigh() == 2.00


def test_create_car_high_negative_int_value():
    car = Car([], 1, -2, 2.45, 'Toyota Yariss', 34, 5, 23)
    assert car.heigh() == 2.00


def test_cteare_car_heigh_negative_float_value():
    car = Car([], 1, -1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    assert car.heigh() == 1.45


def test_create_car_wrong_combustion_type_string():
    with pytest.raises(TypeError):
        car = Car(1.45, 'poltorejlitra', 'Toyota Yariss', 34, 5, 23)


def test_create_car_int_combustion_type():
    car = Car([], 1, 1.45, 2, 'Toyota Yariss', 34, 5, 23)
    assert car.combustion() == 2.00


def test_create_car_negative_int_combustion_type():
    car = Car([], 1, 1.45, -2, 'Toyota Yariss', 34, 5, 23)
    assert car.combustion() == 2


def test_create_car_negative_float_combustion_value():
    car = Car([], 1, 1.45, -2.45, 'Toyota Yariss', 34, 5, 23)
    assert car.combustion() == 2.45


def test_create_wrong_name_type_int_or_float():
    car = Car([], 1, 1.45, 2.45, 86, 34, 5, 23)
    assert car.name() == '86'


def test_create_wrong_id_type():
    with pytest.raises(TypeError):
        car = Car(1.45, 2.45, 'Toyota', 'numerszescdziesiattrzy', 5, 65)


def test_create_car_id_float():
    car = Car([], 1, 1.45, 2.45, 'Toyota', 5.45, 5, 65)
    assert car.id() == 5


def test_create_car_places_float_type():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5.4, 23)
    assert car.places() == 5


def test_create_car_places_negative_value():
    car = car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, -5, 23)
    assert car.places() == 5


def test_create_car_places_negative_float_value():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, -5.45, 23)
    assert car.places() == 5


def test_create_car_places_wrong_type_string():
    with pytest.raises(TypeError):
        car = Car(1.45, 2.45, 'Toyota Yariss', 34, 'pięć', 23)


def test_create_wrong_trunk_spaces_type_string():
    with pytest.raises(TypeError):
        car = Car([], 1, 1.45, 2.45, 'Toyota', 'numerszescdziesiattrzy', 5, 'szesc')


def test_change_name():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_name('Toyota Punkto')
    assert car.name() == 'Toyota Punkto'


def test_change_name_empty_name():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    with pytest.raises(ValueError):
        car.change_name('')


def test_change_heigh():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_heigh(3.45)
    assert car.heigh() == 3.45


def test_change_heigh_negative_value():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_heigh(-3.45)
    assert car.heigh() == 3.45


def test_change_heigh_wrong_type():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    with pytest.raises(TypeError):
        car.change_heigh('trzymetry')


def test_change_combustion():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_combustion(3.0)
    assert car.combustion() == 3.0


def test_change_combustion_negative_value():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_combustion(-3.0)
    assert car.combustion() == 3.0


def test_change_id():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_id(23)
    assert car.id() == 23


def test_change_id_float_value():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_id(25.45)
    assert car.id() == 25


def test_change_id_wrong_type():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    with pytest.raises(TypeError):
        car.change_id('trzydziesci')


def test_change_places():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_places(4)
    assert car.places() == 4


def test_change_places_float_input():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_places(4.34)
    assert car.places() == 4


def test_chang_places_negative_value():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_places(-3)
    assert car.places() == 3


def test_change_places_negative_float_value():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_places(-3.45)
    assert car.places() == 3


def test_change_placer_wrong_type():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    with pytest.raises(TypeError):
        car.places('siedem')


def test_change_trunk_spaces():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_trunk_spaces(34)
    assert car.trunk_space() == 34


def test_change_trunk_spaces_float_val():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_trunk_spaces(54.3)
    assert car.trunk_space() == 54


def test_change_trunk_spaces_negative_value():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_trunk_spaces(-25)
    car.trunk_space() == 25


def test_trunk_spaces_negative_float_value():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    car.change_trunk_spaces(-4.56)
    assert car.trunk_space() == 4


def test_trunk_spaces_string_value():
    car = Car([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 5, 23)
    with pytest.raises(TypeError):
        car.change_trunk_spaces('siedem')


def test_bicycle_create():
    bicycle = Bicycle([], 1, 23, 'Top_bicycle', 'mountain bike', 34)
    assert bicycle.id() == 23
    assert bicycle.name() == 'Top_bicycle'
    assert bicycle.type_of_bicycle() == 'mountain bike'
    assert bicycle.tyres_size() == 34
    assert bicycle.name_in_program() == 'Bicycle'


def test_bicycle_create_wrong_id_string():
    with pytest.raises(TypeError):
        bicycle = Bicycle([], 1, 'dwadziescia', 'Top_bicycle', 'mountain bike', 34)


def test_bicycle_create_id_float():
    bicycle = Bicycle([], 1, 23.23, 'Top_bicycle', 'mountain bike', 34)
    assert bicycle.id() == 23


def test_bicycle_create_id_negative_int():
    bicycle = Bicycle([], 1, -23, 'Top_bicycle', 'mountain bike', 34)
    assert bicycle.id() == 23


def test_bicycle_create_negative_float():
    bicycle = Bicycle([], 1, -23.34, 'Top_bicycle', 'mountain bike', 34)
    assert bicycle.id() == 23


def test_bicycle_empty_name():
    with pytest.raises(ValueError):
        bicycle = Bicycle([], 1, 23, '', 'mountain bike', 34)


def test_bicycle_create_wrong_type_of_bicycle():
    with pytest.raises(Invalid_Type_Of_Bicycle):
        bicycle = Bicycle([], 1, 23, 'Top_bicycle', 'rower gorski', 34)


def test_bicycle_create_correct_type_of_bicycle():
    bicycle = Bicycle([], 1, 23, 'Top_bicycle', 'BMX bike', 34)
    assert bicycle.type_of_bicycle() == 'BMX bike'


def test_tyres_size_incorrect_type_string():
    with pytest.raises(TypeError):
        bicycle = Bicycle([], 1, 23, 'Top_bicycle', 'mountain bike', 'trzydziesci cztery')


def test_tyres_size_float_tyre_size():
    bicycle = Bicycle([], 1, 23, 'Top_bicycle', 'mountain bike', 34.34)
    assert bicycle.tyres_size() == 34


def test_tyres_size_float_negative_tyre_size():
    bicycle = Bicycle([], 1, 23, 'Top_bicycle', 'mountain bike', -34.34)
    assert bicycle.tyres_size() == 34


def test_tyres_size_float_negative_int_tyre_size():
    bicycle = Bicycle([], 1, 23, 'Top_bicycle', 'mountain bike', -34)
    assert bicycle.tyres_size() == 34


def test_create_lorry_typically():
    lorry = Lorry([], 1, 3.45, 2.45, 'Toyota Yariss Lorry', 34, 3, 23, 123)
    assert lorry.heigh() == 3.45
    assert lorry.combustion() == 2.45
    assert lorry.name() == 'Toyota Yariss Lorry'
    assert lorry.places() == 3
    assert lorry.id() == 34
    assert lorry.trunk_space() == 23
    assert lorry.lorry_capacity() == 123
    assert lorry.name_in_program() == 'Lorry'


def test_create_lorry_string_lorry_capitality():
    with pytest.raises(TypeError):
        lorry = Lorry([], 1, 3.45, 2.45, 'Toyota Yariss Lorry', 34, 3, 23, 'sto')


def test_create_lorry_float_lorry_capitality():
    lorry = Lorry([], 1, 3.45, 2.45, 'Toyota Yariss Lorry', 34, 3, 23, 123.23)
    assert lorry.lorry_capacity() == 123


def test_create_lorry_negative_lorry_capitality():
    lorry = Lorry([], 1, 3.45, 2.45, 'Toyota Yariss Lorry', 34, 3, 23, -123)
    assert lorry.lorry_capacity() == 123


def test_create_lorry_negative_float_value():
    lorry = Lorry([], 1, 3.45, 2.45, 'Toyota Yariss Lorry', 34, 3, 23, -123.23)
    assert lorry.lorry_capacity() == 123


def test_change_value_of_lorry_capitality_typically_case():
    lorry = Lorry([], 1, 3.45, 2.45, 'Toyota Yariss Lorry', 34, 3, 23, 123)
    lorry.change_lorry_capitality(145)
    assert lorry.lorry_capacity() == 145


def test_change_value_of_lorry_capitality_wrong_type_string():
    lorry = Lorry([], 1, 3.45, 2.45, 'Toyota Yariss Lorry', 34, 3, 23, 123)
    with pytest.raises(TypeError):
        lorry.change_lorry_capitality('sto')


def test_change_value_of_lorry_capitality_Negative_value_int():
    lorry = Lorry([], 1, 3.45, 2.45, 'Toyota Yariss Lorry', 34, 3, 23, 123)
    lorry.change_lorry_capitality(-145)
    assert lorry.lorry_capacity() == 145


def test_change_value_of_lorry_capitality_float_type():
    lorry = Lorry([], 1, 3.45, 2.45, 'Toyota Yariss Lorry', 34, 3, 23, 123)
    lorry.change_lorry_capitality(145.34)
    assert lorry.lorry_capacity() == 145


def test_change_value_of_lorry_capitality_typically():
    lorry = Lorry([], 1, 3.45, 2.45, 'Toyota Yariss Lorry', 34, 3, 23, 123)
    lorry.change_lorry_capitality(-145.23)
    assert lorry.lorry_capacity() == 145


def test_create_limousine_typically():
    limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 'black', 12.3)
    assert limousine.heigh() == 1.45
    assert limousine.combustion() == 2.45
    assert limousine.name() == 'Toyota Yariss'
    assert limousine.id() == 34
    assert limousine.places() == 10
    assert limousine.trunk_space() == 23
    assert limousine.colour() == 'black'
    assert limousine.length() == 12.3
    assert limousine.name_in_program() == 'Limousine'


def test_create_limousine_with_wrong_size_of_letters():
    limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 'bLaCk', 12.3)
    assert limousine.colour() == 'black'


def test_create_limousine_with_wrong_colour():
    with pytest.raises(ValueError):
        limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 'ALA MA KOTA', 12.3)


def test_create_limousine_with_no_string_colour():
    with pytest.raises(TypeError):
        limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 234, 12.3)


def test_create_limousine_with_string_length():
    with pytest.raises(TypeError):
        limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 'black', 'dwanascie metrow')


def test_create_limousine_with_negative_value_of_length():
    limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 'black', -12.3)
    assert limousine.length() == 12.3


def test_create_limousine_with_negative_value_of_int_length():
    limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 'black', -12)
    assert limousine.length() == 12.0


def test_create_limousine_with_int_value_of_length():
    limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 'black', 12)
    assert limousine.length() == 12.0


def test_change_colour_of_the_limousine_typically():
    limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 'black', 12.3)
    assert limousine.colour() == 'black'
    limousine.change_colour('blue')
    assert limousine.colour() == 'blue'


def test_change_colour_of_the_limousine_wrong_size_of_letters():
    limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 'black', 12.3)
    limousine.change_colour('BlUE')
    assert limousine.colour() == 'blue'


def test_change_colour_of_the_limousine_wrong_str():
    limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 'black', 12.3)
    with pytest.raises(Invalid_Colour_Error):
        limousine.change_colour('Niekolor')


def test_change_lenght_of_limousine():
    limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 'black', 12.3)
    limousine.change_length(12.0)
    assert limousine.length() == 12.0


def test_change_length_of_limousine_negative_int_value_of_new_len():
    limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 'black', 12.3)
    limousine.change_length(-12)
    assert limousine.length() == 12.0


def test_change_length_of_limousine_negative_float_value():
    limousine = limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 'black', 12.3)
    limousine.change_length(-12.4)
    assert limousine.length() == 12.4


def test_change_length_lf_limousine_string_value():
    limousine = Limousine([], 1, 1.45, 2.45, 'Toyota Yariss', 34, 10, 23, 'black', 12.3)
    with pytest.raises(TypeError):
        limousine.change_length('metrsiedemdziesiat')
