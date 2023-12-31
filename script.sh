#!/bin/bash

# Instalar Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Clonar el repositorio de Zsh Autosuggestions
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions

# Agregar "zsh-autosuggestions" al archivo ~/.zshrc
echo 'plugins=(git zsh-autosuggestions)' >> ~/.zshrc

# Cambiar la shell predeterminada a Zsh
chsh -s $(which zsh)

echo "Oh My Zsh y Zsh Autosuggestions se han instalado y configurado correctamente, y Zsh se ha establecido como la shell predeterminada."

