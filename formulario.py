from tkinter import *
 
def send_data():
  usuario_info = usuario.get()
  contraseña_info = contraseña.get()
  nombre_info = nombre.get()
  edad_info = str(edad.get())
  print(usuario_info,"\t", contraseña_info,"\t", nombre_info,"\t", edad_info)
 
 
  file = open("user.txt", "a")
  file.write(usuario_info)
  file.write("\t")
  file.write(contraseña_info)
  file.write("\t")
  file.write(nombre_info)
  file.write("\t")
  file.write(edad_info)
  file.write("\t\n")
  file.close()
  print(" New user registered. Username: {} | FullName: {}   ".format(usuario_info, nombre_info))
 
  usuario_entry.delete(0, END)
  contraseña_entry.delete(0, END)
  nombre_entry.delete(0, END)
  edad_entry.delete(0, END)

# Create new instance - Class Tk()  
mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("REGISTRO OMIND SEX ")
mywindow.resizable(False,False)
mywindow.config(background = "#ff0055")
main_title = Label(text = "REGISTRO | OMIND SEX", font = ("calibri", 16), bg = "#ff0055", fg = "white", width = "500", height = "2")
main_title.pack()

# Define Label Fields 
usuario_label = Label(text = "Usuario", bg = "#ff0055", fg = "white", font = ("calibri", 14))
usuario_label.place(x = 200, y = 100)
contraseña_label = Label(text = "Contraseña", bg = "#ff0055", fg = "white", font = ("calibri", 14))
contraseña_label.place(x = 200, y = 160)
nombre_label = Label(text = "Nombre completo", bg = "#ff0055", fg = "white",font = ("calibri", 14))
nombre_label.place(x = 200, y = 220)
edad_label = Label(text = "Edad", bg = "#ff0055", fg = "white", font = ("calibri", 14))
edad_label.place(x = 200, y = 280)
 

usuario= StringVar()
contraseña = StringVar()
nombre= StringVar()
edad= StringVar()
 
usuario_entry = Entry(textvariable = usuario, width = "40")
contraseña_entry = Entry(textvariable = contraseña, width = "40",  show = "*")
nombre_entry = Entry(textvariable = nombre, width = "40")
edad_entry = Entry(textvariable = edad, width = "40")
 
usuario_entry.place(x = 200, y = 130)
contraseña_entry.place(x = 200, y = 190)
nombre_entry.place(x = 200, y = 250)
edad_entry.place(x = 200, y = 310)
 

submit_btn = Button(mywindow,text = "Registrarse", width = "30", height = "2", command = send_data, bg = "#1f53c5")
submit_btn.place(x = 210, y = 350)

mywindow.mainloop()