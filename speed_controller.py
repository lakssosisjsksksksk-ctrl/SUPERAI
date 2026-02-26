"""
Speed Controller para gerenciar a velocidade de downloads
"""

import time


class SpeedController:
    """
    Controlador de velocidade para limitar e monitorar a taxa de download.
    
    Atributos:
        max_speed (int): Velocidade máxima em KB/s (None = ilimitado)
        chunk_size (int): Tamanho do chunk em bytes
    """

    def __init__(self, max_speed=None, chunk_size=8192):
        """
        Inicializa o controlador de velocidade.
        
        Args:
            max_speed (int): Velocidade máxima em KB/s. None para ilimitado
            chunk_size (int): Tamanho do chunk em bytes
        """
        self.max_speed = max_speed  # em KB/s
        self.chunk_size = chunk_size
        self.last_time = time.time()
        self.bytes_downloaded = 0

    def throttle(self, bytes_amount):
        """
        Limita a velocidade de download baseado no tempo decorrido.
        
        Args:
            bytes_amount (int): Quantidade de bytes baixados no último chunk
        """
        if self.max_speed is None:
            return

        self.bytes_downloaded += bytes_amount
        elapsed = time.time() - self.last_time

        # Calcula a velocidade atual em KB/s
        if elapsed > 0:
            current_speed = (self.bytes_downloaded / 1024) / elapsed

            # Se a velocidade exceder o limite, aguarda
            if current_speed > self.max_speed:
                # Tempo que deveria levar para baixar esse volume na velocidade máxima
                time_needed = (self.bytes_downloaded / 1024) / self.max_speed
                sleep_time = time_needed - elapsed

                if sleep_time > 0:
                    time.sleep(sleep_time)

                # Reseta o contador
                self.last_time = time.time()
                self.bytes_downloaded = 0

    def reset(self):
        """Reseta o controlador para começar um novo download."""
        self.last_time = time.time()
        self.bytes_downloaded = 0

    def set_max_speed(self, speed):
        """
        Define a velocidade máxima de download.
        
        Args:
            speed (int): Velocidade em KB/s, ou None para ilimitado
        """
        self.max_speed = speed
        self.reset()

    def get_current_speed(self, total_bytes, elapsed_time):
        """
        Calcula a velocidade atual do download.
        
        Args:
            total_bytes (int): Total de bytes baixados
            elapsed_time (float): Tempo decorrido em segundos
        
        Returns:
            float: Velocidade em MB/s
        """
        if elapsed_time <= 0:
            return 0
        return (total_bytes / 1024 / 1024) / elapsed_time


class SpeedPresets:
    """Presets de velocidade para diferentes modos."""
    
    UNLIMITED = None
    SLOW = 512       # 512 KB/s
    NORMAL = 2048    # 2 MB/s
    FAST = 5120      # 5 MB/s
    TURBO = None     # Ilimitado

    @staticmethod
    def get_speed(mode):
        """
        Retorna a velocidade para um modo específico.
        
        Args:
            mode (str): 'Slow', 'Normal', 'Fast', 'Turbo'
        
        Returns:
            int: Velocidade em KB/s ou None
        """
        modes = {
            'Slow': SpeedPresets.SLOW,
            'Normal': SpeedPresets.NORMAL,
            'Fast': SpeedPresets.FAST,
            'Turbo': SpeedPresets.TURBO
        }
        return modes.get(mode, SpeedPresets.NORMAL)
