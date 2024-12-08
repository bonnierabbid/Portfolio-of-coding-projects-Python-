  
    
# Exercise 7: Password Checker

def main():
    #Conditions
    is_runing = True
    length = False
    uppercase = False
    lowercase = False
    number = False
    no_space = False

    while is_runing:
        #Print the rules and get the user password input
        password = str(input("Please enter yor password meets theses rules: \n"
                            "o	At least 8 characters long\n"
                            "o	Contains at least one uppercase letter\n"
                            "o	Contains at least one lowercase letter\n"
                            "o	Contains at least one number\n"
                            "o	Does not contain spaces\n"
                            "Enter your password: ")).strip()
        #check length, unppercase, lowercase, number
        if len(password) >= 8:
            length = True

        for x in password:
                if x.isupper():
                    uppercase = True
                if x.islower():
                    lowercase = True
                if x.isdigit():
                    number = True
                if x.isspace():
                    no_space = True
        
        #print fail result
        if length == False:
            print("\n*Failed! Less than 8 characters long")
        else:
            print("\no Password contains at least 8 characters.")
        if uppercase == False:
            print("*Failed! Uppercase letters not included")
        else:
            print("o Password contains uppercase characters")
        if lowercase == False:
            print("*Failed! Lowercase letters not included")
        else:
            print("o Password contains lowercase characters")
        if number == False:
            print("*Failed! Does not contain numbers")
        else:
            print("o Password contains numbers")
        if no_space == True:
            print("*Failed! Space are included")
        else:
            print("o Password does not contain Space")
        
        # Break loop or initionlization
        if length and uppercase and lowercase and number and no_space == False:
            print("\n$ Good Job!! Thats a strong password!")
            break
        else:
            length = False
            uppercase = False
            lowercase = False
            number = False
            no_space = False
            print("$ Failed passwords. Let's try it again.\n")


if __name__ == "__main__":
    main()
            
         
    