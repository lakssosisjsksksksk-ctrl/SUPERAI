@echo off
REM Script de inicialização para Windows
REM SUPER BOT MODPACK ULTRA

cls
echo.
echo ============================================================
echo   SUPER BOT MODPACK ULTRA - Iniciador Windows
echo ============================================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ERRO: Python nao encontrado!
    echo.
    echo Por favor instale Python 3.8+ em:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado
echo.

REM Verifica se requirements.txt existe
if not exist "requirements.txt" (
    echo ERRO: requirements.txt nao encontrado
    echo Certifique-se de estar no diretorio correto
    pause
    exit /b 1
)

echo [OK] requirements.txt encontrado
echo.

REM Instala dependências se necessário
echo Verificando dependências...
python -c "import customtkinter" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo Instalando dependências...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo.
        echo ERRO ao instalar dependências
        pause
        exit /b 1
    )
)

echo [OK] Todas as dependências estao OK
echo.

REM Executa a aplicação
echo Iniciando SUPER BOT MODPACK...
echo.
python main.py

if %errorlevel% neq 0 (
    echo.
    echo ERRO ao executar a aplicacao
    echo.
    pause
)

exit /b %errorlevel%
