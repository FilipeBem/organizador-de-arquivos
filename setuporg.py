import cx_Freeze

executables = [cx_Freeze.Executable('organizador.py')]

cx_Freeze.setup(
    name="Organizador de arquivos",
    options={'build_exe': {'packages':['PySimpleGUI']}},

    executables = executables
)