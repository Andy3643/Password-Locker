from venv import create
from account import account

def main():
    while True:
        print("Welcome to Password Locker")
        print("\n")
        print("Choose short code to continue ;\nTo create an account, use create \nTo login to your account use login \nTo exit, type ex")
        short_code = input().lower()

        if short_code == "create":
            print("Add Username")
        

        break


if __name__ == "__main__":
    main()