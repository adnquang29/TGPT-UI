# TGPT Web UI 🤖

A modern, responsive web interface for **[tgpt](https://github.com/aandrew-me/tgpt)** (Terminal GPT).  
This project creates a beautiful "Messenger-style" chat UI that runs locally or on your VPS, allowing you to use AI without API keys.

## ✨ Features

- **Zero API Keys:** Powered by `tgpt`, free to use.
- **Modern UI:** Clean, "Messenger-style" interface with bubbles.
- **Dark/Light Mode:** Toggle themes with one click (auto-saves preference).
- **Responsive:** Works perfectly on Desktop and Mobile (max-width optimized).
- **Clean Output:** Automatically filters out CLI loading animations and ANSI codes.

## 🛠️ Prerequisites

- **Python 3.x**
- **Linux/macOS** (Recommended) or Windows.
- **tgpt binary**: The core engine.

## 🚀 Installation

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/REPO_NAME.git](https://github.com/YOUR_USERNAME/REPO_NAME.git)
cd REPO_NAME
````

### 2\. Download `tgpt` binary

You need the `tgpt` executable in the project root folder.

**For Linux/macOS:**

```bash
curl -sL [https://github.com/aandrew-me/tgpt/releases/download/v2.8.0/tgpt-linux-amd64](https://github.com/aandrew-me/tgpt/releases/download/v2.8.0/tgpt-linux-amd64) -o tgpt
chmod +x tgpt
```

*(Note: Check the [tgpt releases](https://github.com/aandrew-me/tgpt/releases) for the latest version suitable for your OS).*

### 3\. Install Python dependencies

Create a virtual environment (recommended) and install Flask.

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
```

## 🏃‍♂️ Usage

1.  **Start the server:**

    ```bash
    python app.py
    ```

2.  **Access the UI:**

      - **Local:** Open `http://localhost:5000`
      - **Server/VPS:** Open `http://YOUR_SERVER_IP:5000`

    *(Make sure port 5000 is allowed in your firewall)*

## 📂 Project Structure

```
├── app.py              # Flask backend (handles subprocess & regex cleaning)
├── tgpt                # The executable binary (must be present)
├── templates
│   └── index.html      # Single-file Frontend (HTML/CSS/JS)
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

## 🔧 Troubleshooting

  - **"Server chưa cài đặt tgpt" / File Not Found:**
    Make sure the `tgpt` file is in the **same folder** as `app.py` and has execution permissions (`chmod +x tgpt`).

  - **Permission Denied:**
    Run `chmod +x tgpt` again.

## 🤝 Credits

  - **Core AI Tool:** [tgpt](https://github.com/aandrew-me/tgpt) by aandrew-me.
  - **UI/Wrapper:** Developed by You.

-----
