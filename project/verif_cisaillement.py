import customtkinter
from back_data_constantes import *
from back_functions import *
from verif_flexion_deviee import my_screen as flexion_deviee
from redimensionnement import my_screen as redimmention

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def my_screen():
    root = customtkinter.CTk()
    root.geometry("680x550")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    def continuer_config():
        try:
            nombre_appuis_entry_value = float(nombre_appuis_entry.get())
            l_entry_value = float(l_entry.get())
            type_profile_entry_value = type_profile_entry.get()
            axe_moment_value = axe_moment.get()
            
            if type_profile_entry_value == 'Profilé laminés I ou H':
                type_profile = 'I' or 'H'
            elif type_profile_entry_value == 'Profilé laminés [':
                type_profile = '['
            else:
                type_profile = 'Autres'
            
            Q_val = float(get_resultat_calcul('Q')[1])
            G_val = float(get_resultat_calcul('G')[1])
            A_val = float(get_resultat_calcul('A')[1])
            B_val = float(get_resultat_calcul('B')[1])
            tf_val = float(get_resultat_calcul('tf')[1])
            tw_val = float(get_resultat_calcul('tw')[1])
            r_val = float(get_resultat_calcul('r')[1])
            h_val = float(get_resultat_calcul('h')[1])
            h_val = float(get_resultat_calcul('h')[1])
            fy_val = float(get_resultat_calcul('Fy')[1])
            Msd_val = float(get_resultat_calcul('Msd')[1])
            Mr_val = float(get_resultat_calcul('Mr')[1])
            
            Vsd_appuis = float(calcul_Vsd_appuis(Q_val, l_entry_value, nombre_appuis_entry_value, G_val))
            Av = float(calcul_Av(type_profile, A_val, B_val, tf_val, tw_val, r_val, h_val))
            Vplrd = float(calcul_Vplrd(Av, fy_val))
            if Vsd_appuis is not None:
                rau = float(calcul_rau(Vsd_appuis, Vplrd))
            
                dataExcel = GetDataExcelFile()
                section_type = get_resultat_calcul('Type de section profilé')[1]
                section_type_sheet = dataExcel.getDataProfilee(section_type)
                profile = get_resultat_calcul('Profilé')[1]
                
                for section in section_type_sheet[1:]:
                    if profile == section[0]:
                        if axe_moment_value == 'Axe y':
                            Wpl = float(section[15]) * (10**3)
                        else:
                            Wpl = float(section[20]) * (10**3)
                
                Mv_rd = calcul_Mvrd(Wpl, rau, Av, tw_val, fy_val)
                
                if Vsd_appuis <= 0.5 * Vplrd:
                    if Msd_val <= Mr_val:
                        cond_state1 = "Condition vérifiée"
                    else:
                        root.destroy()
                        redimmention()
                else:
                    if Msd_val <= Mv_rd:
                        cond_state1 = "Condition vérifiée"
                    else:
                        root.destroy()
                        redimmention()
                        
                if Vplrd >= Vsd_appuis:
                    cond_state2 = "Condition vérifiée"
                else:
                    root.destroy()
                    redimmention()

                # Sauvegarde
                Vsd_appuis_result = ("Vsd avec appuis", round(Vsd_appuis, 2))
                Av_result = ("Av", round(Av, 2))
                Vplrd_result = ("Vplrd", round(Vplrd, 2))
                Rau_result = ("Rau", round(rau, 2))
                Mv_rd_result = ("Mv_rd", round(Mv_rd, 2))
                cond_verif_result1 = ("Resistance poutre (Au cisaillement)", cond_state1)
                cond_verif_result2 = ("Resistance poutre (En presence de l'effort tranchant et moment flechissant)", cond_state2)

                add_data_to_db_resultat_calcul(resultat=Vsd_appuis_result)
                add_data_to_db_resultat_calcul(resultat=Av_result)
                add_data_to_db_resultat_calcul(resultat=Vplrd_result)
                add_data_to_db_resultat_calcul(resultat=Rau_result)
                add_data_to_db_resultat_calcul(resultat=Mv_rd_result)
                
                add_data_to_db_resultat_verification(resultat=cond_verif_result1)
                add_data_to_db_resultat_verification(resultat=cond_verif_result2)
                
                root.destroy()
                flexion_deviee()
                
            else:
                error.configure(text="Les nombres d'appuis doit etre < 3", text_color='red')
            
        except Exception as e:
            error.configure(text=e, text_color='red')
                
    frame1 = customtkinter.CTkFrame(master=root)
    frame1.pack(pady=20, padx=10)
    titre = customtkinter.CTkLabel(master=frame1, text="VERIFICATION AU CISAILLEMENT ET PRESENCE", font=("Roboto", 24, 'bold'))
    titre.pack(pady=0, padx=10)
    titre = customtkinter.CTkLabel(master=frame1, text="DE L'EFFORT TRANCHANT ET MOMENT FLECHISSANT", font=("Roboto", 24, 'bold'))
    titre.pack(pady=0, padx=10)
        
    frame2 = customtkinter.CTkFrame(master=root)
    frame2.pack(pady=0, padx=0)
    titre2 = customtkinter.CTkLabel(master=frame2, text="Calcul de Vsd", font=("Roboto", 24, 'bold'))
    titre2.pack(pady=12, padx=10)
    nombre_appuis_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Entrer le nombre d'appuis", font=("Roboto", 16), width=400, height=30)
    nombre_appuis_entry.pack(pady=12, padx=10)
    l_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Entrer la valeur de l", font=("Roboto", 16), width=400, height=30)
    l_entry.pack(pady=12, padx=10)
    
    frame3 = customtkinter.CTkFrame(master=root)
    frame3.pack(pady=20, padx=0)
    titre2 = customtkinter.CTkLabel(master=frame3, text="Calcul de l'aire de cisaillement Av", font=("Roboto", 24, 'bold'))
    titre2.pack(pady=12, padx=10)
    type_profile_entry = customtkinter.CTkOptionMenu(master=frame3, values=['Profilé laminés I ou H', 'Profilé laminés [', 'Reconstituées soudés en I ou H'], font=("Roboto", 16), width=400, height=30)
    type_profile_entry.pack(pady=12, padx=10)
    
    axe_moment = customtkinter.CTkOptionMenu(master=frame3, values=['Axe y', 'Axe z'], font=("Roboto", 16), width=400, height=30)
    axe_moment.pack(pady=12, padx=10)
    
    error = customtkinter.CTkLabel(master=root, text="", font=("Roboto", 16,))
    error.pack(pady=2, padx=10)

    frame5 = customtkinter.CTkFrame(master=root)
    frame5.pack(pady=5, padx=60)
    button = customtkinter.CTkButton(master=frame5, text="VERIFIER", width=300, height=30, font=("Roboto", 16, 'bold'), command=continuer_config)
    button.pack(pady=12, padx=10)

    root.mainloop()