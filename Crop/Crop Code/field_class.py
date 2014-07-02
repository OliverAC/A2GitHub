from potato_class import *
from wheat_class import * 
from Sheep_class import *
from Cow_class import *
import random

class Field:
    """ Simulate a fiel that can contain animals and plants"""

    #constructor
    def __init__(self,max_animals, max_crops):
        self._crops =[]
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

    def plant_crop(self,crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False

    def add_animal(self,animal):
        if len(self._animals) < self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False

    def harvest_crop(self,position):
        return self._crops.pop(position)

    def remove_animal(self,position):
        return self._animals.pop(position)

    def report_contents(self):
        crop_report = []
        animal_report = []
        for crop in self._crops:
            crop_report.append(crop.report())
        for animal in self._animals:
            animal_report.append(animal.report())
        return {"crops": crop_report, "animals": animal_report}

    def report_need(self):
        food = 0
        light = 0
        water =0
        for crop in self._crops:
            needs = crop.needs()
            if needs["light need"] > light:
                light = needs["light need"]
            if needs["water need"] > water:
                water = needs["water need"]
        for animal in self._animals:
            needs = animal.needs()
            food += needs["Food need"]
            if needs["water need"] > water:
                water = needs["water need"]
        return {"food":food, "light":light, "water":water}

    def grow(self, light, food, water):
        if len(self._crops)>0:
            for crop in self._crops:
                crop.grow(light,water)
        if len(self._animals) > 0:
            food_required = 0
            for animal in self._animals:
                needs = animal.needs()
                food_required += needs["Food need"]
        if food>food_required:
            additional_food = food - food_required
            food = food_required
        else:
            additional_food = 0
        for animal in self._animals:
            needs = animal.needs()
            if food >= needs["Food need"]:
                food-= needs["Food need"]
                feed = needs["Food need"]
                if additional_food >0:
                    additional_food-=1
                    feed +=1
                    animal.grow(feed,water)
            
                              
def manual_grow(field):
    valid = False
    while not valid:
        try:
            light = int(input("Please enter light value:  "))
            if 0<light<11:
                valid = True
            else:
                print("invalid input!")
        except ValueError:
            print("invalid input")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter water value:  "))
            if 0<water<11:
                valid = True
            else:
                print("invalid input!")
        except ValueError:
            print("invalid input")
    valid = False
    while not valid:
        try:
            food = int(input("Please enter food value:  "))
            if 0<food<11:
                valid = True
            else:
                print("invalid input!")
        except ValueError:
            print("invalid input")
    field.grow(light,food,water)

    def auto_grow(self,days):
        for days in range(days):
            light = random.randint(1,10)
            water = random.randint(1,10)
            food = random.randint(1,10)
            field.grow(light,food,water)


def display_animal_menu():
    print()
    print("Which Animal? ")
    print()
    print("1. Cow")
    print("2. Sheep")
    print()
    print("0. No entery")
    print()
    print("Please select an option")

def display_crop_menu():
    print()
    print("Which Crop? ")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("0. No entery")
    print()
    print("Please select an option")

def display_main_menu():
    print()
    print("1. new crop")
    print("2. Harvest crop")
    print()
    print("3. Add an animal")
    print("4. remove an animal")
    print()
    print("5. Manual Grow")
    print("6. Auto Grow")
    print()
    print("7. Report field status")
    print()
    print("8. exit")
    print("Please select from above")

def get_menu_choice(lower,upper):
    valid = False
    while not valid:
        try:
            choice = int(input("Option Selected"))
            if lower <= choice <= upper:
                valid = True
            else:
                print("Invalid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def add_animal_to_field(field):
    display_animal_menu()
    choice = get_menu_choice(0,2)
    if choice == 1:
        if field.add_animal(Cow()):
            print()
            print("Cow added")
            print()
        else:
            print()
            print("Field is full - Cow not added")
            print()
    elif choice == 2:
        if field.add_animal(Sheep()):
            print()
            print("Sheep Added")
            print()
        else:
            print()
            print("Field is full - Sheep not planted")
            print()

def plant_crop_in_field(field):
    display_crop_menu()
    choice = get_menu_choice(0,2)
    if choice == 1:
        if field.plant_crop(Potato()):
            print()
            print("Potato Planted")
            print()
        else:
            print()
            print("Field is full - potato not planted")
            print()
    elif choice == 2:
        if field.plant_crop(Wheat()):
            print()
            print("Wheat Planted")
            print()
        else:
            print()
            print("Field is full - Wheat not planted")
            print()

def manage_field(field):
    print("This is the field management program")
    print()
    exit = False
    while not exit:
        display_main_menu()
        option = get_menu_choice(0,7)
        print()
        if option == 1:
            plant_crop_in_field(field)
        elif option == 2:
            removed_crop = harvest_crop_from_field(field)
            print("You removed the crop: {0}".format(removed_crop))
        elif option ==3:
            add_animal_to_field(field)
        elif option == 4:
            removed_animal = remove_animal_from_field(field)
            print("You removed a: {0}".format(removed_animal))
        elif option == 5:
            manual_grow(field)
        elif option == 6:
            auto_grow(field,30)
        elif option == 7:
            print(field.report_contents())
            print()
        elif option == 0:
            exit = True
            print()
        



def display_crops(crop_list):
    print()
    print("The following crops are in this field:  ")
    pos = 1
    for crop in crop_list:
        print("{0:>2}. {1}".format(pos,crop.report()))
        pos += 1    

def display_animals(animal_list):
    print()
    print("The following animals are in this field:  ")
    pos = 1
    for animal in animal_list:
        print("{0:>2}. {1}".format(pos,animal.report()))
        pos += 1

def select_crop(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select a crop:  "))
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("Please enter a valid option!")
        return selected - 1

def select_animal(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select an animal:  "))
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("Please enter a valid option!")
        return selected - 1

def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop = select_crop(len(field._crops))
    return field.harvest_crop(selected_crop)
    
def remove_animal_from_field(field):
    display_animals(field._animals)
    selected_animal = select_animal(len(field._animals))
    return field.remove_animal(selected_animal)
    


def main():
    new_field = Field(5,2)
    manage_field(new_field)
    


    
if __name__ == "__main__":
    main()
