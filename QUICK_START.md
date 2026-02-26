# ⚡ Quick Start - SUPER BOT MODPACK ULTRA

## 🚀 Comece em 30 Segundos

### Windows (Mais Fácil)

**Basta dar duplo clique em:**
```
run.bat
```

Pronto! A aplicação abre automaticamente.

---

### Linux / macOS

**Terminal:**
```bash
chmod +x run.sh
./run.sh
```

---

### Modo Manual (Qualquer SO)

```bash
# 1. Instale dependências
pip install -r requirements.txt

# 2. Execute
python main.py
```

---

## 📖 Como Usar

Após abrir a aplicação:

1. **Escolha uma categoria** 📦
   - tech (mods de tecnologia)
   - magic (mods de magia)
   - adventure (mods de aventura)

2. **Ajuste a quantidade** ⚙️
   - Use o slider: 10 a 200 mods
   - Padrão: 90 mods

3. **Selecione velocidade** ⚡
   - **Slow** (512 KB/s) - para conexões lentas
   - **Normal** (2 MB/s) - recomendado ⭐
   - **Fast** (5 MB/s) - para conexões rápidas
   - **Turbo** (Ilimitado) - máxima velocidade

4. **Clique em "🚀 Criar Modpack"** para iniciar

5. **Acompanhe o progresso:**
   - Barra visual
   - Velocidade em tempo real
   - Tempo restante

6. **Para parar:** Clique em "⛔ Parar" a qualquer momento

---

## 📁 Onde Encontrar os Mods?

Após concluir:

```
C:\Users\seu-usuario\Downloads\
  └─ Modpack-1.21.1-neoforge-[categoria]/
     └─ mods/
        ├─ mod1.jar
        ├─ mod2.jar
        └─ ... mais mods
```

---

## ⚙️ Customizações Rápidas

### Trocar Cores

Abra `config.py` e altere:
```python
COLORS = {
    "title": "#seu_hex_color",  # Cor do título
    "button_primary": "#seu_hex_color",  # Botão
    ...
}
```

### Trocar Velocidades

Em `config.py`:
```python
SPEED_MODES = {
    "Slow": 256,      # Seu valor em KB/s
    "Normal": 1024,
    "Fast": 3072,
    "Turbo": None
}
```

### Trocar Tema

Em `config.py`:
```python
APPEARANCE_MODE = "light"  # ou "dark"
```

---

## 🆘 Problema com Dependências?

Se a instalação falhar:

```bash
# Limpar cache pip
pip cache purge

# Reinstalar
pip install -r requirements.txt --force-reinstall

# Ou individual
pip install customtkinter requests
```

---

## 📊 Diagnóstico

Ter problema?

```bash
python checker.py
```

Isso vai mostrar todos os detalhes do seu ambiente.

---

## 📚 Saiba Mais

- **README.md** - Documentação completa
- **INSTALLATION.md** - Guia de instalação
- **PROJECT_SUMMARY.md** - Resumo executivo

---

## ✅ Tudo Pronto?

```bash
python main.py
```

Ou no Windows, simplesmente: `run.bat`

---

**Divirta-se criando modpacks! 🔥**
