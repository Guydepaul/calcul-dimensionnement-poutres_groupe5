import customtkinter
from back_data_constantes import *
from configuration_one import *
from back_functions import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def my_screen():
    root = customtkinter.CTk()
    root.geometry("700x350")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    def calculer():
        try:
            f_sur_l_value = f_sur_l.get()
            fSurl = 1/150 if f_sur_l_value == '1/150' else 1/300        

            e1 = float(get_resultat_calcul('E1')[1])
            t = float(get_resultat_calcul('t')[1])
            
            h = round(calcul_H(fSurl, e1, t), 2)
            
            pn_result = ('H', h)
            add_data_to_db_resultat_calcul(resultat=pn_result)
            
            root.destroy()
            config_one()

        except Exception as e:
            error.configure(text=e, text_color='red')

                    

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    titre = customtkinter.CTkLabel(master=frame, text="CALCUL DE LA FORCE DE POUSSÉE LATÉRALE", font=("Roboto", 24, 'bold'))
    titre.pack(pady=20, padx=10)

    f_sur_l_label = customtkinter.CTkLabel(master=frame, text="Selectionner la valeur de f/L", font=("Roboto", 16, 'bold'))
    f_sur_l_label.pack(pady=20, padx=10)
    f_sur_l = customtkinter.CTkOptionMenu(master=frame, values=['1/150', '1/300'], font=("Roboto", 18,), width=300, height=30)
    f_sur_l.pack()

    button = customtkinter.CTkButton(master=frame, text="CALCULER", width=300, height=30, font=("Roboto", 16, 'bold'), command=calculer)
    button.pack(pady=20, padx=10)

    error = customtkinter.CTkLabel(master=frame, text="", font=("Roboto", 16,))
    error.pack(pady=12, padx=10)

    root.mainloop()