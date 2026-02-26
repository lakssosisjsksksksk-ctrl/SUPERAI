A modern and intuitive GUI application to create Minecraft modpacks automatically through the Modrinth API.

## ✨ Features

- **Modern Interface**: Built with CustomTkinter for a premium visual experience
- **Smart Download**: Speed control system with 4 different modes
- **Real-Time Progress**: Monitor speed, remaining time, and progress
- **Safe Shutdown**: Cancel downloads at any time
- **Multiple Categories**: Choose from tech, magic, adventure
- **Flexibility**: Configure mod quantity (10-200)

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Steps

1. **Clone or download the project**
```bash
cd your-directory
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Run the Application

```bash
python superbot_gui.py
```

### Steps to Create a Modpack

1. **Select the Category**: tech, magic, or adventure
2. **Configure the Quantity**: Use the slider to choose between 10-200 mods
3. **Choose the Mode**: 
   - **Slow** (512 KB/s) - Slow connection
   - **Normal** (2 MB/s) - Recommended default
   - **Fast** (5 MB/s) - Fast connection
   - **Turbo** (Unlimited) - Maximum speed
4. **Click "Create Modpack"** to start the download
5. **Use "Stop"** if you need to cancel at any time

Mods will be saved to: `C:\Users\your-user\Downloads\Modpack-{version}-{loader}-{category}`

## 📁 File Structure

```
.
├── superbot_gui.py          # Main application with GUI
├── speed_controller.py      # Speed control module
├── requirements.txt         # Project dependencies
└── README.md               # This file
```

## 🔧 Project Files

### superbot_gui.py
Main application containing:
- **SuperBot Class**: Manages the graphical interface
- Methods for download and progress control
- Modrinth API integration

### speed_controller.py
Speed control module:
- **SpeedController**: Limits and monitors download speed
- **SpeedPresets**: Pre-defined speed configurations

## 📊 Interface

The interface is divided into 4 main sections:

### 1. Settings
- Mod category selector
- Slider for mod quantity
- Performance mode menu

### 2. Progress
- Visual progress bar

### 3. Information
- Current download status
- Real-time speed (MB/s)
- Estimated remaining time

### 4. Action Buttons
- **Create Modpack**: Start the download
- **Stop**: Cancel the running download

## ⚡ Performance Modes

| Mode | Speed | Usage |
|------|-----------|-----|
| Slow | 512 KB/s | Very slow connections |
| Normal | 2 MB/s | General use (default) |
| Fast | 5 MB/s | Fast connections |
| Turbo | Unlimited | Maximum speed |

## 🌐 API Used

- **Modrinth API v2**: https://api.modrinth.com/v2/
- Search mods by category, version, and loader
- Supports Minecraft 1.21.1 with NeoForge

## 📝 Version

**Version**: 1.0.0 Final  
**Date**: February 26, 2026  
**Status**: Complete and Tested

## 🎯 Features by Version

### v1.0.0 (Current)
- ✅ Modern GUI interface
- ✅ Mod downloads via Modrinth API
- ✅ Speed control with 4 levels
- ✅ Real-time progress
- ✅ Safe download shutdown
- ✅ Multiple categories
- ✅ Complete documentation

## 🐛 Troubleshooting

### API connection error
- Check your internet connection
- Try again later
- Modrinth API may be temporarily unavailable

### Very slow downloads
- Switch to "Fast" or "Turbo" mode
- Check your internet connection
- Try during off-peak hours

### Application won't open
- Confirm Python 3.8+ is installed
- Run `pip install -r requirements.txt` again
- Check write permissions in the Downloads folder

## 📞 Support

To report bugs or suggest improvements, check the application logs or consult the code documentation.

## 📄 License

This project is provided as-is for personal use.

---

**🔥 Developed with ❤️ for Minecraft gamers**

