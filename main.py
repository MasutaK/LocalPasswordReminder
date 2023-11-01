import tkinter
import tkinter.messagebox
import customtkinter

# Variables
WIDTH = 1100
HEIGHT = 580
SCREEN_SIZE = f"{WIDTH}x{HEIGHT}"
APP_TITLE = "Local Password Reminder"
ADD_TITLE = "Add"
LIST_TITLE = "List"
MANAGE_TITLE = "Manage"

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
      self.label_presentation = customtkinter.CTkLabel(self.sidebar_frame, text="Created by Masuta", font=customtkinter.CTkFont(size=15))
      self.label_presentation.grid(row=1)

      # create tabview
      self.tabview = customtkinter.CTkTabview(self, width=HEIGHT*1.3)
      self.tabview.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
      self.tabview.add(ADD_TITLE)
      self.tabview.add(LIST_TITLE)
      self.tabview.add(MANAGE_TITLE)
      self.tabview.tab(ADD_TITLE).grid_columnconfigure(0, weight=1)
      self.tabview.tab(LIST_TITLE).grid_columnconfigure(0, weight=1)

      # set default values
      self.appearance_mode_optionemenu.set("System")

   def change_appearance_mode_event(self, new_appearance_mode: str):
      customtkinter.set_appearance_mode(new_appearance_mode)

   def add_password(self):
      print("Add password")

   def list_password(self):
      print("List password")

if __name__ == "__main__":
    app = App()
    app.mainloop()