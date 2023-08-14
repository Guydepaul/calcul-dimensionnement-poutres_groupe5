# Ici nous aurons nos interfaces graphiques
import customtkinter
from calcul_platelage import calcul_du_platelage as calc_plat
from back_data_constantes import delete_all_data
from membres_goupe import my_screen as membres
import webbrowser

home = customtkinter.CTk()
home.geometry("800x380")
home.resizable(False, False)
home.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# customtkinter.set_appearance_mode("light")
# customtkinter.set_default_color_theme("dark-blue")


delete_all_data()

def function_continuer():
    home.destroy()
    calc_plat()
    
#def about_function():
  #  url_website = f"https://github.com/Guydepaul/calcul-dimensionnement-poutres_groupe"
   # webbrowser.open(url_website)
    
def membres_here():
    membres()

titre = customtkinter.CTkLabel(master=home, 
                                text="CALCUL ET DIMENSIONNEMENT DES POUTRES", 
                                font=("Roboto", 24, 'bold')
                            ).pack(pady=50, padx=10)

groupe_number = customtkinter.CTkLabel(master=home, 
                                text="GROUPE 1", 
                                font=("Roboto", 20, 'bold')
                            ).pack(pady=12, padx=10)

promotion = customtkinter.CTkLabel(master=home, 
                                text="TECH 1 - GC - SOA", 
                                font=("Roboto", 20, 'bold')
                            ).pack(pady=12, padx=10)

frame_button = customtkinter.CTkFrame(master=home)
frame_button.pack(pady=12, padx=10)

about = customtkinter.CTkButton(master=frame_button, text="A propos", fg_color='#2D3E40', font=("Roboto", 20, 'bold'), width=150, height=30, command=about_function)
about.grid(row=0, column=0, pady=12, padx=10)
member_group = customtkinter.CTkButton(master=frame_button, text="Membres", fg_color='#2D3E40', font=("Roboto", 20, 'bold'), width=150, height=30, command=membres_here)
member_group.grid(row=0, column=1, pady=12, padx=10) 
continuer = customtkinter.CTkButton(master=frame_button, text="CONTINUER", font=("Roboto", 20, 'bold'), width=150, height=30, command=function_continuer)
continuer.grid(row=0, column=2, pady=12, padx=10)

home.mainloop()