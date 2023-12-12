
import itertools

class Add_option:
    def __init__(self,alt,func,priority=0): # Lägger till en valfri parameter för prioritet
        self.alt = alt
        self.func = func
        self.priority = priority # Tilldelar prioritet till self

    def run(self):
        self.func()

    def display(self):
        print(self.alt)

    def __str__(self):
        return self.alt


class Menu:
    """
    skapa en meny eller en undermeny
    först använder du add_option för att skapa alternativ(text,funkttyion,prioriet(lägst kommer först)
    efter add_optionn är skapade passar du dem som en lista till Menu
    sen lägger du till ev undermeny med append till Menu.options
    då skapas en Back funktioni menyn
    sen starar du menyn med Menu.start() i en ev. loop för oändlig inmatning
    """
    count = itertools.count(1) # Skapar en räknare för att ge varje meny ett unikt id
    Menus = [] # Skapar en lista för att lagra alla menyer
    User = None # Lägger till en klassvariabel för att hålla reda på användaren

    def __init__(self,title,options,isSub=False):
        self.title = title
        self.options = options
        self.choice = None
        self.isSub = isSub
        self.id = next(Menu.count) # Tilldelar ett id till menyn
        Menu.Menus.append(self) # Lägger till menyn till listan
        self.parent = None
        #if self.isSub != None:
            #self.options.append("Back")
        if self.isSub == True: # Kontrollerar om menyn är en undermeny
            self.parent = Menu.Menus[self.id - 2] # Sätter föräldern till menyn som skapades innan
            #self.options.append(add_option("Back", self.parent.display))
            self.options.append(Add_option("Back",self.parent.start,9)) # Lägger till ett alternativ för att gå tillbaka till föräldern, med hög prioritet

        # Lägger till en instansvariabel för prioritet, som är summan av prioriteterna för alla alternativ
        self.priority = sum(option.priority for option in self.options) # Fixar felet


    def __str__(self):
        return self.title

    def addSubMenu(self,title,sub_options):
        #self.sub_title = title
        #self.sub_options = sub_options
        submenu = Menu(title,sub_options,True) # Skapar en undermeny med titel och alternativ
        #self.parent = self
        submenu.options.append(Add_option("Back",submenu.parent.start,9)) # Lägger till ett alternativ för att gå tillbaka till föräldern, med hög prioritet
        self.options.append(submenu) # Lägger till undermenyn till menyn



    def display(self):
        print("*"*30)
        print(self.title)
        #print("*"*30)
        for index,option in enumerate(self.options,start=1): # Skriver ut alla alternativ med nummer

            print(f'{index}. {option}')

        print("-"*30)


    def select(self):
        while True:
            try:
                self.choice = int(input("My choice: ")) # Tar emot ett val från användaren
                if 1 <= self.choice <= len(self.options): # Kontrollerar om valet är giltigt

                    break
            except ValueError: # Hanterar fel om användaren inte matar in ett nummer
                print("Error!Please Use a number to select!")

    def run(self):
        if self.isSub == True: # Kontrollerar om menyn är en undermeny
            while self.choice != len(self.options): # Lägger till en while-loop som kör tills användaren väljer Back-alternativet
                self.display() #Skriv ut meny
                #print(f"-{self.options[self.choice - 1]}- ")
                self.options[self.choice - 1].run() # kör vald funktion(första varvet händer inget, men det märker inte användaren)
                self.select()#Ta inmatning från användare


        if isinstance(self.options[self.choice - 1], Menu): # Kontrollerar om det valda alternativet är en undermeny
            # Skriver ut undermenyn och låter användaren välja ett alternativ
            self.options[self.choice - 1].display()
            self.options[self.choice - 1].select()
            self.options[self.choice - 1].run()  # Kör undermenyns run()-metod
        else:  # Lägger till ett else-villkor
            self.options[self.choice - 1].run()  # Kör funktionen som är kopplad till det valda alternativet
            self.options[self.choice - 1].display()

    def start(self, menu): # Lägger till en parameter för att ta emot en meny
        while True:
            if Menu.User is None: # Kontrollerar om User är None
                self.display() # Skriver ut huvudmen
                self.select()
                self.run()
            else:
                menu.display()
                menu.select()
                menu.run()
class Login_manager:

    def __init__(self,title):

        self.logedin_user = None
        self.users = {}
        self.__title = title
        with open("users.txt","r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    username,firstname,lastname,user_type,email,birthdate,phone_number,adress,password = line.split(",")
                    self.users[username] = {
                        "firstname":firstname,
                        "lastname":lastname,
                        "user_type":user_type,
                        "email":email,
                        "birth_date":birthdate,
                        "phone_number":phone_number,
                        "adress":adress,
                        "password":password}


    def create_user_objects(self):
        for user in self.users.keys():
            from ..users_components.user import Person,User
            firstname,lastname,user_type,email,birth_date,phone_number,adress,password = self.users[user].values()
            print(user,firstname,lastname,user_type,email,birth_date,phone_number,adress,password)
            username = user

            pers=Person(firstname,lastname,email,adress,birth_date,phone_number)
            print(pers)

            new_user = User(pers,username,password,user_type)
            print(new_user)




    def login(self):
        stored_username = ""
        while True:

            print("Enter your user credentials")
            if stored_username == "":
                username = input("Username: ")
            else:
                print(f"Username: {username}")
                username = stored_username
            if username in self.users.keys():
                password = input("Password: ")
                if self.users[username]["password"] == password:
                    self.logedin_user = username
                    print(f"Login successful! as {self.logedin_user}")
                    return True
                else:
                    print("Wrong password")
                    stored_username = username


    def update_file(self):
        # with open("users_components.txt","w") as f:
        #     for key,value in self.users_components.items():
        #         print(f'{key}:{value}')
        #         f.write(f'{key}:{value}\n')
        with open("users.txt","w") as f:
            for key,value in self.users.items():
                line = key+','
                line = line+','.join(str(element) for element in value)
                f.write(line+"\n")


#from .menu import *
