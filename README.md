---
title: ArtifyAI
emoji: 🎨
colorFrom: purple
colorTo: pink
sdk: docker
app_port: 7860
pinned: false
license: mit
---

# 🎨 ArtifyAI — Neural Style Transfer

- Transform any photo into an art using deep learning.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.2.2-EE4C2C?style=flat-square&logo=pytorch)
![Flask](https://img.shields.io/badge/Flask-3.1.2-black?style=flat-square&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## ✨ What is ArtifyAI?

ArtifyAI is a web application that applies **Artistic Neural Style Transfer** to your photos. Upload any content image and a style reference (a painting, sketch, or artwork), and the AI will reimagine your photo in that artistic style — in seconds.

Built from scratch using **AdaIN (Adaptive Instance Normalization)**, a fast feed-forward style transfer method that doesn't require optimization at inference time.

---

## 🖼️ Examples
### Example 1

| Content | Output |
|--------|-------|
| ![Content](examples/input.png) | ![Output](examples/output.png) |

## 🧠 How It Works

ArtifyAI uses **AdaIN (Adaptive Instance Normalization)** — a technique that aligns the mean and variance of the content image's feature maps with those of the style image, effectively transferring the artistic style in a single forward pass.

```
Content Image ──┐
                ├──► VGG Encoder ──► AdaIN ──► Decoder ──► Stylized Image
Style Image ────┘
```

1. Both images are passed through a **pretrained VGG19 encoder** to extract feature maps
2. **AdaIN** normalizes the content features using the style's mean and standard deviation
3. A trained **decoder** reconstructs the stylized image from the transformed features
4. The **style strength (alpha)** parameter blends between full stylization and the original content

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ArtifyAI.git
cd ArtifyAI/code

# Create a virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r ../requirements.txt
```


### Run the App

```bash
python app.py
```

Then open **http://localhost:5000** in your browser.

---

## 🏋️ Training the Own Model

```bash
python train.py \
  --content_dir /path/to/content_images \
  --style_dir /path/to/style_images \
  --vgg vgg_normalised.pth \
  --experiment my_experiment \
  --epochs 20 \
  --batch_size 4 \
  --content_weight 1.0 \
  --style_weight 5.0
```

Key training arguments:

| Argument | Default | Description |
|----------|---------|-------------|
| `--epochs` | 1 | Number of training epochs |
| `--batch_size` | 4 | Batch size |
| `--lr` | 1e-5 | Learning rate |
| `--content_weight` | 1.0 | Weight for content loss |
| `--style_weight` | 5.0 | Weight for style loss |
| `--resume` | False | Resume from checkpoint |

---

## 📁 Project Structure

```
ArtifyAI/
├── code/
│   ├── app.py                  # Flask web application
│   ├── train.py                # Model training script
│   ├── vgg_normalised.pth      # VGG encoder weights
│   ├── templates/
│   │   └── index.html          # Frontend UI
│   ├── static/
│   │   └── uploads/            # Uploaded & generated images
│   ├── examples/               # Example images for the UI
│   ├── experiment/
│   │   └── final_exp/
│   │       └── decoder_final.pth  # Trained decoder weights
│   └── utils/
│       ├── models.py           # VGGEncoder & Decoder architecture
│       └── utils.py            # AdaIN, transforms, dataset
├── InputOuputImages/           # Sample input/output pairs
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Deep Learning | PyTorch 2.2.2 |
| Model Architecture | VGG19 + Custom Decoder |
| Style Transfer Method | AdaIN (Adaptive Instance Normalization) |
| Web Framework | Flask 3.1.2 |
| Frontend | HTML, CSS, Bootstrap 5 |
| Forms | Flask-WTF |
| Image Processing | Pillow, torchvision |

---

## 📖 References

- Huang, X., & Belongie, S. (2017). [Arbitrary Style Transfer in Real-time with Adaptive Instance Normalization](https://arxiv.org/abs/1703.06868). ICCV 2017.

---

## 👤 Author

**Your Name**
- GitHub: [@isushmeeta](https://github.com/isushmeeta)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
