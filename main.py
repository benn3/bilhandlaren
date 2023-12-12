from my_utils.menu_components.menu import Menu,Add_option,Login_manager
from my_utils.users_components.user import Person,User
from my_utils.car_components.car import Car
import my_utils.menu_components.login_manager
def start_menu(login_manager,user_type):
    lm = login_manager
    option1 = Add_option("List cars",Car.list_cars,1)

    #option1 = add_option("Create an account", make_account, 1) # Lägger till en prioritet för att sortera alternativen
    option2 = Add_option("Login", lm.login, 2)
    #option3 = add_option("Logout", logout, 3) # Lägger till ett alternativ för att logga ut
    option3 = Add_option("Exit", exit, 10) # Lägger till en prioritet för att sortera alternativen

    # Skapar en huvudmenu med alternativen
    main_menu = my_utils.menu_components.menu.Menu("Main Menu", [option1, option2, option3])


    # Skapar några undermenualternativ
    sub_option1 = Add_option("Say hello", lambda: print(f"Hello, {Menu.User}!")) # Använder en lambda-funktion för att skriva ut ett hälsningsmeddelande med användarnamnet
    sub_option2 = Add_option("Do something", lambda: print("Doing something...")) # Använder en lambda-funktion för att skriva ut ett meddelande
    sub_option3 = Add_option("Do something else", lambda: print("Doing something else..."))
    #sub_menu = menu.Menu("User Menu",[sub_option1,sub_option2,sub_option3])
    main_menu.start(main_menu)

def user_type1_menu():

    global lm
    option1 = menu.add_option("Handle Cars",lambda: print("Here we can manage Cars"),1)
    option2 = menu.add_option("Handle Users",lambda: print("Here we can manage Users"),2)
    option3 = menu.add_option("Logout",lm.logout,4)
    option4 = menu.add_option("Edit my preference",lambda:print("Here i can change my settings",3))
def user_type2_menu():
    pass
def user_type3_menu():
    pass
def default_menu():
    pass


class add_option:
    def __init__(self):
        pass


class Menu:
    def __init__(self):
        pass

    def run(self):
        pass

    def display(self):
        pass

    def select_option(self):
        pass

    def create_sub_menu(self, menu):
        pass


def menu_option1():
    pass


def menu_option2():
    pass


def menu_option3():
    pass


def sub_menu_option1():
    pass


def sub_menu_option2():
    pass


def sub_menu_option3():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #register()
    #if login():
    person1 = Person("Benjamin", "Andersson", "ben52646.andersson@gmail.com", "Televägen 1", 19890423, +460722065588)
    person2 = Person("Ben", "Andersson", "ben52646.andersson@gmail.com", "televägen 1", "19900422", +46722065588)
    user1 = User(person1, "Ben", "ben123", 1)
    user2 = User(person2, "b3n", "benne123", 1)

    car1 = Car("abc123","Volvo","V70",1999,100000,50000,user2)
    car2 = Car("def456", "BMW", "F90", 2010, 1000000, 20000, user1)

    lm = Login_manager("Bilhandlaren")
    #lm.login()
    start_menu(lm,4)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
