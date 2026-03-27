# img-gen

A background removal tool that runs entirely in the browser. No server, no uploads, no account — images are processed locally using WebGPU or WASM.

![desktop screenshot](static/screenshot-desktop.png)

---

## How it works

The app loads [RMBG-1.4](https://huggingface.co/briaai/RMBG-1.4) (BiRefNet-lite) as an ONNX model and runs inference client-side via [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html). On supported browsers (Chrome 113+), it uses the WebGPU execution provider for GPU-accelerated inference. It falls back to WASM on other browsers.

The model is downloaded once (~170 MB) and cached by the browser. Subsequent uses load instantly.

---

## Features

- Runs fully offline after first model load
- WebGPU acceleration on Chrome — WASM CPU fallback elsewhere
- Drag and drop or click to upload
- Side-by-side original / result preview
- One-click PNG download with transparency
- No install, no Python, no dependencies

---

## Screenshots

![desktop](static/screenshot-desktop.png)
![mobile](static/screenshot-mobile.png)

---

## Usage

**Option 1 — Use the hosted version**

Open the deployed site in Chrome for best performance.

**Option 2 — Run locally**

```bash
git clone https://github.com/YashasVM/Img-gen.git
cd Img-gen

# Serve with any static server — file:// won't work due to CORS on the model fetch
npx serve .
# or
python -m http.server 8080
```

Then open `http://localhost:8080` in Chrome.

> Note: The app must be served over HTTP (not opened as a file) because the browser blocks cross-origin model fetches from `file://` URLs.

---

## Browser support

| Browser | WebGPU | WASM fallback |
|---|---|---|
| Chrome 113+ | yes | yes |
| Edge 113+ | yes | yes |
| Firefox | no | yes |
| Safari 17+ | partial | yes |

WebGPU is significantly faster (3-10x depending on GPU). WASM still works but is slower on large images.

---

## Technical details

- Model: RMBG-1.4 by BRIA AI, converted to ONNX
- Input: 1024x1024 normalized RGB tensor
- Output: single-channel alpha mask, normalized and applied to original resolution
- Runtime: ONNX Runtime Web 1.20.1

---

## Stack

- Vanilla HTML / CSS / JS — no framework
- ONNX Runtime Web (CDN)
- RMBG-1.4 ONNX model (HuggingFace)
- JetBrains Mono + Satoshi

---

## License

MIT

---

<a href="https://github.com/YashasVM/I" target="_blank" rel="noopener noreferrer">Created with love.</a>
