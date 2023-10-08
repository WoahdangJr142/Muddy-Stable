import os
import sys

def restart_bot():
    python = sys.executable
    os.execl(python, python, "MuddyBot_Main.py")

if __name__ == "__main__":
    print("Restarting bot...")
    restart_bot()