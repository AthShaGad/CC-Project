import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))
os.chdir("../")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[-1] == "--run":
        os.system("nohup python3 -m streamlit run src/app.py")
    else:
        sys.exit(0)
