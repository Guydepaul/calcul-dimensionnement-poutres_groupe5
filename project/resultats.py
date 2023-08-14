import customtkinter
from back_data_constantes import *
from all_resultats import my_screen as all_results

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def my_screen():
    # screen.destroy()
    root = customtkinter.CTk()
    root.geometry("800x700")
    root.resizable(False, True)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    def fermer_tous():
        root.destroy()
                    
    frame1 = customtkinter.CTkFrame(master=root)
    frame1.pack(pady=10, padx=10)
    titre = customtkinter.CTkLabel(master=frame1, text="RÉSULTATS", font=("Roboto", 24, 'bold'))
    titre.pack(pady=0, padx=10)
        
    titre1= customtkinter.CTkLabel(master=root, text="Résultats de calcul", font=("Roboto", 24, 'bold'))
    titre1.pack(pady=1, padx=10)
    displayBox2 = customtkinter.CTkTextbox(root, width=750, height=250, fg_color='#345d91', text_color='#f2f2f2', font=("Roboto", 18))
    displayBox2.pack(pady=10, padx=0)
        
    titre2 = customtkinter.CTkLabel(master=root, text="Résultats de vérification", font=("Roboto", 24, 'bold'))
    titre2.pack(pady=1, padx=10)
    displayBox1 = customtkinter.CTkTextbox(root, width=750, height=250, fg_color='#2D3E40', text_color='#f2f2f2', font=("Roboto", 18))
    displayBox1.pack(pady=10, padx=0)
    
    frame_button = customtkinter.CTkFrame(master=root)
    frame_button.pack(pady=0, padx=10)

    continuer = customtkinter.CTkButton(master=frame_button, text="TOUS LES RESULTATS", font=("Roboto", 16, 'bold'), width=300, height=30, fg_color="gray", command=all_results)
    continuer.grid(row=0, column=0, padx=20, pady=10)

    continuer = customtkinter.CTkButton(master=frame_button, text="FERMER", font=("Roboto", 16, 'bold'), width=300, height=30, command=fermer_tous)
    continuer.grid(row=0, column=1, padx=20, pady=10)
    
    if read_resultat_calcul():
        for resultat_calcul in read_resultat_calcul():
            label = resultat_calcul[0]
            if RESULTATS_UTILE.get(label):
                label_1 = RESULTATS_UTILE.get(label)
                value = resultat_calcul[1]
                data = f"--> {label_1} ({label}) : {value}\n"
                displayBox2.insert("0.0", data)
    else:
        data = f"Aucun resultat de vérification trouvé dans le système\n"
        displayBox2.configure(text_color='red')
        displayBox2.insert(f"0.0", data)
    
    if read_resultat_verification():
        for resultat_verif in read_resultat_verification():
            label = resultat_verif[0]
            value = resultat_verif[1]
            data = f"{label} : {value}\n"
            displayBox1.insert(f"0.0", data)
    else:
        data = f"Aucun resultat de vérification trouvé dans le système\n"
        displayBox1.configure(text_color='red')
        displayBox1.insert(f"0.0", data)
        
    displayBox1.configure(state="disabled")
    displayBox2.configure(state="disabled")
    root.mainloop()