import customtkinter
from back_data_constantes import *
from back_functions import *
from verif_stabilite_deversement_poutres import my_screen as stabilite_deversement
from redimensionnement import my_screen as redimmension

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def my_screen():
    root = customtkinter.CTk()
    root.geometry("600x500")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    def continuer_config():
        try:
            choix_cas_entry_value = choix_cas_entry.get()
            p_entry_value = float(p_entry.get())
            grand_l_entry_value = float(grand_l_entry.get())
            l_entry_value = float(l_entry.get())
            
            Iy_val = float(get_resultat_calcul('Iy')[1])
            Iz_val = float(get_resultat_calcul('Iz')[1])
            G_val = float(get_resultat_calcul('G')[1])
            
            cond_state = None
            
            if choix_cas_entry_value == "Sur charge d'exploitation":
                cas = 'CEXP'
                f = float(calcul_f(cas, p_entry_value, grand_l_entry_value, Iy_val))
                f = round(f, 2)
                if f <= l_entry_value / 200:
                    cond_state = "Condition vérifiée"
                else:
                    root.destroy()
                    redimmension()
            else:
                cas = 'PP'
                f = float(calcul_f(cas, p_entry_value, grand_l_entry_value, Iz=Iz_val, G=G_val))
                f = round(f, 2)
                if f <= l_entry_value / 200:
                    cond_state = "Condition vérifiée"
                else:
                    root.destroy()
                    redimmension()
                    
            f = ("f", f)
            cond_verif_result = ("Rigidité des poutres", cond_state)

            add_data_to_db_resultat_calcul(resultat=f)
            add_data_to_db_resultat_verification(resultat=cond_verif_result)
            
            root.destroy()
            stabilite_deversement()
        except Exception as e:
            error.configure(text=e, text_color='red')
        
                        
    frame1 = customtkinter.CTkFrame(master=root)
    frame1.pack(pady=60, padx=10)
    titre = customtkinter.CTkLabel(master=frame1, text="VERIFICATION DE LA RIGIDITÉ DES POUTRES", font=("Roboto", 24, 'bold'))
    titre.pack(pady=12, padx=10)
    
    choix = [
        "Sur charge d'exploitation",
        "Sur son poids propre"
    ]
    
    choix_cas_label = customtkinter.CTkLabel(master=frame1, text="Choisir le cas", font=("Roboto", 16, 'bold'))
    choix_cas_label.pack(padx=10)
    choix_cas_entry = customtkinter.CTkOptionMenu(master=frame1, values=choix, font=("Roboto", 16), width=400, height=30)
    choix_cas_entry.pack(padx=10)
    
    p_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de P", font=("Roboto", 16), width=400, height=30)
    p_entry.pack(pady=12, padx=10)
    
    grand_l_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur du grand L", font=("Roboto", 16), width=400, height=30)
    grand_l_entry.pack(pady=12, padx=10)
    
    l_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur du petit l", font=("Roboto", 16), width=400, height=30)
    l_entry.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame1, text="VERIFIER", width=300, height=30, font=("Roboto", 16, 'bold'), command=continuer_config)
    button.pack(pady=12, padx=10)
    
    error = customtkinter.CTkLabel(master=frame1, text="", font=("Roboto", 16,))
    error.pack(pady=2, padx=10)

    root.mainloop()
    
# my_screen()