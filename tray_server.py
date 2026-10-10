"""
SynapseLMS System Tray App
Runs the FastAPI server in the background and shows a tray icon.
Install deps: pip install pystray pillow
Run: python tray_server.py
"""
import sys
import os
import threading
import subprocess
import webbrowser
import time
from pathlib import Path

# Change to script directory
os.chdir(Path(__file__).parent)

try:
    import pystray
    from PIL import Image, ImageDraw
except ImportError:
    print("Installing tray dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pystray", "pillow", "-q"])
    import pystray
    from PIL import Image, ImageDraw

SERVER_URL = "http://127.0.0.1:8000"
server_process = None
server_running = False


def create_icon_image(color="#6C63FF"):
    """Create a simple circular tray icon."""
    size = 64
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
    draw.ellipse([4, 4, size - 4, size - 4], fill=(r, g, b, 255))
    # Letter S
    draw.text((22, 18), "S", fill=(255, 255, 255, 255))
    return img


def start_server():
    global server_process, server_running
    if server_running:
        return
    print("[Tray] Starting SynapseLMS server...")
    server_process = subprocess.Popen(
        [sys.executable, "main.py", "run"],
        creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
    )
    server_running = True
    # Wait for startup then open browser
    time.sleep(2)
    webbrowser.open(SERVER_URL)
    print(f"[Tray] Server running at {SERVER_URL}")


def stop_server():
    global server_process, server_running
    if server_process:
        server_process.terminate()
        server_process = None
    server_running = False
    print("[Tray] Server stopped.")


def on_open(icon, item):
    webbrowser.open(SERVER_URL)


def on_restart(icon, item):
    stop_server()
    time.sleep(1)
    threading.Thread(target=start_server, daemon=True).start()
    icon.icon = create_icon_image("#6C63FF")


def on_stop(icon, item):
    stop_server()
    icon.icon = create_icon_image("#888888")


def on_quit(icon, item):
    stop_server()
    icon.stop()


def main():
    # Start server immediately in background
    threading.Thread(target=start_server, daemon=True).start()

    icon_img = create_icon_image("#6C63FF")
    menu = pystray.Menu(
        pystray.MenuItem("🌐 Open SynapseLMS", on_open, default=True),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("▶ Restart Server", on_restart),
        pystray.MenuItem("⏹ Stop Server", on_stop),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("✖ Quit", on_quit),
    )
    icon = pystray.Icon("SynapseLMS", icon_img, "SynapseLMS Study System", menu)
    print("[Tray] SynapseLMS tray icon active. Right-click for options.")
    icon.run()


if __name__ == "__main__":
    main()
