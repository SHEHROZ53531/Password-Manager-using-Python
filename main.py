from cryptography.fernet import Fernet


class PasswordManager :

     
    def __init__(self):
        self.key = None
        self.Password_file = None
        self.Password_dict = {}

    def create_key(self,path):
        self.key = Fernet.generate_key()  
        with open(path, 'wb') as f:
            f.write(self.key) 

    def load_key(self,path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_password_file(self, path ,initial_values=None):
        self.Password_file=path


        if initial_values is not None:
            for key , value in initial_values.items():
                self.add_password(key,value)
    

    def load_password_file(self,path):
        self.Password_file = path

        with open(path,'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.Password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()


    def add_password(self, site, password):
        self.Password_dict[site] = password

        with open(self.Password_file, 'a+') as f:
            encrypted = Fernet(self.key).encrypt(password.encode())
            f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.Password_dict[site]



def main():
    password = {
        "email": "123456",
        "f1acebook": "myFbPassword",
        "youtube": "Helloworld123",

    }   

    pm =PasswordManager()

    print(""" What do you want to do?
          (1) create a new key
          (2) load an exsisting key
          (3) create a new password file
          (4) load an exsisting password file
          (5) Add a new password 
          (6) get a password 
          (q) Quit

          """) 

    done = False

    while not done:

        choice = input("Enter Your choice : ")
        if choice == "1":
            path = input("Enter path : ")
            pm.create_key(path)

        elif choice == "2":
            path = input("Enter path : ")
            pm.load_key(path)

        elif choice == "3":
            path = input("Enter path : ")
            pm.create_password_file(path, password)  

        elif choice == "4":
            path = input("Enter path : ")   
            pm.load_password_file(path)

        elif choice == "5":
            site = input("Enter the site : ")     
            password = input("Enter the password :")
            pm.add_password(site, password)

        elif choice == "6":
            site = input("What site do you want : ")  
            print(f"Password for {site} is {pm.get_password(site)}")

        elif choice == "q":
            done = True
            print("Good bye User !!!!")
        else:
            print('Invalid choice')


if __name__ == "__main__":
    main()

                        



        




         

    
        
