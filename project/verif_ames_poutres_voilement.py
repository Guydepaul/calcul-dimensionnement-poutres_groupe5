import customtkinter
from back_data_constantes import *
from back_functions import *
from resultats import my_screen as resultats_calcul_verif
from redimensionnement import my_screen as redimmention


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def my_screen():
    root = customtkinter.CTk()
    root.geometry("720x680")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    choix = [
        "Ames sans raidisseur",
        "Ames avec raidisseur transversaux intermediaire avec a/d < 1",
        "Ames avec raidisseur transversaux intermediaire avec a/d >= 1" 
    ]
    
    def continuer_config():
        try:
            a_entry_value = float(a_entry.get())
            d_entry_value = float(d_entry.get())
            fyw_entry_value = float(fyw_entry.get())
            mfrd_point_entry_value = float(mfrd_point_entry.get())
            vba_rd_entry_value = float(vba_rd_entry.get())
            
            choix_cas_entry_value = choix_cas_entry.get()
            
            epsilone = float(get_resultat_calcul('Epsilone')[1])
            tw = float(get_resultat_calcul('tw')[1])
            fy = float(get_resultat_calcul('Fy')[1])
            Grand_A = float(get_resultat_calcul('A')[1])
            Vsd = float(get_resultat_calcul('Vsd')[1])
            Msd = float(get_resultat_calcul('Msd')[1])
            Mr = float(get_resultat_calcul('Mr')[1])
            Nsd = float(get_resultat_calcul('Nsd')[1])
            
            if choix_cas_entry_value == choix[0]:
                cas = 'cas1'
            elif choix_cas_entry_value == choix[1]:
                cas = 'cas2'
            else:
                cas = 'cas3'
            
            K_tao = calcul_Ktao(cas, a_entry_value, d_entry_value)
            verif_resistance = verification_resistance_ames_poutres_voilement_cisaillement(K_tao, epsilone, d_entry_value, tw)
            
            if verif_resistance == 0:
                root.destroy()
                redimmention()
            else:
                verif_resistance = "Condition verifiée"
            
            lambdaBar_w = calcul_GamaBar_w(d_entry_value, tw, epsilone, K_tao)
            Tao_ba = calcul_Tao_ba(lambdaBar_w, fyw_entry_value)
            
            Vbrd = calcul_Vbrd(d_entry_value, tw, Tao_ba)
            
            if Vbrd >= Vsd:
                cond_verif_cisaillement = "Condition verifiée"
            else:
                root.destroy()
                redimmention()
            
            Nfrd = calcul_Nfrd(Grand_A, fy)
            Mfrd = calcul_Mfrd(mfrd_point_entry_value, Nsd, Nfrd)
            
            verif_interaction = verification_interaction_Vsd_Msd_Nsd(Vsd, vba_rd_entry_value, Msd, Mfrd, Mr)
            if verif_interaction == "Condition non vérifiée":
                root.destroy()
                redimmention()
            
            # Storage
            K_tao_result = ("K_tao", K_tao)
            lambdaBar_w_result = ("lambdaBar_w", lambdaBar_w)
            Tao_ba_result = ("Tao_ba", Tao_ba)
            Vbrd_result = ("Vbrd", Vbrd)
            Nfrd_result = ("Nfrd", Nfrd)
            Mfrd_result = ("Mfrd", Mfrd)
            
            cond_verif1_result = ("Resistance des ames au voilement", verif_resistance)
            cond_verif2_result = ("Cisaillement pur", cond_verif_cisaillement)
            cond_verif3_result = ("Interaction entre Vsd, Msd et Nsd", verif_interaction)
            
            add_data_to_db_resultat_calcul(resultat=K_tao_result)
            add_data_to_db_resultat_calcul(resultat=lambdaBar_w_result)
            add_data_to_db_resultat_calcul(resultat=Tao_ba_result)
            add_data_to_db_resultat_calcul(resultat=Vbrd_result)
            add_data_to_db_resultat_calcul(resultat=Nfrd_result)
            add_data_to_db_resultat_calcul(resultat=Mfrd_result)
            
            add_data_to_db_resultat_verification(resultat=cond_verif1_result)
            add_data_to_db_resultat_verification(resultat=cond_verif2_result)
            add_data_to_db_resultat_verification(resultat=cond_verif3_result)
            
            
            root.destroy()
            resultats_calcul_verif()
        except Exception as e:
            error.configure(text=e, text_color='red')
        
                
    frame1 = customtkinter.CTkFrame(master=root)
    frame1.pack(pady=20, padx=10)
    titre = customtkinter.CTkLabel(master=frame1, text="VERIFICATION DES AMES DES POUTRES AU VOILEMENT", font=("Roboto", 24, 'bold'))
    titre.pack(pady=0, padx=10)
        
    frame2 = customtkinter.CTkFrame(master=root)
    frame2.pack(pady=0, padx=0)
    titre2 = customtkinter.CTkLabel(master=frame2, text="Résistance des ames au voilement par cisaillement", font=("Roboto", 24, 'bold'))
    titre2.pack(pady=12, padx=10)
    a_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Entrer la valeur de a", font=("Roboto", 16), width=600, height=30)
    a_entry.pack(pady=12, padx=10)
    d_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Entrer la valeur de d", font=("Roboto", 16), width=600, height=30)
    d_entry.pack(pady=12, padx=10)
    
    choix_cas_entry = customtkinter.CTkOptionMenu(master=frame2, values=choix, font=("Roboto", 16), width=600, height=30)
    choix_cas_entry.pack(pady=12, padx=10)
    
    frame4 = customtkinter.CTkFrame(master=root)
    frame4.pack(pady=5, padx=0)
    titre2 = customtkinter.CTkLabel(master=frame4, text="Méthode Post-critique simple : Cisaillement pur", font=("Roboto", 24, 'bold'))
    titre2.pack(pady=5, padx=10)
    fyw_entry = customtkinter.CTkEntry(master=frame4, placeholder_text="Entrer la valeur de fyw", font=("Roboto", 16), width=600, height=30)
    fyw_entry.pack(pady=5, padx=10)
    
    frame3 = customtkinter.CTkFrame(master=root)
    frame3.pack(pady=5, padx=0)
    titre2 = customtkinter.CTkLabel(master=frame3, text="Interaction entre effort tranchant Vsd, Moment \nflechissant Msd et l'effort axial Nsd", font=("Roboto", 24, 'bold'))
    titre2.pack(pady=12, padx=10)
    mfrd_point_entry = customtkinter.CTkEntry(master=frame3, placeholder_text="Entrer la valeur de M°f,rd", font=("Roboto", 16), width=600, height=30)
    mfrd_point_entry.pack(pady=12, padx=10)
    vba_rd_entry = customtkinter.CTkEntry(master=frame3, placeholder_text="Entrer la valeur de Vba,rd", font=("Roboto", 16), width=600, height=30)
    vba_rd_entry.pack(pady=5, padx=10)
    
    error = customtkinter.CTkLabel(master=root, text="", font=("Roboto", 16,))
    error.pack(pady=2, padx=10)
    
    button = customtkinter.CTkButton(master=root, text="VERIFIER", width=300, height=30, font=("Roboto", 16, 'bold'), command=continuer_config)
    button.pack(pady=5, padx=10)

    root.mainloop()