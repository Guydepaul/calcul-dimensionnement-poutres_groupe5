import customtkinter
from back_functions import *
from verif_rigidite_poutres import my_screen as rigidite_screen
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
from redimensionnement import my_screen as redimmention

def my_screen():
    root = customtkinter.CTk()
    root.geometry("600x590")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    def continuer_config():
        try:
            qv_entry_value = float(qv_entry.get())
            qh_entry_value = float(qh_entry.get())
            Gv_entry_value = float(Gv_entry.get())
            Gh_entry_value = float(Gh_entry.get())
            angle_alpha_entry_value = float(angle_alpha_entry.get())
            l_entry_value = float(l_entry.get())
            grand_a_entry_value = float(grand_a_entry.get())
            Wx_entry_value = float(Wx_entry.get())
            Wy_entry_value = float(Wy_entry.get())
            Wz_entry_value = float(Wz_entry.get())
            
            Fy = float(get_resultat_calcul('Fy')[1])
            Wply = float(get_resultat_calcul('Wply')[1])
            Wplz = float(get_resultat_calcul('Wplz')[1])
            Wplz = float(get_resultat_calcul('Wplz')[1])
            classe = get_resultat_calcul('Classe section')[1]
            Nsd = float(get_resultat_calcul('Nsd')[1])
            
            if classe == 'Classe 1':
                classe_val = 1
            elif classe == 'Classe 2':
                classe_val = 2
            elif classe == 'Classe 3':
                classe_val = 3
            else:
                classe_val = 4
                        
            resultat_calcul = calcul_flexion_deviee(qv_entry_value, qh_entry_value, Gv_entry_value, Gh_entry_value, angle_alpha_entry_value, l_entry_value, Wply, Wplz, Fy)
            qy = resultat_calcul['qy']
            qz = resultat_calcul['qz']
            Qy_ponderee = resultat_calcul['Qy_ponderee']
            Qz_ponderee = resultat_calcul['Qz_ponderee']
            My_sd = resultat_calcul['My_sd']
            Mz_sd = resultat_calcul['Mz_sd']
            Mpl_y_rd = resultat_calcul['Mpl_y_rd']
            Mpl_z_rd = resultat_calcul['Mpl_z_rd']
            Nplrd = float(calcul_Nplrd(grand_a_entry_value, Fy))
            
            verif_cond = verification_flexion_deviee(classe_val, Nsd, grand_a_entry_value, Fy, My_sd, Mz_sd, Mpl_y_rd, Mpl_z_rd, Wx_entry_value, Wy_entry_value, Wz_entry_value, Nplrd)
            
            if verif_cond != 1:
                root.destroy()
                redimmention()
            else:
                cond_state = "Condition vérifiée"
            
            qy_result = ('qy', qy)
            qz_result = ('qz', qz)
            Qy_ponderee_result = ('Qy_ponderee', Qy_ponderee)
            Qz_ponderee_result = ('Qz_ponderee', Qz_ponderee)
            My_sd_result = ('My_sd', My_sd)
            Mz_sd_result = ('Mz_sd', Mz_sd)
            Mpl_y_rd_result = ('Mpl_y_rd', Mpl_y_rd)
            Mpl_z_rd_result = ('Mpl_z_rd', Mpl_z_rd)
            Nplrd_result = ('Nplrd', Nplrd)
            
            verif_state = ("Fléxion déviée", cond_state)
            
            add_data_to_db_resultat_calcul(resultat=qy_result)
            add_data_to_db_resultat_calcul(resultat=qz_result)
            add_data_to_db_resultat_calcul(resultat=Qy_ponderee_result)
            add_data_to_db_resultat_calcul(resultat=Qz_ponderee_result)
            add_data_to_db_resultat_calcul(resultat=My_sd_result)
            add_data_to_db_resultat_calcul(resultat=Mz_sd_result)
            add_data_to_db_resultat_calcul(resultat=Mpl_y_rd_result)
            add_data_to_db_resultat_calcul(resultat=Mpl_z_rd_result)
            add_data_to_db_resultat_calcul(resultat=Nplrd_result)
            
            add_data_to_db_resultat_verification(resultat=verif_state)
            
            root.destroy()
            rigidite_screen()
            
        except Exception as e:
            error.configure(text=e, text_color='red')
        
                
    frame1 = customtkinter.CTkFrame(master=root)
    frame1.pack(pady=20, padx=10)
    titre = customtkinter.CTkLabel(master=frame1, text="VERIFICATION EN FLEXION DEVIÉE", font=("Roboto", 24, 'bold'))
    titre.pack(pady=12, padx=10)
    
    qv_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de qv", font=("Roboto", 16), width=500, height=30)
    qv_entry.pack(pady=5, padx=10)
    qh_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de qh", font=("Roboto", 16), width=500, height=30)
    qh_entry.pack(pady=5, padx=10)
    Gv_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de Gv", font=("Roboto", 16), width=500, height=30)
    Gv_entry.pack(pady=5, padx=10)
    Gh_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de Gh", font=("Roboto", 16), width=500, height=30)
    Gh_entry.pack(pady=5, padx=10)
    angle_alpha_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de l'angle alpha", font=("Roboto", 16), width=500, height=30)
    angle_alpha_entry.pack(pady=5, padx=10)
    l_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de l", font=("Roboto", 16), width=500, height=30)
    l_entry.pack(pady=5, padx=10)
    
    frame2 = customtkinter.CTkFrame(master=root)
    frame2.pack(pady=0, padx=10)
    
    Wx_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Entrer la valeur de Wx", font=("Roboto", 16), width=500, height=30)
    Wx_entry.pack(pady=5, padx=10)
    Wy_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Entrer la valeur de Wy", font=("Roboto", 16), width=500, height=30)
    Wy_entry.pack(pady=5, padx=10)
    Wz_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Entrer la valeur de Wz", font=("Roboto", 16), width=500, height=30)
    Wz_entry.pack(pady=5, padx=10)
    grand_a_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Entrer la valeur de A", font=("Roboto", 16), width=500, height=30)
    grand_a_entry.pack(pady=5, padx=10)
    
    error = customtkinter.CTkLabel(master=frame2, text="", font=("Roboto", 16,))
    error.pack(pady=2, padx=10)

    button = customtkinter.CTkButton(master=frame2, text="VERIFIER", width=300, height=30, font=("Roboto", 16, 'bold'), command=continuer_config)
    button.pack(pady=10, padx=10)

    root.mainloop()