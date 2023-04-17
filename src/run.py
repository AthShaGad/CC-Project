import os
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[-1] == "--test":
        sys.exit(0)
    else:
        os.system("streamlit run app.py")