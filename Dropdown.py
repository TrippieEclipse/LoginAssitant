from colorama import Fore
from tkinter import ttk
import tkinter as tk

import LoginHandle
import JsonHandler

selected_account = None


class UGUI:
    
    def __init__(self,master,accounts) -> None:
        
        self.main_window = master
        self.main_window.config(width=600, height=500)
        self.main_window.title("Combobox")

        self.accounts = accounts
        

    

    def display_selection(self):
        # Get the selected value.
        selection = self.combo.get()
        self.selectedAccount = None
        for x in self.accounts:
            if x == selection:
                self.selectedAccount = self.accounts[x]
                
        if self.selectedAccount == None : 
            return
    
        global selected_account
        selected_account = self.selectedAccount


        self.main_window.destroy()


    
    def GetNames(self):
        self.nameList = []
        print(f"{Fore.CYAN} Accounts - Stage 3 - ",self.accounts, f"{Fore.WHITE}")
        for x in self.accounts:
            self.nameList.append(x)
        print(self.nameList)

    def FillWindow(self):
        self.combo = ttk.Combobox(
            state="readonly",
            values=self.nameList
        )
        self.combo.place(x=50, y=50)
        button = ttk.Button(text="Load Website", command=self.display_selection)
        button.place(x=50, y=100)
        quit_button = tk.Button(text = 'Add Account', width = 25, command = self.AddAcount)
        quit_button.place(x=50,y=150)


    def AddAcount(self):
        self.newWindow = tk.Toplevel(self.main_window)
        self.app = AddAccountWindow(self.newWindow,self.accounts)
        #self.app.FillWindow()



class AddAccountWindow:
    def __init__(self,master,accounts) -> None:

        
        self.accounts = accounts
        self.main_window = master
        self.main_window.geometry("500x500")
        self.frame = tk.Frame(self.main_window)



        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.insert(0,"Account Name")
        self.name_entry.place(x=50,y=50)
        self.name_entry.pack()

        self.url_entry = ttk.Entry(self.frame)
        self.url_entry.insert(0,"URL")
        self.url_entry.place(x=50,y=60)
        self.url_entry.pack()

        self.username_entry = ttk.Entry(self.frame)
        self.username_entry.insert(0,"Username")
        self.username_entry.place(x=50,y=70)
        self.username_entry.pack()

        self.password_entry = ttk.Entry(self.frame)
        self.password_entry.insert(0,"Password")
        self.password_entry.place(x=50,y=80)
        self.password_entry.pack()

        self.auto_login_bool = True
        self.click_login_toggle = tk.Button(self.frame,text="Auto Login - True", width=12, relief="sunken", command=self.Toggle)
        self.click_login_toggle.place(x=50,y=90)
        self.click_login_toggle.pack()

        self.UsernameContainerXPath_entry = ttk.Entry(self.frame)
        self.UsernameContainerXPath_entry.insert(0,"Username Xpath ID")
        self.UsernameContainerXPath_entry.place(x=50,y=100)
        self.UsernameContainerXPath_entry.pack()

        self.UsernameTextXPath_entry = ttk.Entry(self.frame)
        self.UsernameTextXPath_entry.insert(0,"Username Xpath Text")
        self.UsernameTextXPath_entry.place(x=50,y=110)
        self.UsernameTextXPath_entry.pack()

        self.PasswordContainerXPath_entry = ttk.Entry(self.frame)
        self.PasswordContainerXPath_entry.insert(0,"Password Xpath ID")
        self.PasswordContainerXPath_entry.place(x=50,y=120)
        self.PasswordContainerXPath_entry.pack()

        self.PasswordTextXPath_entry = ttk.Entry(self.frame)
        self.PasswordTextXPath_entry.insert(0,"Password Xpath Text")
        self.PasswordTextXPath_entry.place(x=50,y=130)
        self.PasswordTextXPath_entry.pack()


        self.quitButton = tk.Button(self.frame, text = 'Save', width = 25, command = self.save_check)
        self.quitButton.pack()                

        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()


        self.frame.pack()
        
    def Toggle(self):
        if self.auto_login_bool == True :
            self.auto_login_bool = False
            self.click_login_toggle["text"] = "Auto Login - " + str(self.auto_login_bool)
            self.click_login_toggle.pack()
        else:
            self.auto_login_bool = True
            self.click_login_toggle["text"] = "Auto Login - " + str(self.auto_login_bool)
            self.click_login_toggle.pack()


    def FillWindow(self):
        print()



        

    def save_check(self):
        if(self.All_Fields_Filled()):
            self.save_account_info()
        else:
            self.error_label = tk.Label(self.frame,text="MAKE SURE ALL FIELDS ARE FILLED IN BEFORE SAVING",fg="red")
            self.error_label.pack()
        

    def save_account_info(self):
        
        self.jsonHandlerClass = JsonHandler.JsonHandlerClass()
        self.loginInfo = JsonHandler.accountInfoSingle.copy()
        self.name = str(self.name_entry.get())
        self.loginInfo["URL"] = str(self.url_entry.get())
        self.loginInfo["Username"] = str(self.username_entry.get())
        self.loginInfo["Password"] = str(self.password_entry.get())
        self.loginInfo["ClickLogin"] = self.auto_login_bool
        self.loginInfo["UsernameContainerXPath"] = str(self.UsernameContainerXPath_entry.get())
        self.loginInfo["UsernameTextXPath"] = str(self.UsernameTextXPath_entry.get())
        self.loginInfo["PasswordContainerXPath"] = str(self.PasswordContainerXPath_entry.get())
        self.loginInfo["PasswordTextXPath"] = str(self.PasswordTextXPath_entry.get())
        self.accounts[self.name] = self.loginInfo
        self.jsonHandlerClass.SaveTo(self.accounts)
        
        

    def All_Fields_Filled(self):
        text = self.name_entry.get()
        if(text == "Account Name"):
            return False
        
        text = self.url_entry.get()
        if(text == "URL"):
            return False
        
        text = self.username_entry.get()
        if(text == "Username"):
            return False
        
        text = self.password_entry.get()
        if(text == "Password"):
            return False
        
        text = self.UsernameContainerXPath_entry.get()
        if(text == "Username Xpath ID"):
            return False
        
        text = self.UsernameTextXPath_entry.get()
        if(text == "Username Xpath Text"):
            return False
        
        text = self.PasswordContainerXPath_entry.get()
        if(text == "Password Xpath ID"):
            return False
        
        text = self.PasswordTextXPath_entry.get()
        if(text == "Password Xpath Text"):
            return False
        
        return True
        


        

    
    def close_windows(self):
        self.main_window.destroy()


def Main(accounts):
    root = tk.Tk()
    loginHandler = LoginHandle
    mainWindow = UGUI(root,accounts)
    mainWindow.GetNames()
    mainWindow.FillWindow()
    while(True):
        root.mainloop()
        if(selected_account != None):
            break
    
    loginHandler.Activate(selected_account)

    