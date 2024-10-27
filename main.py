import os
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

working_directory = "/Users/sentokai/Desktop/apps/apps_apk"


def get_apk_files(directory):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        files.remove('.DS_Store')
        return files
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))
        return []


def create_interface(files):
    root = tk.Tk()
    root.title("APK Files Installer")

    mainframe = ttk.Frame(root, padding="10 10 70 10")
    mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    ttk.Label(mainframe, text="Выберите файлы APK:").grid(row=0, column=0, sticky=tk.W)

    check_vars = []
    for idx, file in enumerate(files):
        var = tk.BooleanVar()
        check_vars.append(var)
        ttk.Checkbutton(mainframe, text=file, variable=var).grid(row=idx+1, column=0, sticky=tk.W)


    def submit():
        print('[INFO] Идет установка приложений')
        selected_files = [file for idx, file in enumerate(files) if check_vars[idx].get()]
        command = ''
        for app in selected_files:
            command+= f'adb install {app} & '
        
        result = subprocess.run(command[:-2], shell=True, cwd=working_directory, capture_output=True, text=True)
        print("Output:", result.stdout)
        print("Error:", result.stderr)
        print("Return Code:", result.returncode)

    ttk.Button(mainframe, text="Подтвердить", command=submit).grid(row=len(files)+1, column=0, sticky=tk.W)

    root.mainloop()


if __name__ == "__main__":
    apk_directory = os.path.join(os.getcwd(), "apps_apk")
    apk_files = get_apk_files(apk_directory)
    create_interface(apk_files)
