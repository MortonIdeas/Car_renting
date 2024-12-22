class Invalid_Type_Of_Bicycle(ValueError):
    pass


class Invalid_Colour_Error(ValueError):
    pass


class Date_Conflict_Error(ValueError):
    pass


class Vehicle:
    """This is a definition of the class Vehicle(main class)
    it contains information about car reservations:
    1) All reserved terms -> list
    2) Information about vechicle availability -> int
    This class contains also methods witch can change this atributes
    """
    def __init__(self, reserved_terms=None, available_status=1):
        if reserved_terms is None:
            reserved_terms = []
        for elemnet in reserved_terms:
            if not reserved_terms:
                pass
            elif type(elemnet) != list:
                raise TypeError('This must be a list')
        if type(reserved_terms) != list:
            raise TypeError('This must be a list')
        if available_status < 1:
            available_status = 0
        elif available_status > 1:
            available_status = 1
        self._reserved_terms = reserved_terms
        self._available_status = available_status

    def reserved_terms(self):
        return self._reserved_terms

    def available_status(self):
        return self._available_status

    def change_reserved_terms(self, new_reserved_terms):
        self._reserved_terms == new_reserved_terms

    def remove_reservation(self, removed_term):
        if removed_term not in self.reserved_terms():
            raise ValueError('You cannot remove something with does not exist')
        self._reserved_terms.remove(removed_term)

    def change_status(self, new_status):
        if type(new_status) == str:
            raise TypeError("Status can take only 1 and 0")
        if new_status < 1:
            new_status = 0
        if new_status > 1:
            new_status = 1
        self._available_status = new_status

    def add_new_reservation(self, begin_term, end_term):
        new_reservation = [begin_term, end_term]
        self._reserved_terms.append(new_reservation)


class Car(Vehicle):
    """This is a definition of the class Car(main class)
    Car inheritance from Vehicle
    It contains information about car atributes:
    1) All reserved terms -> list
    2) Information about vechicle availability -> int
    3) heigh -> float
    4) name -> str
    5) id -> int
    6) combustion -> float
    7) places -> int
    8) trunk_spaces -> int
    This class contains also methods witch can change this atributes
    """
    def __init__(self, reserved_terms, available_status, heigh, combustion, name, id, places, trunk_spaces):
        super().__init__(reserved_terms, available_status)
        if (type(name) == int or type(name) == float):
            name = str(name)
        if name == '':
            raise ValueError('Name cannot be empty')
        if type(heigh) == str:
            raise TypeError('Heigh of the car cannot be string')
        if type(heigh) == int:
            heigh = float(heigh)
        if heigh < 0:
            heigh = -heigh
        self._heigh = heigh
        if type(combustion) == str:
            raise TypeError('The combustion cannot be string')
        if type(combustion) == int:
            combustion = float(combustion)
        if combustion < 0:
            combustion = -combustion
        self._combustion = combustion
        self._name = name
        if type(id) == str:
            raise TypeError('Id of the vehicle cannot be empty that type')
        if id < 0:
            id = -id
        if type(id) == float:
            id = int(id)
        self._id = id
        if type(places) == float:
            places = int(places)
        if places < 0:
            places = -places
        if type(places) == str:
            raise TypeError('Places cannot be a tekst')
        self._places = places
        if type(trunk_spaces) == str:
            raise TypeError('Trunk spaces cannot be a string')
        self._trunk_spaces = trunk_spaces

    def heigh(self):
        return self._heigh

    def combustion(self):
        return self._combustion

    def name(self):
        return self._name

    def id(self):
        return self._id

    def places(self):
        return self._places

    def trunk_space(self):
        return self._trunk_spaces

    def name_in_program(self):
        return 'Car'

    def change_name(self, new_name):
        if new_name == '':
            raise ValueError('New name cannot be empty')
        self._name = new_name

    def change_heigh(self, new_heigh):
        if type(new_heigh) == str:
            raise TypeError('The high of the car cannot be string, it must be a value')
        if new_heigh < 0:
            new_heigh = -new_heigh
        self._heigh = new_heigh

    def change_combustion(self, new_combustion):
        if new_combustion < 0:
            new_combustion = -new_combustion
        self._combustion = new_combustion

    def change_id(self, new_id):
        if type(new_id) == str:
            raise TypeError('Id number cannot be a string')
        if type(new_id) == float:
            new_id = int(new_id)
        self._id = new_id

    def change_places(self, new_places):
        if type(new_places) == str:
            raise TypeError('The amount of new places cannot be a string, it must be a number')
        if new_places < 0:
            new_places = - new_places
        if type(new_places) == float:
            new_places = int(new_places)
        self._places = new_places

    def change_trunk_spaces(self, new_trunk_spaces):
        if type(new_trunk_spaces) == str:
            raise TypeError('New value of trunk_spaces mus be a value, not a string')
        if new_trunk_spaces < 0:
            new_trunk_spaces = - new_trunk_spaces
        self._trunk_spaces = int(new_trunk_spaces)


