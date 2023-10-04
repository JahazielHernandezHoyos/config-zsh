import os
import subprocess

# Comprobar si Zsh está instalado
def is_zsh_installed():
    return os.path.exists("/bin/zsh") or os.path.exists("/usr/bin/zsh")

# Instalar Zsh si no está instalado
def install_zsh():
    if not is_zsh_installed():
        subprocess.run(["sudo", "apt-get", "install", "zsh"])

# Instalar Oh My Zsh
def install_oh_my_zsh():
    subprocess.run(["sh", "-c", "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"])

# Instalar el plugin Zsh Autosuggestions
def install_zsh_autosuggestions():
    if not os.path.exists("~/.oh-my-zsh/custom/plugins/zsh-autosuggestions"):
        subprocess.run(["git", "clone", "https://github.com/zsh-users/zsh-autosuggestions", "~/.oh-my-zsh/custom/plugins/zsh-autosuggestions"])

# Configurar Zsh y Oh My Zsh
def configure_zsh():
    zshrc_content = """
    # Coloca aquí tu configuración de Zsh y Oh My Zsh
    """
    
    with open("~/.zshrc", "w") as zshrc_file:
        zshrc_file.write(zshrc_content)

# Ejecutar las funciones para instalar y configurar
if __name__ == "__main__":
    install_zsh()
    install_oh_my_zsh()
    install_zsh_autosuggestions()
    configure_zsh()

    print("Configuración completada. Reinicia la terminal para aplicar los cambios.")
