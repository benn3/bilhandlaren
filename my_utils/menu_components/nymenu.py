from my_utils.user_components import user as user

class addOption:
    def __init__(self,text,func,priority=9,menu=None):
        self.text = text
        self.func = func
        self.menu = menu
        self.priority = priority


    def run(self):
        if self.menu is not None:
            self.func(self.menu)
        else:
            self.func()
    def display(self):
        return self.text
        #print(self.text)
    def prio(self):
        return self.priority
    def __str__(self):
        return self.text

class newMenu:
    User = None
    user_type_menu = {}
    def __init__(self,title,options,submenu=False):
        self.title = title
        self.options = options
        self.submenu = submenu

        self.child = None
        if self.submenu == True:
            pass
    def move_element_by_text(self, txt):
        # Skapa en kopia av options för att undvika att påverka originalet direkt
        options_copy = self.options.copy()

        for option in options_copy:

            if option.display() == txt:
                # Ta bort det matchande elementet från options_copy
                options_copy.remove(option)
                # Lägg till det matchande elementet längst bak i options_copy
                options_copy.append(option)
                break

        # Uppdatera self.options med den modifierade kopian
        self.options = options_copy
        print(self.options)

    def sortOptions(self):
        # Skapa en ny lista som innehåller alla alternativ som inte är newMenu-objekt
        options_list = [opt for opt in self.options if not isinstance(opt, newMenu)]
        # Sortera listan efter prioritet med sorted-funktionen och lambda-funktionen
        sorted_list = sorted(options_list, key=lambda x: x.prio())
        # Lägg till newMenu-objektet sist i den sorterade listan
        sorted_list.append(self.options[-1])
        # Returnera den sorterade listan
        return sorted_list

    def add_type_menu(self,menu,user_type):
        newMenu.user_type_menu[user_type] = menu



    def display(self):
        options = self.options #tilldela self.options till option för att inte använda en specifik meny(self)
        title = self.title
        if user.lm.check_user_type():# om en användare är inloggad returnera användare och typ
             User,type = user.lm.check_user_type() #använd typ för att hämta rätt meny

             options = newMenu.user_type_menu[type].options # visa rätt meny
             title = newMenu.user_type_menu[type].title
             print(f"- {User} -")


        print('*'*15+title)
        for index,option in enumerate(options,start=1):

            if isinstance(option,newMenu):
                pass
            print(" "*3+f"{index}. {option}")
        print('-'*15)
    def run(self):
        title = self.title
        options = self.options
        if user.lm.check_user_type():  # om en användare är inloggad returnera användare och typ
            User, type = user.lm.check_user_type()  # använd typ för att hämta rätt meny
            options = newMenu.user_type_menu[type].options
        if self.submenu == True:
            while self.choice != len(self.options):
                self.display()# skriv ut undermeny
                options[self.choice - 1].run()
                self.select()

        if isinstance(self.options[self.choice - 1],newMenu):
            options[self.choice - 1].display()
            options[self.choice - 1].select()
            options[self.choice - 1].run()
        else:
            options[self.choice - 1].run()
            options[self.choice - 1].display()
            #self.options[self.choice - 1].select()

    def start(self,menu):
        while True:
            if newMenu.User is None:
                self.display()
                self.select()
                self.run()
            else:
                menu.display()
                menu.select()
        pass
    def select(self):
        while True:
            try:
                self.choice = int(input(" "*15+"Enter your choice: "))
                if 1 <= self.choice <= len(self.options):
                    break
            except ValueError:
                print("Bad input! BAD!!")
    def createSubMenu(self,title,options):
        back = addOption("back", self.start,9, self)
        options.append(back)
        submenu = newMenu(title,options,True)
        self.options.append(submenu)
        self.child = submenu
        submenu.parent = self


    def __str__(self):
        return self.title

user_type1_option1=addOption("Display my details",lambda: print("My details"))
user_type1_option2=addOption("Change personal information",lambda:print("Changing settings.."))
user_type1_option3=addOption("Logout",user.lm.logout)
user_type1_menu = newMenu("Admin menu",[user_type1_option1,user_type1_option2,user_type1_option3])


option1 = addOption("Say Hello",lambda: print('Hello'),2)
#option2 = addOption("login",lambda : print("loggin in"),1)
option2 = addOption("Login",user.lm.login)
option3 = addOption("Logout",user.lm.logout,2)
option5 = addOption("exit",lambda : exit(),8)
suboption1 = addOption("Sub say hello",lambda :print("Sub hello"),3)
suboption2 = addOption("sub login",lambda: print("sub login"),1)
menu = newMenu("Main menu",[option1,option2,option3,option5])
menu.createSubMenu("My submenu",[suboption1,suboption2])
menu.move_element_by_text('exit')
#menu.move_element_by_text("My submenu")
menu.add_type_menu(user_type1_menu,1)
#suboption3 = addOption("back",menu.start,menu)

#menu.options.append(newMenu("My submenu",[suboption1,suboption2],True))
#print(menu.sortOptions())
menu.start(menu)
menu.options[-1].createSubMenu("New submenu",[1,2,3])
