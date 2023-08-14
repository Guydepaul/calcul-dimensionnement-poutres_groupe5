import customtkinter
from back_data_constantes import *
from back_functions import GetDataExcelFile
from configuration_two import my_screen as config_two

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def config_one():
    root = customtkinter.CTk()
    root.geometry("700x350")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    def continuer_config():
        choix_materiaux_entry_value = choix_materiaux_entry.get()
        choix_profile_entry_value = choix_profile_entry.get()
        
        profilee = ('Type de section profilé', choix_profile_entry_value)
        acier = ('Type acier', choix_materiaux_entry_value)
        add_data_to_db_resultat_calcul(profilee)
        add_data_to_db_resultat_calcul(acier)
        
        getter_data_excel = GetDataExcelFile()
        data_progile = getter_data_excel.getDataProfilee(choix_profile_entry_value)
        profiles = []
        for profile in data_progile[1:]:
            profiles.append(profile[0])
        root.destroy()
        config_two(profiles)
        
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=40, padx=60, fill="both", expand=True)

    titre = customtkinter.CTkLabel(master=frame, text="CHOIX DES MATÉRIAUX", font=("Roboto", 24, 'bold'))
    titre.pack(pady=20, padx=10)

    choix_materiaux_label = customtkinter.CTkLabel(master=frame, text="Choisir les matériaux", font=("Roboto", 16, 'bold'))
    choix_materiaux_label.pack(padx=10)
    choix_materiaux_entry = customtkinter.CTkOptionMenu(master=frame, values=TYPE_ACIER, font=("Roboto", 16), width=400, height=30)
    choix_materiaux_entry.pack(padx=10)
    
    choix_profile_label = customtkinter.CTkLabel(master=frame, text="Choisir le profilé", font=("Roboto", 16, 'bold'))
    choix_profile_label.pack(padx=10)
    choix_profile_entry = customtkinter.CTkOptionMenu(master=frame, values=TYPE_PROFILE, font=("Roboto", 16), width=400, height=30)
    choix_profile_entry.pack(padx=10)

    button = customtkinter.CTkButton(master=frame, text="CONTINUER", width=400, height=30, font=("Roboto", 16, 'bold'), command=continuer_config)
    button.pack(pady=12, padx=10)

    root.mainloop()