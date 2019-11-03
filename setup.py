"""
== SETUP.PY FILE FOR USE WITH CX_FREEZE AND PYTHON 3.6 ==
==== INSTRUCTIONS  ====
1. Make sure you have Python 3.6 installed.
2. Install cx_Freeze by typing `pip install cx_freeze` in the Terminal or Command Prompt. Make sure to use the pip for Python 3 (sometimes called pip3)
3. Create a new file called setup.py and paste the contents of this file in it (or just download this file)
4. Make sure to place the setup.py file in the same directory where your main Python application is located
5. From the Terminal/Command Prompt, run `python setup.py build`. Make sure that you're running Python 3.6 (use `python --version`)
6. Enjoy!
The script should have created another folder called `build/`. You will find your generated .exe file.
"""
import os
from cx_Freeze import setup, Executable
os.environ['TCL_LIBRARY'] = r'C:\Users\Champ\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Champ\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

executables = [Executable("StudentRe3_0.py",icon="iconn.ico", base = "Win32GUI")]

"""packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}"""


build_exe_options = {"include_files": ["tcl86t.dll", "tk86t.dll"]} 




setup(
    name = "Prommanusorn Recruitment Program",
    options = {"build_exe": build_exe_options},
    version = "1.0",
    description = 'For Recruitment',
    executables = executables
)