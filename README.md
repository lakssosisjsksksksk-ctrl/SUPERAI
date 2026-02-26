# 🔥 SUPER BOT MODPACK ULTRA

Uma aplicação GUI moderna e intuitiva para criar Minecraft modpacks automaticamente através da API Modrinth.

## ✨ Características

- **Interface Moderna**: Built com CustomTkinter para uma experiência visual premium
- **Download Inteligente**: Sistema de controle de velocidade com 4 modos diferentes
- **Progresso em Tempo Real**: Monitore velocidade, tempo restante e progresso
- **Parada Segura**: Cancele downloads a qualquer momento
- **Múltiplas Categorias**: Escolha entre tech, magic, adventure
- **Flexibilidade**: Configure quantidade de mods (10-200)

## 🚀 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip

### Passos

1. **Clone ou baixe o projeto**
```bash
cd seu-diretorio
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

## 💻 Uso

### Executar a Aplicação

```bash
python superbot_gui.py
```

### Passos para Criar um Modpack

1. **Selecione a Categoria**: tech, magic ou adventure
2. **Configure a Quantidade**: Use o slider para escolher entre 10-200 mods
3. **Escolha o Modo**: 
   - **Slow** (512 KB/s) - Conexão lenta
   - **Normal** (2 MB/s) - Padrão recomendado
   - **Fast** (5 MB/s) - Conexão rápida
   - **Turbo** (Ilimitado) - Máxima velocidade
4. **Clique em "Criar Modpack"** para iniciar o download
5. **Use "Parar"** se precisar cancelar em qualquer momento

Os mods serão salvos em: `C:\Users\seu-usuario\Downloads\Modpack-{versao}-{loader}-{categoria}`

## 📁 Estrutura de Arquivos

```
.
├── superbot_gui.py          # Aplicação principal com GUI
├── speed_controller.py      # Módulo de controle de velocidade
├── requirements.txt         # Dependências do projeto
└── README.md               # Este arquivo
```

## 🔧 Arquivos do Projeto

### superbot_gui.py
Aplicação principal que contém:
- **Classe SuperBot**: Gerencia a interface gráfica
- Métodos para download e controle de progresso
- Integração com API Modrinth

### speed_controller.py
Módulo de controle de velocidade:
- **SpeedController**: Limita e monitora a velocidade de download
- **SpeedPresets**: Configurações pré-definidas de velocidade

## 📊 Interface

A interface está dividida em 4 seções principais:

### 1. Configurações
- Seletor de categoria de mods
- Slider para quantidade de mods
- Menu de modo de performance

### 2. Progresso
- Barra de progresso visual

### 3. Informações
- Status atual do download
- Velocidade em tempo real (MB/s)
- Tempo restante estimado

### 4. Botões de Ação
- **Criar Modpack**: Inicia o download
- **Parar**: Cancela o download em andamento

## ⚡ Modos de Performance

| Modo | Velocidade | Uso |
|------|-----------|-----|
| Slow | 512 KB/s | Conexões muito lentas |
| Normal | 2 MB/s | Uso geral (padrão) |
| Fast | 5 MB/s | Conexões rápidas |
| Turbo | Ilimitado | Máxima velocidade |

## 🌐 API Utilizada

- **Modrinth API v2**: https://api.modrinth.com/v2/
- Busca mods por categoria, versão e carregador
- Suporta Minecraft 1.21.1 com NeoForge

## 📝 Versão

**Versão**: 1.0.0 Final  
**Data**: 26 de fevereiro de 2026  
**Status**: Completo e Testado

## 🎯 Funcionalidades por Versão

### v1.0.0 (Atual)
- ✅ Interface GUI moderna
- ✅ Download de mods via Modrinth API
- ✅ Controle de velocidade em 4 níveis
- ✅ Progresso em tempo real
- ✅ Parada segura de downloads
- ✅ Múltiplas categorias
- ✅ Documentação completa

## 🐛 Troubleshooting

### Erro de conexão com API
- Verifique sua conexão com internet
- Tente novamente mais tarde
- A API Modrinth pode estar temporariamente indisponível

### Downloads muito lentos
- Mude para o modo "Fast" ou "Turbo"
- Verifique sua conexão de internet
- Tente em horário de menor uso

### Aplicação não abre
- Confirme que Python 3.8+ está instalado
- Execute `pip install -r requirements.txt` novamente
- Verifique permissões de escrita na pasta Downloads

## 📞 Suporte

Para reportar bugs ou sugerir melhorias, verifique os logs da aplicação ou consulte a documentação do código.

## 📄 Licença

Este projeto é fornecido como está, para uso pessoal.

---

**🔥 Desenvolvido com ❤️ para gamers Minecraft**
