from venv import create
from account import account

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

        break


if __name__ == "__main__":
    main()