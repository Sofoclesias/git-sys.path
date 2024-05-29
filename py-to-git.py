import os
import tkinter as tk
import shutil
import subprocess

def add_git():
    # Para Notebooks
    config_file = os.path.expanduser("~/.jupyter/jupyter_notebook_config.py")
    ipy_dir = os.path.expanduser("~/.ipython/profile_default/startup/")

    if os.path.exists(config_file):
        print('Existe config file.')
        name = os.path.basename(config_file)
        shutil.copyfile(config_file, os.path.join('backup',name))
    else:
        batch_script_path = os.path.join(os.getcwd(), 'files/run_command.bat')
        process = subprocess.run(['cmd.exe', '/C', batch_script_path], capture_output=True, text=True)
        print('Output:', process.stdout)
        config_file = os.path.expanduser("~/.jupyter/jupyter_notebook_config.py")

    shutil.copy('files/jupyter_startup.py',ipy_dir)

    agregar = [
        """c.InteractiveShellApp.exec_lines = ["""
        'import os, sys; exec(open(os.path.expanduser("~/.ipython/profile_default/startup/00-startup.py")).read())'
    """]"""   
    ]
    
    with open(config_file, 'a') as file:
        file.writelines(agregar)
    
    # Para archivos python
    site_file = os.path.expanduser('~/anaconda3/Lib/')
    
    if os.path.exists(site_file + 'sitecustomize.py'):
        print('Existe archivo sitecustomize.')
        name = os.path.basename(site_file + 'sitecustomize.py')
        shutil.copyfile(site_file, os.path.join('backup',name))
    
    shutil.copy('files/sitecustomize.py', site_file)
    
    print('Excepción creada con éxito.')

def purge():
    config_dir = os.path.expanduser("~/.jupyter/")
    ipy_dir = os.path.expanduser("~/.ipython/profile_default/startup/")

    # Para notebook
    if os.path.exists(r'backup\jupyter_notebook_config.py'):
        os.remove(config_dir + r'\\jupyter_notebook_config.py')
        os.remove(ipy_dir + r'\\jupyter_startup.py')
        shutil.move(r'backup\jupyter_notebook_config.py', config_dir)
    else:
        os.remove(config_dir + r'\\jupyter_notebook_config.py')
        os.remove(ipy_dir + r'\\jupyter_startup.py')
    
    # Para py file
    site_dir = os.path.expanduser('~/anaconda3/Lib/')
    
    if os.path.exists(r'backup\sitecustomize.py'):
        os.remove(site_dir + r'\\sitecustomize.py')
        shutil.move(r'backup\sitecustomize.py', site_dir)
    else:
        os.remove(site_dir + r'\\sitecustomize.py')
    
    print('Reseteado a configuraciones iniciales.')
        
def gui():
    """
    Create the GUI.
    """
    root = tk.Tk()
    root.title("Optiones")

    add_button = tk.Button(root, text="Agregar .git a sys.path", command=add_git)
    add_button.pack(pady=10)

    purge_button = tk.Button(root, text="Purgar", command=purge)
    purge_button.pack(pady=10)

    root.mainloop()
    
if __name__ == "__main__":
    gui()