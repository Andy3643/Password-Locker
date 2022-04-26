from venv import create
from account import account
from credentials import credentials

def main():
    while True:
        print("Welcome to Password Locker")
        print("\n")
        print("Choose short code to continue ;\nTo create an account, use create \nTo login to your account use login \nTo exit, type ex")
        short_code = input().lower()
        print("\n")

        if short_code == "create":
            print("Add Username")
            new_username = input()

            print ("create a password")
            new_password = input()

            print ("confirm your password")
            confirmed_password = input()
            
            while confirmed_password != new_password :
                print ("Password do not match! Try again")
                new_password = input()
                print ("confirm your password")
                confirmed_password = input()
            else:
                print("Your account has been succesfully created \nProceed to login.")
                print("\n")
                print("Enter username")
                entered_username = input()
                print ("Enter your password")
                entered_passsword = input()

            while entered_username != new_username  or entered_passsword != new_password:
                print("Invalid username or password!Try again")
                print("Enter username")
                entered_username = input()
                print ("Enter your password")
                entered_passsword = input()
            else:
                print (f"{entered_username} welcome to your account")
                print("\n")
                #Add code to save user password here
        
        elif short_code == "login":
            print("Enter username")
            saved_username = input()
            #testcode for login...replce with accountlist loop
            while saved_username != "andy":
                print("Username does not exist. Create an account first")
                break

            else:
                print("Enter Password")
                saved_password = input()

                while saved_password != "1234":
                    print("""Wrong Password!
                    Please try again""")
                    saved_password = input()

                else:
                    print("Congratulations! You have succesfully logged in")
                    print ("""You can now save your passwords here.
                    to create add a username and password use the code save""")

                #save password
                    if short_code == 'save':
                            print("Add username")
                            username_to_save = input()
                            print ("Print password")
                            password_to_save = input()

                            # save_credentials(create_credentials(username,password))
                            # print ('\n')
                            # print(f"New details for  {username_to_save}created")
                            # print ('\n')


                    
        elif short_code =="exit":
            break
        else:
            print("Enter a valid shortcode!")


if __name__ == "__main__":
    main()