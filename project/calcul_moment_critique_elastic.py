import customtkinter
from back_data_constantes import *
from back_functions import *
from verif_ames_poutres_voilement import my_screen as ames_poutres_voilement

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def my_screen():
    root = customtkinter.CTk()
    root.geometry("700x570")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    def calculer():
        try:
            choix_cas_entry_value = choix_cas_entry.get()
            c1_entry_value = float(c1_entry.get())
            c2_entry_value = float(c2_entry.get())
            c3_entry_value = float(c3_entry.get())
            l_entry_value = float(l_entry.get())
            k_entry_value = float(k_entry.get())
            kw_entry_value = float(kw_entry.get())
            zy_entry_value = float(zy_entry.get())
            zj_entry_value = float(zj_entry.get())
            zg_entry_value = float(zg_entry.get())
            
            Iy = float(get_resultat_calcul('Iy')[1])
            Iw = float(get_resultat_calcul('Iw')[1])
            g = float(get_resultat_calcul('G')[1])
            Iw = float(get_resultat_calcul('Iw')[1])
            It = float(get_resultat_calcul('It')[1])
            
            
            if choix_cas_entry_value == "Poutre à section transversale constante":
                cas = 'Cas1'
            else:
                cas = 'Cas1'
            
            Mcr = float(calcul_Mcr(cas, c1_entry_value, c2_entry_value, c3_entry_value, Iy, k_entry_value, l_entry_value, kw_entry_value, Iw, g, E, It, zy_entry_value, zj_entry_value, zg_entry_value))
            
            Mcr_result = ("Mcr", round(Mcr, 2))
            add_data_to_db_resultat_calcul(resultat=Mcr_result)
            
            root.destroy()
            ames_poutres_voilement()
            
        except Exception as e:
            error.configure(text=e, text_color='red')
                
    frame1 = customtkinter.CTkFrame(master=root)
    frame1.pack(pady=20, padx=10)
    titre = customtkinter.CTkLabel(master=frame1, text="CALCUL DE MOMENT CRITIQUE ÉLASTIQUE (Mcr)", font=("Roboto", 24, 'bold'))
    titre.pack(pady=12, padx=10)
    
    choix = [
        "Poutre à section transversale constante",
        "Poutre à section transversale constante et doublement symétrique"
    ]
    
    choix_cas_entry = customtkinter.CTkOptionMenu(master=frame1, values=choix, font=("Roboto", 16), width=550, height=30)
    choix_cas_entry.pack(pady=5, padx=10)
    
    c1_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de C1", font=("Roboto", 16), width=550, height=30)
    c1_entry.pack(pady=5, padx=10)
    
    c2_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de C2", font=("Roboto", 16), width=550, height=30)
    c2_entry.pack(pady=5, padx=10)
    
    c3_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de C3", font=("Roboto", 16), width=550, height=30)
    c3_entry.pack(pady=5, padx=10)
    
    k_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de K", font=("Roboto", 16), width=550, height=30)
    k_entry.pack(pady=5, padx=10)
    
    l_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de L", font=("Roboto", 16), width=550, height=30)
    l_entry.pack(pady=5, padx=10)
    
    kw_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de Kw", font=("Roboto", 16), width=550, height=30)
    kw_entry.pack(pady=5, padx=10)
    
    zy_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de Zy", font=("Roboto", 16), width=550, height=30)
    zy_entry.pack(pady=5, padx=10)
    
    zj_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de Zj", font=("Roboto", 16), width=550, height=30)
    zj_entry.pack(pady=5, padx=10)
    
    zg_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de Zg", font=("Roboto", 16), width=550, height=30)
    zg_entry.pack(pady=5, padx=10)

    button = customtkinter.CTkButton(master=frame1, text="CALCULER", width=300, height=30, font=("Roboto", 16, 'bold'), command=calculer)
    button.pack(pady=10, padx=10)
    
    error = customtkinter.CTkLabel(master=frame1, text="", font=("Roboto", 16,))
    error.pack(pady=2, padx=10)

    root.mainloop()