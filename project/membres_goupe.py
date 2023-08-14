# Ici nous aurons nos interfaces graphiques
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def my_screen():
    root = customtkinter.CTk()
    root.geometry("800x600")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    def fermer():
        root.destroy()
        

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    customtkinter.CTkLabel(master=frame, 
                                    text="MEMBRE DU GROUPE 1", 
                                    font=("Roboto", 20, 'bold')
                                ).pack(pady=12, padx=10)

    customtkinter.CTkLabel(master=frame, 
                                    text="1. MUGISHO CIRINDYE Frederick", 
                                    font=("Roboto", 20, 'bold')
                                ).pack(pady=12, padx=10)
    customtkinter.CTkLabel(master=frame, 
                                    text="2. MUGISHO CIRINDYE Frederick", 
                                    font=("Roboto", 20, 'bold')
                                ).pack(pady=12, padx=10)
    customtkinter.CTkLabel(master=frame, 
                                    text="3. MUGISHO CIRINDYE Frederick", 
                                    font=("Roboto", 20, 'bold')
                                ).pack(pady=12, padx=10)
    customtkinter.CTkLabel(master=frame, 
                                    text="4. MUGISHO CIRINDYE Frederick", 
                                    font=("Roboto", 20, 'bold')
                                ).pack(pady=12, padx=10)
    customtkinter.CTkLabel(master=frame, 
                                    text="5. MUGISHO CIRINDYE Frederick", 
                                    font=("Roboto", 20, 'bold')
                                ).pack(pady=12, padx=10)
    customtkinter.CTkLabel(master=frame, 
                                    text="6. MUGISHO CIRINDYE Frederick", 
                                    font=("Roboto", 20, 'bold')
                                ).pack(pady=12, padx=10)
    customtkinter.CTkLabel(master=frame, 
                                    text="7. MUGISHO CIRINDYE Frederick", 
                                    font=("Roboto", 20, 'bold')
                                ).pack(pady=12, padx=10)
    customtkinter.CTkLabel(master=frame, 
                                    text="8. MUGISHO CIRINDYE Frederick", 
                                    font=("Roboto", 20, 'bold')
                                ).pack(pady=12, padx=10)

    continuer = customtkinter.CTkButton(master=frame, text="FERMER", font=("Roboto", 20, 'bold'), width=300, height=30, command=fermer)
    continuer.pack(pady=12, padx=10)

    root.mainloop()