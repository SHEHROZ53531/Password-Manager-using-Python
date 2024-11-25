# Password-Manager-using-Python
I have developed a Project Password Manager using python cryptography.
-----> PasswordManager Class

The PasswordManager class is the core of the script. It has several methods that allow users to create, load, and manage passwords.

-----> __init__ method

The __init__ method is the constructor of the class. It initializes the following instance variables:


1. self.key: a Fernet key used for encryption and decryption
2. self.Password_file: the path to the password file
3. self.Password_dict: a dictionary to store passwords

----->create_key method

The create_key method generates a new Fernet key and saves it to a file specified by the path parameter.

1. self.key = Fernet.generate_key(): generates a new Fernet key
2. with open(path, 'wb') as f:: opens the file in binary write mode ('wb')
3. f.write(self.key): writes the key to the file 

-----> load_key method

The load_key method loads a Fernet key from a file specified by the path parameter.

1. with open(path, 'rb') as f:: opens the file in binary read mode ('rb')
2.self.key = f.read(): reads the key from the file

----->create_password_file method

The create_password_file method creates a new password file and initializes it with the passwords from the initial_values dictionary (if provided).

1. self.Password_file = path: sets the password file path
2. if initial_values is not None:: checks if initial_values is not None
3. for key, value in initial_values.items():: iterates over the initial_values dictionary
self.add_password(key, value): adds each password to the password file using the add_password method

----->load_password_file method

The load_password_file method loads passwords from a file specified by the path parameter.

1. self.Password_file = path: sets the password file path
2. with open(path, 'r') as f:: opens the file in read mode ('r')
3. for line in f:: iterates over the lines in the file
4. site, encrypted = line.split(":"): splits each line into site and encrypted parts
5. self.Password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode(): decrypts the password using the Fernet key and stores it in the Password_dict

----->add_password method

The add_password method adds a new password to the password file.

1. self.Password_dict[site] = password: stores the password in the Password_dict
2. with open(self.Password_file, 'a+') as f:: opens the password file in append mode ('a+')
3. encrypted = Fernet(self.key).encrypt(password.encode()): encrypts the password using the Fernet key
4. f.write(site + ":" + encrypted.decode() + "\n"): writes the encrypted password to the file

----->get_password method

The get_password method returns the password for a given site.

1. return self.Password_dict[site]: returns the password from the Password_dict

----->Main Function

The main function is the entry point of the script. It creates a PasswordManager object and provides a menu-driven interface to interact with the password manager.

1. password = {...}: defines a dictionary of initial passwords
2. pm = PasswordManager(): creates a PasswordManager object
3. The script then enters a loop where it prompts the user to choose an action:
4. Create a new key
5. Load an existing key
6. Create a new password file
7. Load an existing password file
8. Add a new password
9. Get a password
10. Quit
Based on the user's choice, the script calls the corresponding method of the PasswordManager object.

Overall, this script provides a simple password manager that allows users to create, load, and manage passwords using the Fernet encryption algorithm.





