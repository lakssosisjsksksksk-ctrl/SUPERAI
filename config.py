"""
Configurações da aplicação SUPER BOT MODPACK
"""

# ============================================================
# CONFIGURAÇÕES DE INTERFACE
# ============================================================

# Tema
APPEARANCE_MODE = "dark"      # "dark" ou "light"
COLOR_THEME = "blue"          # Tema de cores

# Janela
WINDOW_TITLE = "SUPER BOT MODPACK ULTRA"
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
WINDOW_RESIZABLE = False

# ============================================================
# CONFIGURAÇÕES DE CORES
# ============================================================

COLORS = {
    "title": "#1f6ef1",        # Azul para título
    "frame_bg": "#212121",     # Fundo dos frames
    "text_primary": "#ffffff", # Texto principal
    "text_secondary": "#888888",  # Texto secundário
    "button_primary": "#1f6ef1",  # Cor principal do botão
    "button_primary_hover": "#1555d4",  # Hover do botão
    "button_stop": "#d63031",  # Cor do botão parar
    "button_stop_hover": "#c92a2a",  # Hover do botão parar
}

# ============================================================
# CONFIGURAÇÕES DE MINECRAFT
# ============================================================

# Versão padrão
DEFAULT_MINECRAFT_VERSION = "1.21.1"
DEFAULT_LOADER = "neoforge"

# Categorias de mods disponíveis
MOD_CATEGORIES = ["tech", "magic", "adventure"]

# ============================================================
# CONFIGURAÇÕES DE SLIDER
# ============================================================

MOD_SLIDER_MIN = 10
MOD_SLIDER_MAX = 200
MOD_SLIDER_DEFAULT = 90
MOD_SLIDER_STEPS = 19

# ============================================================
# CONFIGURAÇÕES DE VELOCIDADE
# ============================================================

SPEED_MODES = {
    "Slow": 512,      # 512 KB/s
    "Normal": 2048,   # 2 MB/s
    "Fast": 5120,     # 5 MB/s
    "Turbo": None     # Ilimitado
}

DEFAULT_SPEED_MODE = "Normal"
EXTRA_DELAY_SLOW_MODE = 0.2  # Delay adicional em modo Slow (segundos)

# ============================================================
# CONFIGURAÇÕES DE DOWNLOAD
# ============================================================

CHUNK_SIZE = 8192  # Tamanho dos chunks de download
MODRINTH_API_BASE = "https://api.modrinth.com/v2"
TIMEOUT_REQUEST = 10  # Timeout em segundos

# ============================================================
# CONFIGURAÇÕES DE CAMINHOS
# ============================================================

import os
BASE_PATH = os.path.join(os.path.expanduser("~"), "Downloads")
MODPACK_FOLDER_TEMPLATE = "Modpack-{version}-{loader}-{category}"
MODS_SUBFOLDER = "mods"

# ============================================================
# CONFIGURAÇÕES DE TIPOGRAFIA
# ============================================================

FONTS = {
    "title": ("Arial", 32, "bold"),
    "section_title": ("Arial", 13, "bold"),
    "label": ("Arial", 12),
    "button": ("Arial", 14, "bold"),
    "info": ("Arial", 12),
    "info_small": ("Arial", 11),
}

# ============================================================
# CONFIGURAÇÕES DE LAYOUT
# ============================================================

PADDING = {
    "main": (20, 20),      # Padding principal
    "frame": (15, 15),     # Padding dos frames
    "element": (15, 8),    # Padding dos elementos
}

# ============================================================
# MENSAGENS
# ============================================================

MESSAGES = {
    "waiting": "Status: esperando comando",
    "searching": "Buscando mods...",
    "downloading": "Baixando {current}/{total}",
    "completed": "🔥 MODPACK FINALIZADO!",
    "cancelled": "⏹️ Download cancelado",
    "api_error": "Erro na API",
    "speed_format": "Velocidade: {speed:.2f} MB/s",
    "time_format": "Tempo restante: {time}s",
}

# ============================================================
# VERSÕES SUPORTADAS
# ============================================================

SUPPORTED_VERSIONS = ["1.21.1"]  # Versões Minecraft suportadas
SUPPORTED_LOADERS = ["neoforge"]  # Loaders suportados
