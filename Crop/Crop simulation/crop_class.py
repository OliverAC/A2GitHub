import random

class Crop:
    """ A generic food crop"""

    #constructor
    def __init__(self,growth_rate, light_need, water_need):
        #set the attributes with an initial value
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
        #the above attributesare prefixed with an underscore to indicate
        #that they should not be accesses directly from outwith the class
 
    def needs(self):
            #return a dictonary containing the light and water needs
            return{"light need":self._light_need, 'water need':self._water_need}

    def report(self):
            #returns a dictionary containing the type, status, growth and of growing
            return{'type ':self._type, 'status':self._status, 'growth':self._growth, 'days growing' :self._days_growing}

    def _update_status(self):
        if self._growth >15:
            self._status = "Old"
        elif self._growth >10:
                self._status = "Mature"
        elif self._growth >5:
                self._status = "Young"
        elif self._growth >0:
                self._status = "Seedling"
        elif self._growth ==0:
                self._status = "Seed"

    def grow(self,light,water):
        if light>= self._light_need and water>=self._water_need:
            self._growth += self._growth_rate
        #increment days growing
        self._days_growing +=1
        ##update the status
        self._update_status()

def manual_grow(crop):
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value (1-10):  "))
            if 0< light <11 :
                        valid = True
            else:
                        print("Invalid input...")
        except ValueError:
            print("Invalid input...")
        valid = False
        while not valid:
            try:
                water = int(input("Please enter a water value (1-10):  "))
                if 0<water<11:
                        valid = True
                else:
                        print("Invalid input...")
            except ValueError:
                print("Invalid Input... ")
    crop.grow(light,water)

def auto_grow(crop, days):
    # grow the crop
    for says in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

def display_menu():
    print("1. grow manually over one day")
    print("2. grow automatically over 30 days")
    print("3. report status")
    print("0. exit the program")
    print()
    print("please select an option from the above menu")


def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected:  "))
            if 0<= choice <= 4:
                 option_valid = True
            else:
                 print("Please enter a valid option")
        except ValueError:
                 print("Please enter a valid option")
    return choice

def manage_crop(crop):
         print("This is the crop management progrem")
         print()
         noexit = True
         while noexit:
            display_menu()
            option = get_menu_choice()
            print()
            if option ==1 :
                    manual_grow(crop)
                    print()
            elif option ==2 :
                    auto_grow(crop,30)
                    print()
            elif option ==3 :
                    print(crop.report())
                    print()
            elif option == 0:
                noexit = False


def main(): # initiate the class
    new_crop = Crop(1,4,3)
    manage_crop(new_crop)

if __name__ == "__main__":
    main()
        
