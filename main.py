import tkinter
import tkinter.messagebox
import customtkinter

# const
WIDTH = 1100
HEIGHT = 580
SCREEN_SIZE = f"{WIDTH}x{HEIGHT}"
APP_TITLE = "Local Password Reminder"
ADD_TITLE = "Add"
ADD_PWD_NAME_LABEL = "Name"
ADD_PWD_LOGIN_LABEL = "Login"
ADD_PWD_MAIL_LABEL = "Mail address"
ADD_PWD_LABEL = "Password"
LIST_TITLE = "List"
MANAGE_TITLE = "Manage"
AUTHOR = "Created by Masuta"

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
   def __init__(self):
      super().__init__()

      # configure window
      self.title(APP_TITLE)
      self.geometry(SCREEN_SIZE)
      self.resizable(False, False)

      # configure grid layout
      self.grid_columnconfigure(0, weight=1)
      self.grid_rowconfigure((0, 1), weight=1)

      # create sidebar frame with widgets
      self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
      self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
      self.sidebar_frame.grid_rowconfigure(4, weight=1)
      self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text=APP_TITLE, font=customtkinter.CTkFont(size=20, weight="bold"))
      self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 20))
      self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
      self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
      self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
      self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
      self.label_author = customtkinter.CTkLabel(self.sidebar_frame, text=AUTHOR, font=customtkinter.CTkFont(size=15))
      self.label_author.grid(row=1)

      # create tabview
      self.tabview = customtkinter.CTkTabview(self, width=HEIGHT*1.3)
      self.tabview.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
      self.tabview.add(ADD_TITLE)
      self.tabview.add(LIST_TITLE)
      self.tabview.add(MANAGE_TITLE)
      self.tabview.tab(ADD_TITLE).grid_columnconfigure((0, 3), weight=1)
      self.tabview.tab(LIST_TITLE).grid_columnconfigure(0, weight=1)

      # handle tab to add password
      self.label_name = customtkinter.CTkLabel(self.tabview.tab(ADD_TITLE), text=ADD_PWD_NAME_LABEL, font=customtkinter.CTkFont(size=15))
      self.label_name.grid(row=0, column=0, pady=20)
      self.textbox_name = customtkinter.CTkEntry(self.tabview.tab(ADD_TITLE), width=WIDTH/3, height=1)
      self.textbox_name.grid(row=0, column=1)
      self.label_login = customtkinter.CTkLabel(self.tabview.tab(ADD_TITLE), text=ADD_PWD_LOGIN_LABEL, font=customtkinter.CTkFont(size=15))
      self.label_login.grid(row=1, column=0, pady=20)
      self.textbox_login = customtkinter.CTkEntry(self.tabview.tab(ADD_TITLE), width=WIDTH/3, height=1)
      self.textbox_login.grid(row=1, column=1)
      self.label_email = customtkinter.CTkLabel(self.tabview.tab(ADD_TITLE), text=ADD_PWD_MAIL_LABEL, font=customtkinter.CTkFont(size=15))
      self.label_email.grid(row=2, column=0, pady=20)
      self.textbox_email = customtkinter.CTkEntry(self.tabview.tab(ADD_TITLE), width=WIDTH/3, height=1)
      self.textbox_email.grid(row=2, column=1)
      self.label_password = customtkinter.CTkLabel(self.tabview.tab(ADD_TITLE), text=ADD_PWD_LABEL, font=customtkinter.CTkFont(size=15))
      self.label_password.grid(row=3, column=0, pady=20)
      self.textbox_pwd = customtkinter.CTkEntry(self.tabview.tab(ADD_TITLE), width=WIDTH/3, height=1, show="*")
      self.textbox_pwd.grid(row=3, column=1)
      self.button_add_pwd = customtkinter.CTkButton(self.tabview.tab(ADD_TITLE), text=ADD_TITLE + " " + ADD_PWD_LABEL, command=self.button_event_add_password)
      self.button_add_pwd.grid(row=4, column=0, pady=20)

      # set default values
      self.appearance_mode_optionemenu.set("System")

   def change_appearance_mode_event(self, new_appearance_mode: str):
      customtkinter.set_appearance_mode(new_appearance_mode)

   def button_event_add_password(self):
      name = self.textbox_name.get()
      login = self.textbox_login.get()
      mail = self.textbox_email.get()
      pwd = self.textbox_pwd.get()

if __name__ == "__main__":
    app = App()
    app.mainloop()