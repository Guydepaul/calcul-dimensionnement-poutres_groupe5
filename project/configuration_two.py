import customtkinter
from CTkScrollableDropdown import *
from back_data_constantes import *
from calcul_classe_section import my_screen as classe_section

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def my_screen(liste_profiles: list):
    root = customtkinter.CTk()
    root.geometry("700x350")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    def continuer_config():
        choix_materiaux_entry_value = choix_materiaux_entry.get()
        profilee = ('Profilé', choix_materiaux_entry_value)
        if choix_materiaux_entry_value != "CTkOptionMenu":
            add_data_to_db_resultat_calcul(profilee)

            root.destroy()
            classe_section()
            
        error.configure(text="Veuillez selectionner une valeur", text_color='red')

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    titre = customtkinter.CTkLabel(master=frame, text="CHOIX DES MATÉRIAUX", font=("Roboto", 24, 'bold'))
    titre.pack(pady=12, padx=10)

    choix_materiaux_label = customtkinter.CTkLabel(master=frame, text="Choisir le type de profilé", font=("Roboto", 16, 'bold'))
    choix_materiaux_label.pack(padx=10)
    choix_materiaux_entry = customtkinter.CTkOptionMenu(master=frame, font=("Roboto", 16), width=300, height=30)
    choix_materiaux_entry.pack(pady=12, padx=10)

    CTkScrollableDropdown(choix_materiaux_entry, values=liste_profiles, justify="left", button_color="transparent")

    error = customtkinter.CTkLabel(master=frame, text="", font=("Roboto", 16,))
    error.pack(pady=2, padx=10)

    button = customtkinter.CTkButton(master=frame, text="CONTINUER", width=300, height=30, font=("Roboto", 16, 'bold'), command=continuer_config)
    button.pack(pady=12, padx=10)

    root.mainloop()