class Bicycle(Vehicle):
    """This is a definition of the class Bicycle
    Bicycle inheritance from Vehicle
    It contains information about car atributes:
    1) All reserved terms -> list
    2) Information about vechicle availability -> int
    3) name -> str
    4) id -> int
    5) type_of_bicycle -> str
    6) tyres_size -> float
    This class contains also methods witch can change this atributes
    """
    def __init__(self, reserved_terms, available_status, id, name, type_of_bicycle, tyres_size):
        super().__init__(reserved_terms, available_status)
        correct_types_of_bicycles = [
            'mountain bike',
            'BMX bike',
            'Cross Country Bike',
            'Dutch Bike'
        ]
        if type(id) == str:
            raise TypeError('Value cannot be a string')
        if id < 0:
            id = -id
        self._id = int(id)
        if name == '':
            raise ValueError("The name cannot be empty")
        self._name = name
        if type_of_bicycle not in correct_types_of_bicycles:
            raise Invalid_Type_Of_Bicycle('This type of bicycle is not correct')
        self._type = type_of_bicycle
        if type(tyres_size) == str:
            raise TypeError('Tyres size must be a number not a string')
        if tyres_size < 0:
            tyres_size = -tyres_size
        self._tyres_size = int(tyres_size)
        self._name_in_program = 'Bicycle'

    def name(self):
        return self._name

    def type_of_bicycle(self):
        return self._type

    def name_in_program(self):
        return self._name_in_program

    def id(self):
        return self._id

    def tyres_size(self):
        return self._tyres_size

    def change_name(self, new_name):
        if new_name == '':
            raise ValueError('New name cannot be empty')
        self._name = new_name

    def change_id(self, new_id):
        if type(new_id) == str:
            raise TypeError('Id number cannot be a string')
        if type(new_id) == float:
            new_id = int(new_id)
        self._id = new_id

    def change_tyres_size(self, new_tyres_size):
        if type(new_tyres_size == str):
            raise TypeError('Tyres size cannot be a string')
        if new_tyres_size < 0:
            new_tyres_size = - new_tyres_size
        self._tyres_size = new_tyres_size

    def change_type_of_bicycles(self, new_type_of_bicycle):
        self._type == new_type_of_bicycle


class Lorry(Car):
    """This is a definition of the class Lorry
    Lorry inheritance from Car
    It contains information about car atributes:
    1) All reserved terms -> list
    2) Information about vechicle availability -> int
    3) heigh -> float
    4) name -> str
    5) id -> int
    6) combustion -> float
    7) places -> int
    8) trunk_spaces -> int
    9) lorry_capacity -> int
    This class contains also methods witch can change this atributes
    """
    def __init__(self, reserved_terms, available_status, heigh, combustion, name, id, places, trunk_spaces, lorry_capacity):
        super().__init__(reserved_terms, available_status, heigh, combustion, name, id, places, trunk_spaces)
        if type(lorry_capacity) == str:
            raise TypeError('Lorry capitality canno be a string')
        if lorry_capacity < 0:
            lorry_capacity = -lorry_capacity
        self._lorry_capacity = int(lorry_capacity)

    def lorry_capacity(self):
        return self._lorry_capacity

    def change_lorry_capitality(self, new_capitality):
        if type(new_capitality) == str:
            raise TypeError('lorry_capitality must not be a string')
        if new_capitality < 0:
            new_capitality = -new_capitality
        self._lorry_capacity = int(new_capitality)

    def name_in_program(self):
        return 'Lorry'


