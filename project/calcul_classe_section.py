import customtkinter
from back_data_constantes import *
from back_functions import *
from verif_resistance_poutres import my_screen as resistance_poutre_verif

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def my_screen():
    root = customtkinter.CTk()
    root.geometry("700x350")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    def continuer_config():
        try:
            effort_axial_entry_value = effort_axial_entry.get()
            r_entry_value = r_entry.get()
            sollicitation_entry_value = choix_sollicitation_entry.get()
            r = float(r_entry_value)
            Nsd = float(effort_axial_entry_value)
            acier = get_resultat_calcul('Type acier')[1]
            section_type = get_resultat_calcul('Type de section profilé')[1]
            profile = get_resultat_calcul('Profilé')[1]
            
            dataExcel = GetDataExcelFile()
            acierSheet = dataExcel.getDataAcier('CA')
            section_type_sheet = dataExcel.getDataProfilee(section_type)
            fy = None
            tf = None
            b = None
            tw = None
            d = None
            h = None
            
            for acierS in acierSheet[1:]:
                if acier == acierS[0]:
                    fy = float(acierS[1])
                
            for section in section_type_sheet[1:]:
                if profile == section[0]:
                    h = float(section[2])
                    b = float(section[3])
                    tw = float(section[4])
                    tf = float(section[5])
                    Grand_A = float(section[6]) * (10**2)
                    d = float(section[7])
                    Iy = float(section[13]) * (10**4)
                    Iz = float(section[18]) * (10**4)
                    Wply = float(section[15]) * (10**3)
                    Wplz = float(section[20]) * (10**3)
                    Wely = float(section[14]) * (10**3)
                    iy = float(section[16]) * (10)
                    Iw = float(section[24]) * (10**9)
                    It = float(section[23]) * (10**4)
                    
            if None not in [fy, tf, b, tw, d, h]:
                c = round(calcul_C(b, r, tw), 2)
                epsilone = round(calcul_Epsilone(fy), 2)
                alpha = round(calcul_Alpha(d, h, Nsd, tw, fy, tf, r))
                                
                c_sur_tf = c / tf
                d_sur_tw = d / tw
                
                cas = None
                
                if sollicitation_entry_value == 'La section est sollicité en compression':
                    cas = 'Cas1'
                elif sollicitation_entry_value == 'La section est sollicité en fléxion':
                    cas = 'Cas2'
                elif sollicitation_entry_value == 'La section est sollicité en fléxion composée':
                    cas = 'Cas3'
                    
                if cas == 'Cas3':
                    classe_section = verification_classe_section_poutre(cas, c_sur_tf, d_sur_tw, epsilone, alpha)
                else:
                    classe_section = verification_classe_section_poutre(cas, c_sur_tf, d_sur_tw, epsilone)
                    
                c_result = ('C', c)
                espilone_result = ('Epsilone', epsilone)
                alpha_result = ('Alpha', alpha)
                classe_section_result = ('Classe section', classe_section)
                fy_result = ('Fy', fy)
                A_result = ('A', Grand_A)
                tf_result = ('tf', tf)
                tw_result = ('tw', tw)
                r_result = ('r', r)
                h_result = ('h', h)
                Iy_result = ('Iy', Iy)
                Iz_result = ('Iz', Iz)
                Wply_result = ('Wply', Wply)
                Wplz_result = ('Wplz', Wplz)
                Wely_result = ('Wely', Wely)
                iy_result = ('iy', iy)
                Iw_result = ('Iw', Iw)
                It_result = ('It', It)
                Nsd_result = ('Nsd', Nsd)
                
                add_data_to_db_resultat_calcul(resultat=c_result)
                add_data_to_db_resultat_calcul(resultat=espilone_result)
                add_data_to_db_resultat_calcul(resultat=alpha_result)
                add_data_to_db_resultat_calcul(resultat=classe_section_result)
                add_data_to_db_resultat_calcul(resultat=fy_result)
                add_data_to_db_resultat_calcul(resultat=A_result)
                add_data_to_db_resultat_calcul(resultat=tf_result)
                add_data_to_db_resultat_calcul(resultat=tw_result)
                add_data_to_db_resultat_calcul(resultat=r_result)
                add_data_to_db_resultat_calcul(resultat=h_result)
                add_data_to_db_resultat_calcul(resultat=Iy_result)
                add_data_to_db_resultat_calcul(resultat=Iz_result)
                add_data_to_db_resultat_calcul(resultat=Wply_result)
                add_data_to_db_resultat_calcul(resultat=Wplz_result)
                add_data_to_db_resultat_calcul(resultat=Wely_result)
                add_data_to_db_resultat_calcul(resultat=iy_result)
                add_data_to_db_resultat_calcul(resultat=Iw_result)
                add_data_to_db_resultat_calcul(resultat=It_result)
                add_data_to_db_resultat_calcul(resultat=Nsd_result)
                
                root.destroy()
                resistance_poutre_verif()
            
            else:
                error.configure(text="Une des valeurs utilisées pour cette opération est nulle", text_color='red')
                    
        except Exception as e:
            error.configure(text=e, text_color='red')
        
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    titre = customtkinter.CTkLabel(master=frame, text="CALCUL DE CLASSE DE LA SECTION", font=("Roboto", 24, 'bold'))
    titre.pack(pady=12, padx=10)
    
    effort_axial_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Effort axial (Nsd)", font=("Roboto", 16), width=400, height=30)
    effort_axial_entry.pack(pady=12, padx=10)
    
    r_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Entrer la valeur de r", font=("Roboto", 16), width=400, height=30)
    r_entry.pack(pady=12, padx=10)
    
    sollicitation_choice = [
        'La section est sollicité en compression',
        'La section est sollicité en fléxion',
        'La section est sollicité en fléxion composée',
    ]
    
    choix_sollicitation_label = customtkinter.CTkLabel(master=frame, text="Selectionner la sollicitation", font=("Roboto", 16, 'bold'))
    choix_sollicitation_label.pack(padx=10)
    choix_sollicitation_entry = customtkinter.CTkOptionMenu(master=frame, values=sollicitation_choice, font=("Roboto", 16), width=400, height=30)
    choix_sollicitation_entry.pack(padx=10)

    button = customtkinter.CTkButton(master=frame, text="CALCULER", width=300, height=30, font=("Roboto", 16, 'bold'), command=continuer_config)
    button.pack(pady=12, padx=10)
    
    error = customtkinter.CTkLabel(master=frame, text="", font=("Roboto", 16,))
    error.pack(pady=12, padx=10)

    root.mainloop()