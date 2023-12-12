from ..user_components import *
from my_utils import common_functions
from my_utils.common_functions import today
class Car:
    """
    The Car class is used to create cars for the system\n
    rplate is the unique identifier of an car and\n
    brand,model explains itself, year is the year the car was produced\n
    trip is the total miles the car has gone,\n
    estValue is the estimated car value, and\n
    owner is either a user object or in company storage\n
    using print with a ar object tells you\n
    brand, model, year and who owns it.\n
    You can use the owner method to assign a new owner for a car object.
    """

    all_cars = {}

    def __init__(self,rplate,brand,model,year,trip,estValue=999,owner="In storage"):


        self.__rplate = rplate
        self.__brand = brand
        self.__owner = owner
        self.__model = model
        self.__year = year
        self.__trip = trip
        self.__estValue = estValue
        self.__owner = owner
        self.__date_created = today()
        self.__problems = []
        Car.all_cars[rplate] = {"brand": brand, "model": model, "year": year, "trip": trip, "owner": owner, "estValue": estValue}

    @property
    def owner(self):
        return self.__owner

    def printCustomer(self):
        print(self.owner)

    def has_problems(self):
        # Kontrollera om __problems listan har några element
        if len(self.__problems) > 0:
            # Returnera True
            return True
        else:
            # Returnera False
            return False
    @classmethod
    def list_cars(cls):
        for index,rplate in enumerate(Car.all_cars.keys(),start=1):
            #print(Car.all_cars[rplate].items())
            brand,model,year,trip,owner,estValue = Car.all_cars[rplate].values()
            print(f'Car {index}. {brand} of model:{model} witch has a total miles driven of {trip} and is has a '
                  f'estimated value of {estValue} the car is registered to {owner.get_firstname()} ')






    def get_problems(self):
        # Skapa en tom sträng som ska fyllas med problemen
        problems = ""
        # Kontrollera om __problems listan har några element
        if len(self.__problems) > 0:
            # Kombinera elementen i listan till en sträng med kommatecken
            problems = ", ".join(self.__problems)
        # Returnera strängen
        return problems

    def remove_problem(self, problem):
        # Kontrollera om problemet finns i __problems listan
        if problem in self.__problems:
            # Ta bort problemet från __problems listan
            self.__problems.remove(problem)
        else:
            # Skriv ut ett felmeddelande
            print(f"{problem} finns inte i listan över problem")

    def add_problem(self, problem):
        # Lägg till problemet i __problems listan
        self.__problems.append(problem)

    def __str__(self):
        # Skapa en tom sträng som ska fyllas med information
        message = ""
        # Lägg till information om registreringsplåten, märket, modellen och året för bilen
        message += f"Detta är en {self.__brand} {self.__model} från {self.__year} med registreringsplåten {self.__rplate}. "
        # Kontrollera om bilen har en ägare eller är i förvaring
        if self.__owner == "In storage":
            # Lägg till information om att bilen är i förvaring
            message += "Bilen är i förvaring och väntar på en ny ägare. "
        else:
            # Lägg till information om ägaren av bilen
            message += f"Bilen ägs av {self.__owner}. "
        # Lägg till information om miltal och estimerat värde för bilen
        message += f"Bilen har kört {self.__trip} km och har ett estimerat värde på {self.__estValue} kr. "
        # Lägg till information om datumet då bilen skapades
        message += f"Bilen skapades den {self.__date_created}. "
        # Kontrollera om bilen har några problem eller varningar
        if self.has_problems():
            # Lägg till information om problemen eller varningarna som bilen har
            message += f"Bilen har följande problem eller varningar: {self.get_problems()}. "
        # Returnera det färdiga meddelandet
        return message

    def set_owner(self,owner):
        self.__owner = owner

    def book_vehicle_inspection(self):
        pass

    def add_user_as_owner(self, user):
        # Kontrollera om användaren är ett objekt av klassen User
        if isinstance(user, User):
            # Uppdatera ägaren av bilen
            self.__owner = user
            # Uppdatera klass variabeln all_cars
            Car.all_cars[self.__rplate]["owner"] = user
        else:
            # Skriv ut ett felmeddelande
            print("Användaren måste vara ett objekt av klassen User")

    # En metod för att sortera alla bil objekts egenskap i ordning

def create_car():
    details = ["rplate","brand","model","year","trip","estValue","owner"]
    new_object_values = {}
    for detail in details:
        user_input = input(f"enter a value for {detail}: ")
        new_object_values[detail] = user_input
    new_object = Car(*list(new_object_values.values()))
    return new_object

