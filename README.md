# ✨ Img-gen — Free Background Remover

> Remove image backgrounds **100% locally** using AI — no subscriptions, no API keys, no data sent to any server.

Powered by [`rembg`](https://github.com/danielgatis/rembg) and the **U2Net** deep learning model.

---

## 🚀 Features

- **100% free** — no limits, no watermarks, no account needed
- **Runs offline** — your images never leave your machine
- **Two modes** — CLI (batch) and Web UI (single image, drag & drop)
- **Supports** JPG, PNG, WebP, BMP, TIFF
- **Outputs** transparent PNG files

---

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/yashasvm208/Img-gen.git
cd Img-gen
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> **Note:** The first run will automatically download the U2Net AI model (~170 MB). This happens once and is cached locally at `~/.u2net/`.

---

## 🖥️ Usage — CLI (Batch Mode)

Drop your images into the `input/` folder, then run:

```bash
python remove_bg.py
```

Processed images (transparent PNGs) will appear in the `output/` folder.

**Or pass specific files:**
```bash
python remove_bg.py photo1.jpg photo2.png
```

**Custom output directory:**
```bash
python remove_bg.py -o my_results/ photo.jpg
```

### Example output
```
🔍  Found 3 image(s) to process...

✅  photo1.jpg  →  output/photo1_nobg.png
✅  photo2.png  →  output/photo2_nobg.png
✅  selfie.jpg  →  output/selfie_nobg.png

🎉  Done! 3 succeeded, 0 failed.
📁  Results saved to: /home/user/Img-gen/output
```

---

## 🌐 Usage — Web UI

Start the local web server:

```bash
python app.py
```

Then open **http://localhost:5000** in your browser.

- Drag & drop or click to upload an image
- Click **Remove Background**
- Preview the result and download the transparent PNG

![Web UI screenshot](https://raw.githubusercontent.com/yashasvm208/Img-gen/main/static/preview.png)

---

## 📁 Project Structure

```
Img-gen/
├── remove_bg.py      # CLI batch processor
├── app.py            # Flask web UI server
├── requirements.txt  # Python dependencies
├── templates/
│   └── index.html    # Web UI frontend
├── input/            # Drop your images here (CLI mode)
└── output/           # Processed images saved here
```

---

## ⚙️ Requirements

- Python 3.8+
- ~170 MB disk space for the AI model (auto-downloaded on first run)
- No GPU required — runs on CPU

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open an issue for bugs or feature requests.

---

## 📄 License

MIT License — free for personal and commercial use.

---

Made with ❤️ using [rembg](https://github.com/danielgatis/rembg) by danielgatis.
