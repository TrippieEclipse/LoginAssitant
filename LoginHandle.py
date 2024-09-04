from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from colorama import Fore
from os import system

class LoginTest:

    def SetUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def LoginToSiteWithAccount(self,account):
        system("clear")
        url = str(account["URL"])
        username = str(account["Username"])
        password = str(account["Password"])
        clickLogin = account["ClickLogin"]

        containID = str(account["UsernameContainerXPath"])
        textID = str(account["UsernameTextXPath"])
        usernameXpath = f"//input[contains(@{containID}, '{textID}')]"

        containID = str(account["PasswordContainerXPath"])
        textID = str(account["PasswordTextXPath"])
        passwordXpath = f"//input[contains(@{containID}, '{textID}')]"

        self.driver.get(url)
        print(f"{Fore.LIGHTBLUE_EX} UsernameXpath",usernameXpath)

        self.usernameElem = self.driver.find_element(By.XPATH, usernameXpath)
        self.usernameElem.clear()
        self.usernameElem.send_keys(username)
        
        self.passwordElem = self.driver.find_element(By.XPATH, passwordXpath)
        self.usernameElem.clear()
        self.usernameElem.send_keys(username)
        self.passwordElem.send_keys(password)
        
        if(clickLogin):
            self.loginButton = self.driver.find_element(By.ID, "submit")
            self.loginButton.click()
        while(True):
            pass
        

    def TearDown(self):
        self.driver.close()


main_instance = LoginTest()


def Activate(selected_account):
    main_instance.SetUp()
    main_instance.LoginToSiteWithAccount(selected_account)


print(f"{Fore.YELLOW} INACTIVE {Fore.WHITE}")