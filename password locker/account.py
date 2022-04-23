class account:
    accounts_list = [] #hold a list of all accounts created.
    
    def __init__(self,username,password):
        self. username = username
        self.password = password
        
    def add_account(self):
        account.accounts_list.append(self) #adds the new account details to the accounts list