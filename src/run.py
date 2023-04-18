import os
import sys
import subprocess

os.chdir(os.path.dirname(sys.argv[0]))
os.chdir("../")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[-1] == "--run":
        process = subprocess.Popen(["python3", "-m", "streamlit", "run", "src/app.py"], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        sys.exit(0)
