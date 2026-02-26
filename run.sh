#!/bin/bash
# Script de inicialização para Linux/macOS
# SUPER BOT MODPACK ULTRA

clear

echo ""
echo "============================================================"
echo "  SUPER BOT MODPACK ULTRA - Iniciador Unix"
echo "============================================================"
echo ""

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "ERRO: Python não encontrado!"
    echo ""
    echo "Por favor instale Python 3.8+"
    echo ""
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip"
        echo "  Fedora: sudo dnf install python3 python3-pip"
        echo "  Arch: sudo pacman -S python python-pip"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "  macOS: brew install python3"
    fi
    echo ""
    exit 1
fi

echo "[OK] Python encontrado"
echo ""

# Verifica se requirements.txt existe
if [ ! -f "requirements.txt" ]; then
    echo "ERRO: requirements.txt não encontrado"
    echo "Certifique-se de estar no diretório correto"
    exit 1
fi

echo "[OK] requirements.txt encontrado"
echo ""

# Instala dependências se necessário
echo "Verificando dependências..."
python3 -c "import customtkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo ""
    echo "Instalando dependências..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo ""
        echo "ERRO ao instalar dependências"
        exit 1
    fi
fi

echo "[OK] Todas as dependências estão OK"
echo ""

# Executa a aplicação
echo "Iniciando SUPER BOT MODPACK..."
echo ""
python3 main.py

exit_code=$?
if [ $exit_code -ne 0 ]; then
    echo ""
    echo "ERRO ao executar a aplicação (código: $exit_code)"
    echo ""
fi

exit $exit_code
