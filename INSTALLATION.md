# 📋 Guia de Instalação - SUPER BOT MODPACK ULTRA

## 🔧 Requisitos Mínimos

- **Python**: 3.8 ou superior
- **Sistema Operacional**: Windows, macOS ou Linux
- **Conexão com Internet**: Obrigatória (para download de mods)
- **Espaço em Disco**: Mínimo 500MB para modpacks grandes

## 📥 Instalação Passo a Passo

### 1. Instalação do Python

**Windows:**
- Baixe em: https://www.python.org/downloads/
- Durante a instalação, **IMPORTANTE**: marque "Add Python to PATH"
- Verifique: `python --version`

**macOS:**
```bash
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3 python3-pip
```

### 2. Clonar/Baixar o Projeto

**Via Git:**
```bash
git clone seu-repositorio
cd superbot-modpack
```

**Ou manualmente:**
- Baixe os arquivos
- Extraia em uma pasta

### 3. Instalar Dependências

```bash
# Navegue até a pasta do projeto
cd caminho/para/superbot-modpack

# Instale as dependências
pip install -r requirements.txt
```

**Saída esperada:**
```
Successfully installed customtkinter-5.x.x requests-2.x.x
```

## 🚀 Executar a Aplicação

### Opção 1: Usando main.py (Recomendado)
```bash
python main.py
```

### Opção 2: Direto com superbot_gui.py
```bash
python superbot_gui.py
```

### Opção 3: Executável (Windows)
Você pode criar um executável Windows com PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

O executável estará em `dist/main.exe`

## ✅ Verificação de Instalação

Execute o verificador de dependências:

```bash
python checker.py
```

Saída esperada:
```
==================================================
VERIFICAÇÃO DE DEPENDÊNCIAS
==================================================
Python: 3.8+ - OK
✓ customtkinter>=5.2.0
✓ requests>=2.31.0
==================================================

✓ Todas as dependências estão OK!
```

## 🔑 Variáveis de Ambiente (Opcional)

Você pode configurar variáveis de ambiente para customizar a aplicação:

```bash
# Windows PowerShell
$env:SUPERBOT_LOG_DIR = "C:\Logs"

# Windows CMD
set SUPERBOT_LOG_DIR=C:\Logs

# Linux/macOS
export SUPERBOT_LOG_DIR="/home/user/logs"
```

## 🐛 Resolvendo Problemas

### Erro: "No module named 'customtkinter'"

**Solução:**
```bash
pip install --upgrade customtkinter
```

### Erro: "No module named 'requests'"

**Solução:**
```bash
pip install requests
```

### Erro: "ModuleNotFoundError" ao executar

**Solução:** Certifique-se de estar no diretório correto:
```bash
cd /caminho/correto/do/projeto
python main.py
```

### Aplicação não abre (Windows)

1. Abra PowerShell como administrador
2. Execute: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
3. Tente novamente: `python main.py`

### Downloads muito lentos

- Use o modo "Fast" ou "Turbo" na interface
- Verifique sua conexão com internet
- Tente em outro horário (menos congestionado)

### Erro na API Modrinth

- Verifique conexão com internet
- A API pode estar temporariamente indisponível
- Tente novamente em alguns minutos

## 📚 Arquitetura do Projeto

```
superbot-modpack/
├── main.py                 # Ponto de entrada (verificações + GUI)
├── superbot_gui.py        # Interface gráfica principal
├── speed_controller.py    # Controlador de velocidade
├── config.py              # Configurações
├── logger.py              # Sistema de logs
├── checker.py             # Validação de ambiente
├── requirements.txt       # Dependências
├── README.md              # Documentação geral
└── INSTALLATION.md        # Este arquivo
```

## 🛠️ Configuração Avançada

### Editar Configurações

Abra `config.py` e customize:

```python
# Alterar tema
APPEARANCE_MODE = "light"  # ou "dark"

# Alterar cores
COLORS = {
    "title": "#seu_hex_color",
    ...
}

# Alterar velocidades
SPEED_MODES = {
    "Slow": 256,      # Reduzido
    "Normal": 1024,   # Normal
    "Fast": 3072,     # Mais rápido
    "Turbo": None     # Ilimitado
}
```

### Ativar Logging Detalhado

Os logs são salvos automaticamente em:
`C:\Users\seu-usuario\Downloads\SuperBot_Logs\`

Você pode acessar para análise de erros ou performance.

## 🌐 Testes de Conectividade

Para testar a conexão com Modrinth API:

```bash
python -c "import requests; print(requests.get('https://api.modrinth.com/v2').status_code)"
```

Esperado: `200`

## 📱 Requisitos de Sistema Recomendados

| Recurso | Mínimo | Recomendado |
|---------|--------|------------|
| CPU | Dual Core | Quad Core |
| RAM | 2GB | 4GB+ |
| Disco | 500MB | 2GB+ |
| Internet | 1 Mbps | 10+ Mbps |
| Tela | 800x600 | 1920x1080+ |

## 🔒 Segurança

- A aplicação **não coleta dados pessoais**
- Todos os downloads vêm do servidor oficial Modrinth
- Os mods são salvos em: `Downloads/Modpack-*/`
- Logs locais salvos em: `Downloads/SuperBot_Logs/`

## 📞 Suporte Técnico

Se encontrar problemas:

1. Verifique o arquivo de log em `SuperBot_Logs/`
2. Execute `python checker.py` para diagnóstico
3. Confirme que Python 3.8+ está instalado
4. Reinstale dependências: `pip install -r requirements.txt --force-reinstall`

## 🎉 Pronto!

Agora você pode executar:

```bash
python main.py
```

Divirta-se criando modpacks! 🔥

---

**Última atualização:** 26 de fevereiro de 2026  
**Versão:** 1.0.0 Final
