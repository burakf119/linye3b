# Linye 3B - Windows baslatici
# Linye3B.html dosyasini kendi penceresinde (Edge ya da Chrome uygulama modu) acar.
import os
import pathlib
import shutil
import subprocess
import sys
import webbrowser


def main():
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    src = os.path.join(base, "Linye3B.html")
    data_dir = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "Linye3B")
    os.makedirs(data_dir, exist_ok=True)
    dst = os.path.join(data_dir, "Linye3B.html")
    shutil.copyfile(src, dst)
    url = pathlib.Path(dst).as_uri()

    roots = [os.environ.get("ProgramFiles(x86)", ""), os.environ.get("ProgramFiles", ""), os.environ.get("LOCALAPPDATA", "")]
    names = [r"Microsoft\Edge\Application\msedge.exe", r"Google\Chrome\Application\chrome.exe"]
    for name in names:
        for root in roots:
            exe = os.path.join(root, name) if root else ""
            if exe and os.path.exists(exe):
                subprocess.Popen([exe, "--app=" + url, "--window-size=1400,900"])
                return
    webbrowser.open(url)


if __name__ == "__main__":
    main()
