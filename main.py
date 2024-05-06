import subprocess
import os
import tkinter as tk

# Point to installers with loadInstallers

# For installers that may require interatction i.e. keys look into process communicate



def loadInstallers():
        installers = [
            {"name": "Google Chrome",
            "path": "path_to",
            "args": "/silent /install"},

            {"name": "example",
            "path": "path_to",
            "args": "/silent /install"},

            {"name": "example",
            "path": "path_to=",
            "args": "/silent /install"}
        ]
        
        return installers

def main():

    installers = loadInstallers()

    for software in installers:
        process = subprocess.Popen(software["path"] + " " + software["args"], shell=True, stdin=subprocess.PIPE)
        process.communicate(input=b'CD_KEY\n')  # Replace CD_KEY with the actual CD key


    pass



if __name__ == '__main__':
     main()