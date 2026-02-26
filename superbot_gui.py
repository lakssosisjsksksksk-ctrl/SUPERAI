import customtkinter as ctk
import threading
import requests
import os
import time
from speed_controller import SpeedController, SpeedPresets

BASE_PATH = os.path.join(os.path.expanduser("~"), "Downloads")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SuperBot(ctk.CTk):
    """
    SuperBot: A GUI application for creating Minecraft modpacks.
    This class extends CustomTkinter (ctk.CTk) to provide a user interface for
    downloading and organizing Minecraft mods from the Modrinth API.
    Attributes:
        start_time (float): Timestamp marking the beginning of a download operation.
        total_bytes (int): Cumulative bytes downloaded during the current operation.
        category_menu (ctk.CTkOptionMenu): Dropdown for selecting mod category (tech, magic, adventure).
        mod_slider (ctk.CTkSlider): Slider for selecting the number of mods to download (10-200).
        speed_mode (ctk.CTkOptionMenu): Dropdown for selecting performance mode (Normal, Turbo).
        progress (ctk.CTkProgressBar): Progress bar showing download completion percentage.
        status (ctk.CTkLabel): Label displaying current operation status.
        speed_label (ctk.CTkLabel): Label displaying current download speed in MB/s.
        time_label (ctk.CTkLabel): Label displaying estimated remaining time.
    Methods:
        __init__(): Initializes the GUI with all widgets and settings.
        start_download(versao, loader): Initiates a mod download in a separate thread.
        baixar_mods(versao, loader, limite, categoria): Downloads mods from Modrinth API
            and saves them to the modpack directory, updating progress metrics in real-time.
    """

    def __init__(self):
        super().__init__()

        self.title("SUPER BOT MODPACK ULTRA")
        self.geometry("750x750")
        self.resizable(False, False)

        self.start_time = 0
        self.total_bytes = 0
        self.is_downloading = False
        self.stop_download_flag = False
        self.speed_controller = SpeedController()

        # Frame principal com padding
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Títílo
        title_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        title_frame.pack(fill="x", pady=(0, 30))
        
        ctk.CTkLabel(
            title_frame, 
            text="🔥 SUPER BOT MODPACK", 
            font=("Arial", 32, "bold"),
            text_color="#1f6ef1"
        ).pack(side="left")

        # Frame de configurações
        config_frame = ctk.CTkFrame(main_frame, corner_radius=10, fg_color="#212121")
        config_frame.pack(fill="x", pady=(0, 20))

        # Categoria
        cat_label = ctk.CTkLabel(
            config_frame, 
            text="📦 Categoria de Mods", 
            font=("Arial", 13, "bold")
        )
        cat_label.pack(anchor="w", padx=15, pady=(15, 8))

        self.category_menu = ctk.CTkOptionMenu(
            config_frame, 
            values=["tech", "magic", "adventure"],
            font=("Arial", 12),
            dropdown_font=("Arial", 12),
            height=35
        )
        self.category_menu.set("tech")
        self.category_menu.pack(fill="x", padx=15, pady=(0, 15))

        # Quantidade de Mods
        mod_label = ctk.CTkLabel(
            config_frame, 
            text="⚙️ Quantidade de Mods (10 - 200)", 
            font=("Arial", 13, "bold")
        )
        mod_label.pack(anchor="w", padx=15, pady=(15, 8))

        self.mod_slider = ctk.CTkSlider(
            config_frame, 
            from_=10, 
            to=200, 
            number_of_steps=19,
            height=6,
            button_length=20
        )
        self.mod_slider.set(90)
        self.mod_slider.pack(fill="x", padx=15, pady=(0, 5))

        slider_value_label = ctk.CTkLabel(
            config_frame,
            text="90 mods",
            font=("Arial", 11),
            text_color="#888888"
        )
        slider_value_label.pack(anchor="w", padx=15, pady=(0, 15))
        
        # Atualizar label do slider
        def update_slider_label(value):
            slider_value_label.configure(text=f"{int(value)} mods")
        
        self.mod_slider.configure(command=update_slider_label)

        # Modo performance
        speed_label = ctk.CTkLabel(
            config_frame, 
            text="⚡ Modo de Performance", 
            font=("Arial", 13, "bold")
        )
        speed_label.pack(anchor="w", padx=15, pady=(15, 8))

        self.speed_mode = ctk.CTkOptionMenu(
            config_frame, 
            values=["Slow", "Normal", "Fast", "Turbo"],
            font=("Arial", 12),
            dropdown_font=("Arial", 12),
            height=35
        )
        self.speed_mode.set("Normal")
        self.speed_mode.pack(fill="x", padx=15, pady=(0, 15))

        # Frame de progresso
        progress_frame = ctk.CTkFrame(main_frame, corner_radius=10, fg_color="#212121")
        progress_frame.pack(fill="x", pady=(0, 20))

        progress_title = ctk.CTkLabel(
            progress_frame,
            text="📊 Progresso",
            font=("Arial", 13, "bold")
        )
        progress_title.pack(anchor="w", padx=15, pady=(15, 10))

        self.progress = ctk.CTkProgressBar(progress_frame, height=8)
        self.progress.pack(fill="x", padx=15, pady=(0, 15))
        self.progress.set(0)

        # Frame de informações
        info_frame = ctk.CTkFrame(main_frame, corner_radius=10, fg_color="#212121")
        info_frame.pack(fill="x", pady=(0, 20))

        self.status = ctk.CTkLabel(
            info_frame, 
            text="Status: esperando comando",
            font=("Arial", 12),
            text_color="#888888"
        )
        self.status.pack(anchor="w", padx=15, pady=(12, 8))

        self.speed_label = ctk.CTkLabel(
            info_frame, 
            text="Velocidade: 0 MB/s",
            font=("Arial", 12),
            text_color="#888888"
        )
        self.speed_label.pack(anchor="w", padx=15, pady=(0, 8))

        self.time_label = ctk.CTkLabel(
            info_frame, 
            text="Tempo restante: --",
            font=("Arial", 12),
            text_color="#888888"
        )
        self.time_label.pack(anchor="w", padx=15, pady=(0, 12))

        # Botão
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(fill="x", pady=(10, 0))

        self.download_button = ctk.CTkButton(
            button_frame,
            text="🚀 Criar Modpack 1.21.1 NeoForge",
            command=lambda: self.start_download("1.21.1", "neoforge"),
            font=("Arial", 14, "bold"),
            height=45,
            corner_radius=8,
            hover_color="#1555d4"
        )
        self.download_button.pack(fill="x", side="left", expand=True, padx=(0, 5))

        self.stop_button = ctk.CTkButton(
            button_frame,
            text="⛔ Parar",
            command=self.stop_download,
            font=("Arial", 14, "bold"),
            height=45,
            corner_radius=8,
            fg_color="#d63031",
            hover_color="#c92a2a",
            state="disabled"
        )
        self.stop_button.pack(fill="x", side="left", expand=True, padx=(5, 0))

    def start_download(self, versao, loader):
        categoria = self.category_menu.get()
        limite = int(self.mod_slider.get())
        speed_mode = self.speed_mode.get()

        self.is_downloading = True
        self.stop_download_flag = False
        self.download_button.configure(state="disabled")
        self.stop_button.configure(state="normal")

        # Configura a velocidade conforme o modo selecionado
        max_speed = SpeedPresets.get_speed(speed_mode)
        self.speed_controller.set_max_speed(max_speed)

        threading.Thread(
            target=self.baixar_mods,
            args=(versao, loader, limite, categoria),
            daemon=True
        ).start()

    def stop_download(self):
        self.stop_download_flag = True
        self.status.configure(text="⏹️ Download cancelado pelo usuário")
        self.download_button.configure(state="normal")
        self.stop_button.configure(state="disabled")

    def baixar_mods(self, versao, loader, limite, categoria):

        pasta_modpack = os.path.join(BASE_PATH, f"Modpack-{versao}-{loader}-{categoria}")
        pasta_mods = os.path.join(pasta_modpack, "mods")
        os.makedirs(pasta_mods, exist_ok=True)

        self.start_time = time.time()
        self.total_bytes = 0

        speed_mode = self.speed_mode.get()
        add_extra_delay = speed_mode == "Slow"

        self.speed_controller.reset()
        self.status.configure(text="Buscando mods...")

        url = (
            f"https://api.modrinth.com/v2/search?"
            f"facets=[[\"categories:{loader}\"],[\"versions:{versao}\"],[\"categories:{categoria}\"]]"
            f"&limit={limite}"
        )

        response = requests.get(url)

        if response.status_code != 200:
            self.status.configure(text="Erro na API")
            return

        mods = response.json()["hits"]

        for i, mod in enumerate(mods):
            if self.stop_download_flag:
                break

            project_id = mod["project_id"]

            versoes = requests.get(
                f"https://api.modrinth.com/v2/project/{project_id}/version"
            ).json()

            for v in versoes:
                if versao in v["game_versions"] and loader in v["loaders"]:
                    arquivo = v["files"][0]

                    r = requests.get(arquivo["url"], stream=True)

                    file_path = os.path.join(pasta_mods, arquivo["filename"])
                    with open(file_path, "wb") as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                                self.total_bytes += len(chunk)
                                self.speed_controller.throttle(len(chunk))

                    break

            # 🔥 Atualiza métricas
            elapsed = time.time() - self.start_time
            speed = (self.total_bytes / 1024 / 1024) / elapsed if elapsed > 0 else 0

            restante = limite - (i + 1)
            tempo_estimado = restante * (elapsed / (i + 1)) if i > 0 else 0

            self.progress.set((i + 1) / limite)
            self.status.configure(text=f"Baixando {i+1}/{limite}")
            self.speed_label.configure(text=f"Velocidade: {speed:.2f} MB/s")
            self.time_label.configure(text=f"Tempo restante: {int(tempo_estimado)}s")

            if add_extra_delay:
                time.sleep(0.2)

        if self.stop_download_flag:
            self.status.configure(text="⏹️ Download cancelado")
        else:
            self.status.configure(text="🔥 MODPACK FINALIZADO!")
            self.progress.set(1)

        self.is_downloading = False
        self.download_button.configure(state="normal")
        self.stop_button.configure(state="disabled")


if __name__ == "__main__":
    app = SuperBot()
    app.mainloop()