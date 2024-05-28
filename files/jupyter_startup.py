
import os
import sys

def find_git_root(path):
    current_path = path
    while current_path != os.path.dirname(current_path):
        if os.path.isdir(os.path.join(current_path,'.git')):
            return current_path
        current_path = os.path.dirname(current_path)
    return None

notebook_dir = os.getcwd()

git_root_dit = find_git_root(notebook_dir)

if git_root_dit not in sys.path:
    sys.path.append(git_root_dit)