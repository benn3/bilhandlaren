
import datetime,itertools
from ..common_functions import today


class Person:



    all_persons = {}


    def __init__(self, firstname=None, lastname=None, email=None, adress=None, birth_date=None,phone_number=None):


        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.adress = adress
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.created = today() # Spara datumet personen skapades
        if self.validate_birth(self.birth_date):
            Person.all_persons[self.birth_date] = self
        else:
            self.create_birthdate()
            Person.all_persons[self.birth_date] = self
        #Person.all_persons.append(self) #Lägg til sig själv i all_persons klass listan

    def __str__(self):
        return f'{self.__firstname} {self.__lastname}'
    def get_firstname(self):
        return self.__firstname
    def get_lastname(self):
        return self.__lastname
    def get_email(self):
        return self.__email
    def set_firstname(self,new_Name):
        self.__firstname = new_Name

    def list_self(self):
        return [self.firstname,self.lastname,self.email,self.adress,self.birth_date,self.phone_number]

    def create_birthdate(self):
        print("If you were born before October or before the 10th day of the month\n"
              ", make sure to include a leading zero.")
        year = int(input("enter the year you was born: "))
        month = int(input("enter the month u were born: "))
        day = int(input("enter date: "))
        self.birth_date = datetime.date(year=year,month=month,day=day)
        print(self.birth_date)
        return self.birth_date

    def validate_birth(self, date_string):
        # Kontrollera om date_string är ett giltigt datumvärde i YYYY-MM-DD
        date_string = str(date_string) #omvandla datum till en sträng
        if '-' in date_string:
            date_string = date_string.replace('-', '')#ta bort ut ev. bindestreck

        try:
            if len(date_string) == 8:#kontrollera om det är 8 siffrore som i YYYYMMDD

                year = int(date_string[:4])#ta 4 första tecken och sätt som år
                month = int(date_string[4:6])# ta 4de till 6te tecken som månad
                day = int(date_string[6:8])# ta tecken 6-8 som dag
            else:
                self.create_birthdate()#ogiltig längd så fråga användaren om nytt datum

            if 1900 <= int(year) <= 2024 and 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                date = datetime.date(year=year, month=month, day=day)
                self.birth_date = date
                return True
            else:
                print("Invalid birth date. Please try again.")
                #self.create_birthdate()
                return self.validate_birth(self.create_birthdate())

        except ValueError:
            print("Invalid input. Please try again.")
            print(self.birth_date)
            #self.create_birthdate()
            return self.validate_birth(self.create_birthdate())

# Skapa en klass som representerar en användare
class User(Person):

    id_count = itertools.count(1)
    all_users = {}

    def __init__(self,person_instance,username,password,user_type=3):

        super().__init__(person_instance.get_firstname(),person_instance.get_lastname(),
                         person_instance.get_email(),person_instance.adress,
                         person_instance.birth_date,person_instance.phone_number) # Skicka personobjektet som ett argument
        self.__username = username
        self.__password = password
        self.__user_type = user_type
        self.__created = today()
        self.__parent = person_instance # Spara personobjektet som ett attribut
        self.__firstname = self.__parent.get_firstname()
        self.__lastname = self.__parent.get_lastname()
        self.__email = self.__parent.get_email()
        self.__id = next(User.id_count)
        User.all_users[self.__username] = self
        #User.all_users.append(self)
        # Resten av koden
    def __str__(self):
        return f'{self.__firstname} {self.__lastname} has the {self.__username} account with {self.__email} on {self.adress}'


    def print_users(self):
        for index,user in enumerate(User.all_users.keys(),start=1):
            print(f'{index}. {user}')


    def check_password(self,pw):
        if self.__password == pw:
            return True
        else:
            return False
    @classmethod
    def check_user_type(cls,username):
        if User.all_users[username]:
            return User.all_users[username]["user_type"]
        else:
            return print("Theres no user with that username, try again")
