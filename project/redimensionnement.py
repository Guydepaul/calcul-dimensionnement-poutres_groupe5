# Ici nous aurons nos interfaces graphiques
import customtkinter
# from configuration_one import *
import configuration_one as config_one_module
from resultats import my_screen as resultats_dim
from back_data_constantes import delete_partial_data

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def my_screen():
    root = customtkinter.CTk()
    root.geometry("800x350")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")
    
    def redimensionner():
        root.destroy()
        delete_partial_data()
        config_one_module.config_one()
        
    def voir_resultats():
        resultats_dim()

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    customtkinter.CTkLabel(master=frame, 
                                    text="CALCUL ET DIMENSIONNEMENT DES POUTRES", 
                                    font=("Roboto", 24, 'bold')
                                ).pack(pady=50, padx=10)

    customtkinter.CTkLabel(master=frame, 
                                    text="La condition précedente n'as pas été vérifiée", 
                                    font=("Roboto", 20, 'bold')
                                ).pack(pady=12, padx=10)

    frame_button = customtkinter.CTkFrame(master=root)
    frame_button.pack(pady=12, padx=10)

    continuer = customtkinter.CTkButton(master=frame_button, text="VOIR RESULTATS", font=("Roboto", 16, 'bold'), width=300, height=30, fg_color="gray", command=voir_resultats)
    continuer.grid(row=0, column=0, padx=20, pady=10)

    continuer = customtkinter.CTkButton(master=frame_button, text="REDIMENSIONNER", font=("Roboto", 16, 'bold'), width=300, height=30, command=redimensionner)
    continuer.grid(row=0, column=1, padx=20, pady=10)

    root.mainloop()