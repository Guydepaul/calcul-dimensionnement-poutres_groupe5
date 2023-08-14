import customtkinter
from back_data_constantes import *
from back_functions import *
from calcul_moment_critique_elastic import my_screen as calcul_moment_critique
from redimensionnement import my_screen as redimmention

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def my_screen():
    root = customtkinter.CTk()
    root.geometry("500x420")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    def verifier():
        try:
            c1_entry_value = float(c1_entry.get())
            l_entry_value = float(l_entry.get())
            alphaLT_entry_value = float(alphaLT_entry.get())
            
            classe = get_resultat_calcul('Classe section')[1]
            Wely = float(get_resultat_calcul('Wely')[1])
            Wply = float(get_resultat_calcul('Wply')[1])
            espilone = float(get_resultat_calcul('Epsilone')[1])
            iy = float(get_resultat_calcul('iy')[1])
            h = float(get_resultat_calcul('h')[1])
            tf = float(get_resultat_calcul('tf')[1])
            fy = float(get_resultat_calcul('Fy')[1])
            if classe in ['Classe 1', 'Classe 2']:
                classe_val = 1
            elif classe == 'Classe 3':
                classe_val = 3
            else:
                classe_val = 4
            
            beta_omega = float(calcul_BetaOmega(classe_val, Wply, Wely))
            gamma1 = float(calcul_Gama1(espilone))
            gammaLT = float(calcul_GamaLT(l_entry_value, iy, c1_entry_value, h, tf))
            gammaBar_LT = float(calcul_GamaBarLT(gammaLT, gamma1, beta_omega))
            phiLT = float(calcul_PhiLT(alphaLT_entry_value, gammaBar_LT))
            xlt = float(calcul_Xlt(phiLT, gammaBar_LT))
            Mb_rd = calcul_Mbrd(beta_omega, xlt, Wely, fy)
            
            if gammaLT <= 0.4:
                cond_state = "Stabilité au deversement assurée"
            else:
                root.destroy()
                redimmention()
            
            beta_omega_result = ("Beta Omega", beta_omega)
            gamma1_result = ("λ1", gamma1)
            gammaLT_result = ("λLT", gammaLT)
            gammaBar_LT_result = ("λ Bar LT", gammaBar_LT)
            phiLT_result = ("ɸLT", phiLT)
            xlt_result = ("X LT", xlt)
            Mb_rd_result = ("Mb,rd", Mb_rd)
            cond_verif_result = ("Rigidité des poutres", cond_state)

            add_data_to_db_resultat_calcul(resultat=beta_omega_result)
            add_data_to_db_resultat_calcul(resultat=gamma1_result)
            add_data_to_db_resultat_calcul(resultat=gammaLT_result)
            add_data_to_db_resultat_calcul(resultat=gammaBar_LT_result)
            add_data_to_db_resultat_calcul(resultat=phiLT_result)
            add_data_to_db_resultat_calcul(resultat=xlt_result)
            add_data_to_db_resultat_calcul(resultat=Mb_rd_result)
            add_data_to_db_resultat_verification(resultat=cond_verif_result)
            
            root.destroy()
            calcul_moment_critique()
            
        except Exception as e:
            error.configure(text=e, text_color='red')
                
    frame1 = customtkinter.CTkFrame(master=root)
    frame1.pack(pady=40, padx=10)
    titre = customtkinter.CTkLabel(master=frame1, text="VERIFICATION DE LA STABILITÉ \nAU DEVERSEMENT DES POUTRES", font=("Roboto", 24, 'bold'))
    titre.pack(pady=12, padx=10)
    
    c1_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de C1", font=("Roboto", 16), width=400, height=30)
    c1_entry.pack(pady=12, padx=10)
    
    l_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de L", font=("Roboto", 16), width=400, height=30)
    l_entry.pack(pady=12, padx=10)
    
    alphaLT_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de Alpha LT", font=("Roboto", 16), width=400, height=30)
    alphaLT_entry.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame1, text="VERIFIER", width=300, height=30, font=("Roboto", 16, 'bold'), command=verifier)
    button.pack(pady=12, padx=10)
    
    error = customtkinter.CTkLabel(master=frame1, text="", font=("Roboto", 16,))
    error.pack(pady=2, padx=10)

    root.mainloop()