class Limousine(Car):
    """This is a definition of the class Limousine
    Limousine inheritance from Car
    It contains information about car atributes:
    1) All reserved terms -> list
    2) Information about vechicle availability -> int
    3) heigh -> float
    4) name -> str
    5) id -> int
    6) combustion -> float
    7) places -> int
    8) trunk_spaces -> int
    9) colour -> str
    10) length -> float
    This class contains also methods witch can change this atributes
    """
    def __init__(self, reserved_terms, available_status, heigh, combustion, name, id, places, trunk_spaces, colour, length):
        super().__init__(reserved_terms, available_status, heigh, combustion, name, id, places, trunk_spaces)
        if type(length) == str:
            raise TypeError('Length value cannot be a string')
        if length < 0:
            length = -length
        self._length = float(length)
        self._available_colours = [
            'black',
            'white',
            'blue',
            'orange',
            'purple',
            'red',
            'green'
        ]
        if type(colour) != str:
            raise TypeError('This type of colour is not a string')
        colour = colour.lower()
        if colour not in self._available_colours:
            raise Invalid_Colour_Error('This colour is out of the list')
        self._colour = colour

    def colour(self):
        return self._colour

    def length(self):
        return self._length

    def name_in_program(self):
        return 'Limousine'

    def change_colour(self, new_colour):
        new_colour = new_colour.lower()
        if new_colour not in self._available_colours:
            raise Invalid_Colour_Error('This colour is not on the list')
        if new_colour in self._available_colours:
            self._colour = new_colour

    def change_length(self, new_length):
        if type(new_length) == str:
            raise TypeError('Length cannot be a string')
        if new_length < 0:
            new_length = -new_length
        self._length = float(new_length)

    def available_colours(self):
        return self._available_colours


class Sport_car(Car):
    """This is a definition of the class Sport Car
    Sport Car inheritance from Car
    It contains information about car atributes:
    1) All reserved terms -> list
    2) Information about vechicle availability -> int
    3) heigh -> float
    4) name -> str
    5) id -> int
    6) combustion -> float
    7) places -> int
    8) trunk_spaces -> int
    9) zero_to_60 -> float
    This class contains also methods witch can change this atributes
    """
    def __init__(self, reserved_terms, available_status, heigh, combustion, name, id, places, trunk_spaces, zero_to_60):
        if type(zero_to_60) == str:
            raise TypeError('Zero_to_60 cannot be a string')
        super().__init__(reserved_terms, available_status, heigh, combustion, name, id, places, trunk_spaces)
        if zero_to_60 < 0:
            zero_to_60 = -zero_to_60
        self._zero_to_60 = float(zero_to_60)

    def name_in_program(self):
        return 'sport car'

    def zero_to_60(self):
        return self._zero_to_60

    def change_zero_to_60(self, new_zero_to_60):
        if type(new_zero_to_60) == str:
            raise TypeError('New value od zero_to_60 cannot be a string')
        if new_zero_to_60 < 0:
            new_zero_to_60 = -new_zero_to_60
        self._zero_to_60 = float(new_zero_to_60)


class RV(Car):
    """This is a definition of the class RV
    RV inheritance from Car
    It contains information about car atributes:
    1) All reserved terms -> list
    2) Information about vechicle availability -> int
    3) heigh -> float
    4) name -> str
    5) id -> int
    6) combustion -> float
    7) places -> int
    8) trunk_spaces -> int
    9) ability_to_pass_obstacles -> int
    This class contains also methods witch can change this atributes
    """
    def __init__(self, reserved_terms, available_status, heigh, combustion, name, id, places, trunk_spaces, ability_to_pass_obstacles):
        super().__init__(reserved_terms, available_status, heigh, combustion, name, id, places, trunk_spaces)
        if type(ability_to_pass_obstacles) == str:
            raise TypeError('Ability to pass the obstacles cannot be negative')
        if ability_to_pass_obstacles < 0:
            ability_to_pass_obstacles = -ability_to_pass_obstacles
        if ability_to_pass_obstacles > 100:
            ability_to_pass_obstacles = 100
        self._ability_to_pass_obstacles = ability_to_pass_obstacles

    def name_in_program(self):
        return 'RV'

    def ability_to_pass_obstacles(self):
        return self._ability_to_pass_obstacles

    def change_ability_to_pass_obstacles(self, new_ablity):
        if type(new_ablity) == str:
            raise TypeError('New value of ability cannot be a string')
        if new_ablity < 0:
            new_ablity = -new_ablity
        if new_ablity > 100:
            new_ablity = 100
        self._ability_to_pass_obstacles = int(new_ablity)
