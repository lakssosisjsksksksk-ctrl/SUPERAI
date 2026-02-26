"""
Verificador de dependências e validação de ambiente
"""

import sys
import importlib
import subprocess
from typing import Tuple, List


class DependencyChecker:
    """Verifica se todas as dependências estão instaladas."""
    
    REQUIRED_PACKAGES = {
        "customtkinter": "customtkinter>=5.2.0",
        "requests": "requests>=2.31.0",
    }
    
    @staticmethod
    def check_python_version() -> Tuple[bool, str]:
        """
        Verifica se a versão do Python é compatível.
        
        Returns:
            Tuple[bool, str]: (sucesso, mensagem)
        """
        required_version = (3, 8)
        current_version = sys.version_info[:2]
        
        if current_version >= required_version:
            return True, f"Python {current_version[0]}.{current_version[1]} - OK"
        else:
            return False, f"Python 3.8+ requerido (encontrado: {current_version[0]}.{current_version[1]})"
    
    @staticmethod
    def check_package(package_name: str) -> bool:
        """
        Verifica se um pacote está instalado.
        
        Args:
            package_name (str): Nome do pacote
        
        Returns:
            bool: True se instalado, False caso contrário
        """
        try:
            importlib.import_module(package_name)
            return True
        except ImportError:
            return False
    
    @classmethod
    def check_all_dependencies(cls) -> Tuple[bool, List[str]]:
        """
        Verifica todas as dependências.
        
        Returns:
            Tuple[bool, List[str]]: (todas_ok, mensagens)
        """
        messages = []
        all_ok = True
        
        # Verifica Python
        python_ok, python_msg = cls.check_python_version()
        messages.append(f"Python: {python_msg}")
        all_ok = all_ok and python_ok
        
        # Verifica pacotes
        for package_name, package_spec in cls.REQUIRED_PACKAGES.items():
            if cls.check_package(package_name):
                messages.append(f"✓ {package_spec}")
            else:
                messages.append(f"✗ {package_spec} - NÃO INSTALADO")
                all_ok = False
        
        return all_ok, messages
    
    @staticmethod
    def install_missing_packages() -> bool:
        """
        Instala pacotes faltantes.
        
        Returns:
            bool: True se sucesso, False se falhou
        """
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
            ])
            return True
        except subprocess.CalledProcessError:
            return False
    
    @staticmethod
    def print_status():
        """Imprime status das dependências."""
        checker = DependencyChecker()
        all_ok, messages = checker.check_all_dependencies()
        
        print("\n" + "="*50)
        print("VERIFICAÇÃO DE DEPENDÊNCIAS")
        print("="*50)
        for msg in messages:
            print(msg)
        print("="*50 + "\n")
        
        if not all_ok:
            print("❌ Dependências faltando!")
            print("\nTentando instalar automaticamente...")
            if checker.install_missing_packages():
                print("✓ Dependências instaladas com sucesso!")
                return True
            else:
                print("✗ Falha ao instalar dependências")
                print("Execute: pip install -r requirements.txt")
                return False
        else:
            print("✓ Todas as dependências estão OK!")
            return True


class EnvironmentValidator:
    """Valida o ambiente de execução."""
    
    @staticmethod
    def validate_downloads_folder() -> bool:
        """
        Valida se a pasta Downloads existe e é acessível.
        
        Returns:
            bool: True se válida, False caso contrário
        """
        import os
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        
        if not os.path.exists(downloads_path):
            print(f"⚠️  Pasta Downloads não encontrada: {downloads_path}")
            return False
        
        if not os.access(downloads_path, os.W_OK):
            print(f"⚠️  Sem permissão de escrita: {downloads_path}")
            return False
        
        return True
    
    @staticmethod
    def validate_internet_connection() -> bool:
        """
        Valida se há conexão com a internet.
        
        Returns:
            bool: True se há conexão, False caso contrário
        """
        try:
            import requests
            response = requests.get("https://api.modrinth.com/v2", timeout=5)
            return response.status_code == 200
        except Exception:
            return False
    
    @staticmethod
    def validate_all() -> bool:
        """
        Valida todo o ambiente.
        
        Returns:
            bool: True se válido, False caso contrário
        """
        print("\n" + "="*50)
        print("VALIDAÇÃO DE AMBIENTE")
        print("="*50)
        
        # Valida pasta Downloads
        if EnvironmentValidator.validate_downloads_folder():
            print("✓ Pasta Downloads OK")
        else:
            print("✗ Problema com pasta Downloads")
            return False
        
        print("="*50 + "\n")
        return True


def run_diagnostics():
    """Executa diagnósticos completos."""
    print("\n🔍 DIAGNOSTICANDO AMBIENTE...\n")
    
    # Verifica dependências
    deps_ok = DependencyChecker.print_status()
    
    # Valida ambiente
    env_ok = EnvironmentValidator.validate_all()
    
    if deps_ok and env_ok:
        print("✅ Ambiente pronto para executar a aplicação!")
        return True
    else:
        print("⚠️  Resolva os problemas acima antes de executar a aplicação")
        return False


if __name__ == "__main__":
    run_diagnostics()
