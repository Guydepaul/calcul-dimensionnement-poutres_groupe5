import customtkinter
from back_data_constantes import *
from calcul_poussee import my_screen as calcul_poussee
from back_functions import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def calcul_du_platelage():
    root = customtkinter.CTk()
    root.geometry("600x460")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    def calculer():
        q_value = q.get()
        g_value = g.get()
        a_value = a.get()
        n0_value = n0.get()
        t_value = t.get()

        try:
            q_val = float(q_value)
            g_val = float(g_value)
            a_val = float(a_value)
            n0_val = float(n0_value)
            t_val = float(t_value)

            Pn = calcul_Pn(g_val, q_val, a_val)
            e1 = calcul_E1()
            
            condition = False
            if Pn <= 10:
                if t_val < 6 or t_val > 8:
                    error.configure(text="La valeur de t n'est pas dans l'intervale (t = 6 à 8)", text_color='red')
                else:
                    condition = True
                    
            if Pn >= 11 and Pn <= 20:
                if t_val < 8 or t_val > 10:
                    error.configure(text="La valeur de t n'est pas dans l'intervale (t = 8 à 10)", text_color='red')
                else:
                    condition = True
                    
            if Pn >= 21 and Pn <= 30:
                if t_val < 10 or t_val > 12:
                    error.configure(text="La valeur de t n'est pas dans l'intervale (t = 10 à 12)", text_color='red')
                else:
                    condition = True
                
            if Pn > 30:
                if t_val < 12 or t_val > 14:
                    error.configure(text="La valeur de t n'est pas dans l'intervale (t = 12 à 14)", text_color='red')
                else:
                    condition = True
            
            if condition:
                aL = calcul_a(n0_val, e1, Pn, t_val)
                
                pn_result = ('Pn', Pn)
                e1_result = ('E1', e1)
                aL_result = ('a', aL)
                t_result = ('t', t_val)
                Q_result = ('Q', q_val)
                G_result = ('G', g_val)
                
                add_data_to_db_resultat_calcul(resultat=pn_result)
                add_data_to_db_resultat_calcul(resultat=e1_result)
                add_data_to_db_resultat_calcul(resultat=aL_result)
                add_data_to_db_resultat_calcul(resultat=t_result)
                add_data_to_db_resultat_calcul(resultat=Q_result)
                add_data_to_db_resultat_calcul(resultat=G_result)
                
                
                root.destroy()
                calcul_poussee()

        except Exception as e:
            error.configure(text=e, text_color='red')

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=40, fill="both", expand=True)

    titre = customtkinter.CTkLabel(master=frame, text="CALCUL DU PLATELAGE", font=("Roboto", 24, 'bold'))
    titre.pack(pady=12, padx=10)

    q = customtkinter.CTkEntry(master=frame, placeholder_text="Entrer valeur de Q", font=("Roboto", 18,), width=550, height=30)
    q.pack(pady=12, padx=10)

    g = customtkinter.CTkEntry(master=frame, placeholder_text="Entrer valeur de G", font=("Roboto", 18,), width=550, height=30)
    g.pack(pady=12, padx=10)

    t = customtkinter.CTkEntry(master=frame, placeholder_text="Entrer valeur de t", font=("Roboto", 18,), width=550, height=30)
    t.pack(pady=12, padx=10)

    a = customtkinter.CTkEntry(master=frame, placeholder_text="Entrer valeur de l'ecartement de poutre de platelage a", font=("Roboto", 18,), width=550, height=30)
    a.pack(pady=12, padx=10)

    n0 = customtkinter.CTkOptionMenu(master=frame, values=['150', '200'], font=("Roboto", 18,), width=550, height=30)
    n0.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="CALCULER", width=300, height=30, command=calculer)
    button.pack(pady=12, padx=10)

    error = customtkinter.CTkLabel(master=frame, text="", font=("Roboto", 16,))
    error.pack(pady=12, padx=10)


    root.mainloop()