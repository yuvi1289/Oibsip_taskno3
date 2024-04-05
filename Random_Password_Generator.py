import string
import random
import tkinter as tk
import customtkinter
from PIL import ImageTk, Image


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("900x700")
app.title('PasswordGenerator')


pil_image = Image.open('bg.jpg')
img1 = ImageTk.PhotoImage(pil_image)

l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

frame = customtkinter.CTkFrame(master=l1, width=410, height=500, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
l2 = customtkinter.CTkLabel(master=frame, text="Password Generator", font=('Century Gothic', 18))
l2.place(x=110, y=45)

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak", score
    elif score <= 4:
        return "Moderate", score
    else:
        return "Strong", score

def generate_password():
    try:
        length = int(entry1.get())
        num_digits = int(entry2.get())
        num_special_chars = int(entry4.get())
        num_letters = length - num_digits - num_special_chars

        letters = ""
        if uppercase_var.get():
            letters += string.ascii_uppercase
        if lowercase_var.get():
            letters += string.ascii_lowercase

        password = ''.join(random.choices(letters, k=num_letters))
        password += ''.join(random.choices(string.digits, k=num_digits))
        password += ''.join(random.choices(string.punctuation, k=num_special_chars))

        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        entry3.delete(0, tk.END)
        entry3.insert(0, password)

        strength, score = check_password_strength(password)
        strength_label.configure(text=f"Password Strength: {strength} (Score: {score})")
    except ValueError:
        entry3.delete(0, tk.END)
        entry3.insert(0, "Invalid input")



entry1 = customtkinter.CTkEntry(master=frame, width=273, placeholder_text='Enter the length of the password')
entry1.place(x=70, y=110)
entry2 = customtkinter.CTkEntry(master=frame, width=273, placeholder_text='How many digits you want to add')
entry2.place(x=70, y=159)
entry4 = customtkinter.CTkEntry(master=frame, width=273, placeholder_text='How many special characters you want to add')
entry4.place(x=70, y=208)
entry3 = customtkinter.CTkEntry(master=frame, width=180, placeholder_text='Generated Password')
entry3.place(x=120, y=439)

uppercase_var = tk.BooleanVar()
uppercase_checkbox = customtkinter.CTkCheckBox(master=frame, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_checkbox.place(x=70, y=258)

lowercase_var = tk.BooleanVar()
lowercase_checkbox = customtkinter.CTkCheckBox(master=frame, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_checkbox.place(x=70, y=288)

generate_button = customtkinter.CTkButton(master=frame, text="Generate Password", command=generate_password)
generate_button.place(x=140, y=335)

strength_label = customtkinter.CTkLabel(master=frame, text="Password Strength: ", font=('Century Gothic', 12))
strength_label.place(x=120, y=380)

tips_label = customtkinter.CTkLabel(master=frame, text="Tips: Use a mix of uppercase and lowercase letters, digits, and special characters.", font=('Century Gothic', 12), wraplength=350)
tips_label.place(x=50, y=410)


app.mainloop()
