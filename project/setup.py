from cx_Freeze import setup, Executable

base = None
executables = [Executable("home.py", base=base)]

packages = ["idna", "customtkinter", "sqlite3", "openpyxl", "webbrowser"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
setup(
    name = "Calcul-Dimensionnement-Poutres",
    options = options,
    version = "1.0",
    description = 'Voici mon programme',
    executables = executables
)

# python setup.py build
# https://plainenglish.io/blog/convert-a-python-project-to-an-executable-exe-file