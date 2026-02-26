"""
Logger para a aplicação SUPER BOT MODPACK
Registra informações de download e operações
"""

import os
import time
from datetime import datetime


class Logger:
    """Classe para registrar eventos da aplicação."""
    
    def __init__(self, log_dir=None):
        """
        Inicializa o logger.
        
        Args:
            log_dir (str): Diretório para salvar logs
        """
        if log_dir is None:
            log_dir = os.path.join(os.path.expanduser("~"), "Downloads", "SuperBot_Logs")
        
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        
        self.log_file = os.path.join(
            log_dir,
            f"superbot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )
        
        self._write_log("=== SUPER BOT MODPACK INICIADO ===")
    
    def _write_log(self, message):
        """Escreve mensagem no arquivo de log."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}\n"
        
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_message)
        except Exception as e:
            print(f"Erro ao escrever log: {e}")
    
    def info(self, message):
        """Registra informação."""
        self._write_log(f"[INFO] {message}")
    
    def error(self, message):
        """Registra erro."""
        self._write_log(f"[ERROR] {message}")
    
    def warning(self, message):
        """Registra aviso."""
        self._write_log(f"[WARNING] {message}")
    
    def download_start(self, version, loader, category, mod_count):
        """Registra início do download."""
        self._write_log(
            f"[DOWNLOAD_START] Version: {version}, "
            f"Loader: {loader}, Category: {category}, Mods: {mod_count}"
        )
    
    def download_progress(self, current, total, speed, time_remaining):
        """Registra progresso do download."""
        self._write_log(
            f"[PROGRESS] {current}/{total} | "
            f"Speed: {speed:.2f} MB/s | Time: {time_remaining}s"
        )
    
    def download_complete(self, mod_count, total_size_mb, duration_seconds):
        """Registra conclusão do download."""
        self._write_log(
            f"[DOWNLOAD_COMPLETE] Mods: {mod_count}, "
            f"Size: {total_size_mb:.2f} MB, Duration: {duration_seconds}s"
        )
    
    def download_cancelled(self):
        """Registra cancelamento de download."""
        self._write_log("[DOWNLOAD_CANCELLED] Download cancelado pelo usuário")
    
    def api_error(self, error_message):
        """Registra erro da API."""
        self._write_log(f"[API_ERROR] {error_message}")
    
    def close(self):
        """Finaliza o logger."""
        self._write_log("=== SUPER BOT MODPACK ENCERRADO ===\n")
