import json
from colorama import Fore

## Default Account Info ##
accountInfoSingle = {
    "URL" : "",
    "Username" : "",
    "Password" : "",
    "ClickLogin" : False,
    "UsernameContainerXPath" : "",
    "UsernameTextXPath" : "",
    "PasswordContainerXPath" : "",
    "PasswordTextXPath" : ""
}

class JsonHandlerClass():
    mainClassInstance = None  

    def __init__(self) -> None:
        pass
    
    
    def SaveTo(self,accountInfoToSave):
        print("SaveTo Start") # Start check 
        print(accountInfoToSave) # Check account info has loaded
        with open("Accounts.json", mode="w", encoding="utf-8") as write_file:  # Open Accounts Json ready to save to
            json.dump(accountInfoToSave, write_file) # Save accounts info to Json
    
    def LoadFrom(self):
        with open("Accounts.json", mode="r", encoding="utf-8") as read_file:  # Open Accounts Json ready to read from
            accountJson = json.load(read_file)  # Json accounts data in Json format 
            for account, obj in accountJson.items():
                newAccount = accountInfoSingle.copy() # Copy default account template 
                for y in obj:
                    newAccount[y] = obj[y] # Copy account from Json data and convet to python format 

                self.mainClassInstance.accountsTransfer[account] = newAccount # Transfer converted info to MainClass

            print(f"{Fore.RED}Accounts - Stage 2 - ",self.mainClassInstance.accountsTransfer,f"{Fore.WHITE}") # Stage 2 Debug check 
        self.mainClassInstance.TransferAccountsFromjson() # Start MainClass Def to fully transfer account details 
        


