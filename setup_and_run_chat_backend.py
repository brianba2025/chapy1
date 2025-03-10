
import os
import subprocess
import sys

# Ruta base
base_dir = os.path.join(os.path.dirname(__file__), "backend")
venv_path = os.path.join(base_dir, "venv")
requirements_path = os.path.join(base_dir, "requirements.txt")
manage_py_path = os.path.join(base_dir, "manage.py")

def create_venv():
    if not os.path.exists(venv_path):
        print("✅ Creando entorno virtual...")
        subprocess.run([sys.executable, "-m", "venv", venv_path])
    else:
        print("⚠️ El entorno virtual ya existe.")

def activate_venv_and_install():
    activate_script = os.path.join(venv_path, "Scripts", "activate.bat")
    if not os.path.exists(activate_script):
        print("❌ No se encontró el entorno virtual.")
        return
    print("✅ Activando entorno virtual...")
    pip_path = os.path.join(venv_path, "Scripts", "pip.exe")
    subprocess.run([pip_path, "install", "-r", requirements_path])

def run_server():
    python_path = os.path.join(venv_path, "Scripts", "python.exe")
    subprocess.run([python_path, manage_py_path, "runserver"])

if __name__ == "__main__":
    print("🚀 Preparando entorno del Chat IA...")
    create_venv()
    activate_venv_and_install()
    run_server()
