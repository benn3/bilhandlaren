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

    def __init__(self,title,options,submenu=False):
        self.title = title
        self.options = options
        self.submenu = submenu

        self.child = None
        if self.submenu == True:
            pass
            #back = addOption("back", self.start, self)
            #options.append(back)

    def sortOptions(self):
        # Skapa en ny lista som innehåller alla alternativ som inte är newMenu-objekt
        options_list = [opt for opt in self.options if not isinstance(opt, newMenu)]
        # Sortera listan efter prioritet med sorted-funktionen och lambda-funktionen
        sorted_list = sorted(options_list, key=lambda x: x.prio())
        # Lägg till newMenu-objektet sist i den sorterade listan
        sorted_list.append(self.options[-1])
        # Returnera den sorterade listan
        return sorted_list


    def display(self):
        print('*'*15+self.title)
        for index,option in enumerate(self.options,start=1):
            if isinstance(option,newMenu):
                #print(f"{index}.{option.title}")
                pass
            print(f"{index}.{option}")
        print('-'*15)
    def run(self):
        if self.submenu == True:
            while self.choice != len(self.options):
                self.display()# skriv ut undermeny
                self.options[self.choice - 1].run()
                self.select()

        if isinstance(self.options[self.choice - 1],newMenu):
            self.options[self.choice - 1].display()
            self.options[self.choice - 1].select()
            self.options[self.choice - 1].run()
        else:
            self.options[self.choice - 1].run()
            self.options[self.choice - 1].display()
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
                self.choice = int(input("Enter your choice"))
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


option1 = addOption("Say Hello",lambda: print('Hello'),2)
option2 = addOption("login",lambda : print("loggin in"),1)
option3 = addOption("exit",lambda : exit(),14)
suboption1 = addOption("Sub say hello",lambda :print("Sub hello"),3)
suboption2 = addOption("sub login",lambda: print("sub login"),1)
menu = newMenu("Main menu",[option1,option2,option3])
#suboption3 = addOption("back",menu.start,menu)
menu.createSubMenu("My submenu",[suboption1,suboption2])
#menu.options.append(newMenu("My submenu",[suboption1,suboption2],True))
#print(menu.sortOptions())
menu.start(menu)
menu.options[-1].createSubMenu("New submenu",[1,2,3])