class login_manager:

    # def __init__(self,title):
    #     self.logedin_user = None
    #     self.users_components = {}
    #     self.title = title
    #     with open("users_components.txt", "r") as f:
    #         lines = f.readlines()
    #         for line in lines:
    #             line = line.strip()
    #             if line:
    #                 key, value = line.split(":")
    #                 self.users_components[key] = value
    def __init__(self,title):
        self.logedin_user = None
        self.users = {}
        self.__title = title
        with open("users_components.txt","r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    username,firstname,lastname,user_type,email,birthdate,phone_number,adress,password = line.split(",")
                    #self.users_components[username] = [firstname,lastname,user_type,email,adress,password]
                    self.users[username] = {
                        "firstname":firstname,
                        "lastname":lastname,
                        "user_type":user_type,
                        "email":email,
                        "birth_date":birthdate,
                        "phone_number":phone_number,
                        "adress":adress,
                        "password":password}
        # for user in self.users_components.keys():
        #     print(user," ",self.users_components[user].items())

    def create_user_objects(self):
        for user in self.users.keys():
            firstname,lastname,user_type,email,birth_date,phone_number,adress,password = self.users[user].values()
            print(user,firstname,lastname,user_type,email,birth_date,phone_number,adress,password)
            username = user
            pers =Person(firstname,lastname,email,adress,birth_date,phone_number)
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
        with open("users_components.txt","w") as f:
            for key,value in self.users.items():
                line = key+','
                line = line+','.join(str(element) for element in value)
                f.write(line+"\n")


            #for firstname,lastname,user_type,email,adress,password in self.users_components[key]:
            #    print(f"{key},{firstname}, {lastname}, {user_type}, {email}, {adress}, {password}")



    # def register(self):
    #     username = None
    #     password = None
    #     while True:
    #         username = input("Enter a username of your choice: ")
    #         if password == None:
    #             password = input("Enter a password for that user: ")
    #
    #             if username not in list(self.users_components.keys()):
    #
    #                 self.users_components[username] = password
    #
    #                 print("Register successful, you'll have to fill in your contact info upon first login!")
    #                 return True
    #             else:
    #                 print("User exsists! try enter another username")
    def register(self,user):
        username = input("Enter a username: ")
        if username not in list(self.users.keys()):
            self.users[username] = user.self_list()
            password = user.self_list()[-1]
            print("Register complete!")

    def logout(self):
        if self.logedin_user is None:
            print("Theres no user logedin atm")
        else:
            self.logedin_user = None

    def __str__(self):
        return

def register_user():
    questions = ["firstname","lastname","user type","e-mail","adress","password"]

    answer = []
    print("Enter ypour details when asked, until done")
    for question in questions:
        answer.append(input(f'My {question} is: '))
    #User(firstname, lastname, user_type, email, password)
    return User(*answer)

def create_Person():
    person_questions = ["firstname","lastname","email","adress","birth_date","phone_number"]
    person_info = {}
    for question in person_questions:
        person_info[question] = input(f"What is the persons {question}?\n: ")
    print(person_info)
    person = Person(**person_info)
    return person


#user3 = register_user()
#print(user3)

person1 = Person("Benjamin","Andersson","ben52646.andersson@gmail.com","Televägen 1",19890423,+460722065588)
user1 = User(person1,"Ben","ben123",1)
#person1.create_birthdate()

print(user1)
#user2 = User()
#user1 = User("benjamin","andersson",1,"ben52646.andersson@gmail.com","televägen 1","benne123")
#user2 = User("olof","palm",1,"palm@urkraft.se","vetej 1","palm")
    #v1 = create_Person()
person2 = Person("Ben","Andersson","ben52646.andersson@gmail.com","televägen 1","19900422",+46722065588)
user3 = User(person2,"b3n","benne123",1)
#person2.validate_birth("19890423")

user3.print_users()
print(user3.check_password("benne12"))
#skräp nedan
#obj1 = Test1("benjamin","Andersson","ben")
#obj2 = Test2(obj1)
