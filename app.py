#!/usr/bin/env python3
"""
Img-gen — Web UI (Flask)
Run: python app.py
Then open http://localhost:5000 in your browser.
Upload images via the web UI and download the transparent PNGs instantly.
"""

import io
import os
from pathlib import Path

from flask import Flask, render_template, request, send_file, jsonify
from PIL import Image
from rembg import remove

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024  # 20 MB max upload

SUPPORTED = {"image/jpeg", "image/png", "image/webp", "image/bmp", "image/tiff"}
UPLOAD_FOLDER = Path("output")
UPLOAD_FOLDER.mkdir(exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/remove", methods=["POST"])
def remove_bg():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]
    if file.mimetype not in SUPPORTED:
        return jsonify({"error": f"Unsupported file type: {file.mimetype}"}), 400

    try:
        input_data = file.read()
        output_data = remove(input_data)

        output_filename = Path(file.filename).stem + "_nobg.png"
        output_path = UPLOAD_FOLDER / output_filename
        output_path.write_bytes(output_data)

        return send_file(
            io.BytesIO(output_data),
            mimetype="image/png",
            as_attachment=True,
            download_name=output_filename,
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀  Img-gen Web UI running at http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
