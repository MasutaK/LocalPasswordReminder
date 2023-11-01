import customtkinter

# Variables
SCREEN_SIZE = "500x350"

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry(SCREEN_SIZE)
root.title("Local Password Reminder")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Hello World")
label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

root.mainloop()