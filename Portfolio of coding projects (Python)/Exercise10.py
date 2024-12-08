
#Exercise 10: File Reader and Writer

#import datetime
from datetime import datetime

#Creat file
file_name = 'diary.txt'


def main():
    while True:
        #Get datetime in frame
        today = datetime.now().strftime("%d-%m-%Y")
                
        #Print the menu
        user_selection = str(input("\nDiary Menu\n"
                               "1. Add Diary\n"
                               "2. Empty Diary\n"
                               "3. Read all content\n"
                               "4. Exit\n"
                               "Please enter your choice: "))
          
        #Add diary
        if user_selection == "1":
            user_writing = input("What did you do today? \n")
            with open(file_name, 'a') as file:
                file.write(user_writing + " " + today + "\n")
            print("Diary added!")

        #Empty diary
        elif user_selection == '2':
            open(file_name, 'w').close()
            print("The diary has been cleared!")
                  
        # Read all content
        elif user_selection == '3':
            with open(file_name, 'r') as file:
                print("\nDiary content:\n", file.read())
                      
        #Exit
        elif user_selection == '4':
            print("Exit the menu!")
            break
             
        else:
            print("Invalid choice, try again")


if __name__ == "__main__":
    main()