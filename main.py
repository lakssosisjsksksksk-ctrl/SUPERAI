#!/usr/bin/env python3
"""
SUPER BOT MODPACK ULTRA - Versão 1.0.0 Final
Cria Minecraft modpacks automaticamente via API Modrinth

Uso: python main.py
"""

import sys
import os

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.dirname(__file__))

from checker import DependencyChecker, EnvironmentValidator
from superbot_gui import SuperBot


def main():
    """Função principal da aplicação."""
    
    print("\n" + "="*60)
    print("🔥 SUPER BOT MODPACK ULTRA v1.0.0")
    print("="*60 + "\n")
    
    # Verifica dependências
    print("🔍 Verificando dependências...")
    deps_ok, messages = DependencyChecker.check_all_dependencies()
    
    for msg in messages:
        print(f"  {msg}")
    
    if not deps_ok:
        print("\n❌ Dependências faltando!")
        print("   Execute: pip install -r requirements.txt")
        return 1
    
    print("\n✓ Dependências OK\n")
    
    # Valida ambiente
    print("🔍 Validando ambiente...")
    if not EnvironmentValidator.validate_all():
        print("❌ Problemas no ambiente detectados!")
        return 1
    
    print("✓ Ambiente OK\n")
    
    # Inicia aplicação
    print("🚀 Iniciando SUPER BOT MODPACK...\n")
    
    try:
        app = SuperBot()
        app.mainloop()
    except KeyboardInterrupt:
        print("\n\n⏹️  Aplicação encerrada pelo usuário")
        return 0
    except Exception as e:
        print(f"\n❌ Erro ao executar aplicação: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    print("✓ Aplicação encerrada com sucesso")
    return 0


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
