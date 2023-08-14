import customtkinter
from back_functions import *
from back_data_constantes import *
from verif_cisaillement import my_screen as cisaillement_verif
from redimensionnement import my_screen as redimmention

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def my_screen():
    root = customtkinter.CTk()
    root.geometry("750x450")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    def continuer_config():
        try:
            longueur_poutre_entry_value = longueur_poutre_entry.get()
            module_resistance_entry_value = module_resistance_entry.get()

            longueur_poutre_val = float(longueur_poutre_entry_value)
            module_val = float(module_resistance_entry_value)

            G_val = float(get_resultat_calcul('G')[1])
            Q_val = float(get_resultat_calcul('Q')[1])
            classe_section = get_resultat_calcul('Classe section')[1]
            fy = float(get_resultat_calcul('Fy')[1])

            q = float(calcul_q(G_val, Q_val))
            Msd = round(calcul_Msd(q, longueur_poutre_val), 2)
            Vsd = round(calcul_Vsd(q, longueur_poutre_val), 2)

            # Calcul moment resistant
            if classe_section in ['Classe 1', 'Classe 2', 'Classe 3']:
                Mr = round(calcul_Mr(module_val, fy, 1), 2)
            else:
                Mr = round(calcul_Mr(module_val, fy, 4), 2)

            if classe_section in ['Classe 1', 'Classe 2', 'Classe 3']:
                if Mr >= Msd:
                    cond_state = 'Condition vérifiée'
                else:
                    root.destroy()
                    redimmention()
            else:
                if Mr == Msd:
                    cond_state = 'Condition vérifiée'
                else:
                    root.destroy()
                    redimmention()
                
            # Storage
            save_B = ('B', longueur_poutre_val)
            save_W = ('W', module_val)
            save_q = ('q', q)
            save_Msd = ('Msd', Msd)
            save_Vsd = ('Vsd', Vsd)
            save_Mr = ('Mr', Mr)
            
            verif_state = ("Resistance poutre (Absence de l'effort tranchant)", cond_state)
            
            add_data_to_db_resultat_calcul(resultat=save_B)
            add_data_to_db_resultat_calcul(resultat=save_W)
            add_data_to_db_resultat_calcul(resultat=save_q)
            add_data_to_db_resultat_calcul(resultat=save_Msd)
            add_data_to_db_resultat_calcul(resultat=save_Vsd)
            add_data_to_db_resultat_calcul(resultat=save_Mr)
            
            add_data_to_db_resultat_verification(resultat=verif_state)
            
            root.destroy()
            cisaillement_verif()
        except Exception as e:
            error.configure(text=e, text_color='red')
        
        
    frame1 = customtkinter.CTkFrame(master=root)
    frame1.pack(pady=20, padx=60)
    titre = customtkinter.CTkLabel(master=frame1, text="VERIFICATION DE LA RESISTANCE DES POUTRES", font=("Roboto", 24, 'bold'))
    titre.pack(pady=12, padx=10)

    frame2 = customtkinter.CTkFrame(master=root)
    frame2.pack(pady=0, padx=0)
    titre2 = customtkinter.CTkLabel(master=frame2, text="Calcul Moment et effort tranchant", font=("Roboto", 24, 'bold'))
    titre2.pack(pady=12, padx=10)
    longueur_poutre_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="La longueur du poutre", font=("Roboto", 16), width=400, height=30)
    longueur_poutre_entry.pack(pady=12, padx=10)

    frame3 = customtkinter.CTkFrame(master=root)
    frame3.pack(pady=10, padx=0)
    titre2 = customtkinter.CTkLabel(master=frame3, text="Calcul du moment resistant", font=("Roboto", 24, 'bold'))
    titre2.pack(pady=12, padx=10)
    module_resistance_entry = customtkinter.CTkEntry(master=frame3, placeholder_text="Module de résistance (Wpl, Wel, Weff)", font=("Roboto", 16), width=400, height=30)
    module_resistance_entry.pack(pady=12, padx=10)
    
    error = customtkinter.CTkLabel(master=root, text="", font=("Roboto", 16,))
    error.pack(pady=2, padx=10)

    frame5 = customtkinter.CTkFrame(master=root)
    frame5.pack(pady=10, padx=60)
    button = customtkinter.CTkButton(master=frame5, text="VERIFIER", width=300, height=30, font=("Roboto", 16, 'bold'), command=continuer_config)
    button.pack(pady=5, padx=10)
    

    root.mainloop()