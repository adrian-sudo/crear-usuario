from forms.registration.form_designer import FormRegisterDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Auth_User
from tkinter import messagebox
import util.encoding_decoding as end_dec
import tkinter as tk

class FormRegister(FormRegisterDesigner):   
        def __init__(self):
                self.auth_user_repository = AuthUserRepository()
                super().__init__()
                
        def register(self):
            if(self.isConfirmationPassword()):
                user = Auth_User()
                user.username = self.username.get()
                user_db: Auth_User = self.auth_repository.getUserByUsername(self.usuario.get())
                if not (self.isUserRegister(user_db)):
                        user.password = end_dec.encode(self.password.get())
                        self.auth_user_repository.save(user)
                        messagebox.showinfo("Registro", "Usuario registrado")
                        self.ventana.destroy()
                        
        def isConfirmationPassword(self):
                status : bool = True
                if(self.password.get() == self.confirmation.get()):
                        status = False
                        messagebox.showerror("Error", "La contraseña no coincide")
                        self.password.delete(0, tk.END)
                        self.confirmation.delete(0, tk.END)
                return status
        
        def isRegister(self, user: Auth_User):
                status : bool = False
                if(user != None):
                        status = False
                        messagebox.showerror("Error", "El usuario ya existe")
                        self.username.delete(0, tk.END)
                return status