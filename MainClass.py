import JsonHandler
import Dropdown
from colorama import Fore
from os import system

accounts = {}

class main:
    accountsTransfer = {}

    selectedAccount = None

    def __init__(self):
        ### Summary
        ###
        ### initiates the connection to all other scripts needed for this software and tells those scripts  
        ### that this instance is the main instance 
        self.jsonHandlerClass = JsonHandler.JsonHandlerClass()
        self.jsonHandlerClass.__init__()
        self.jsonHandlerClass.mainClassInstance = self
        self.dropDownInstance = Dropdown

    def Start(self):
        print("Start")
        self.jsonHandlerClass.LoadFrom() # Starts JsonHandlers Def to get all accounts info fron Json
        self.dropDownInstance.Main(accounts) # Initiate the main window the user will interact with  


    def TransferAccountsFromjson(self):
        print("Transfer")

        print(self.accountsTransfer)
        
        for account, obj in self.accountsTransfer.items():
            
                newAccount = JsonHandler.accountInfoSingle.copy()
                for y in obj:
                    newAccount[y] = obj[y]

                    #print(f"{Fore.MAGENTA}",obj[y])
                #print(f"{Fore.WHITE}New Account - ", newAccount)
                accounts[account] = newAccount

    def TestSaveInfo(self):

        self.loginTestInfo = JsonHandler.accountInfoSingle.copy()
        self.name = "Login Test 1"
        self.loginTestInfo["URL"] = "https://practicetestautomation.com/practice-test-login/"
        self.loginTestInfo["Username"] = "student"
        self.loginTestInfo["Password"] = "Password123"
        self.loginTestInfo["ClickLogin"] = True
        self.loginTestInfo["UsernameContainerXPath"] = "name"
        self.loginTestInfo["UsernameTextXPath"] = "username"
        self.loginTestInfo["PasswordContainerXPath"] = "name"
        self.loginTestInfo["PasswordTextXPath"] = "password"
        accounts[self.name] = self.loginTestInfo
        self.jsonHandlerClass.SaveTo(accounts)

print("INNIT")

mainInstance = main()
mainInstance.__init__()
#mainInstance.TestSaveInfo()
mainInstance.Start()






