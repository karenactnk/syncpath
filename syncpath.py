import os
import subprocess
import sys

class SyncPath:
    def __init__(self, script_path):
        self.script_path = script_path
        self.current_directory = os.getcwd()

    def compile_script(self):
        try:
            print(f"Compiling the script: {self.script_path}")
            # Assuming the script is a Python script, we "compile" it by checking syntax
            subprocess.check_call([sys.executable, '-m', 'py_compile', self.script_path])
            print("Compilation successful.")
        except subprocess.CalledProcessError as e:
            print("Compilation failed. Please check the script for errors.")
            print(e)

    def run_script(self):
        try:
            print(f"Running the script: {self.script_path}")
            subprocess.check_call([sys.executable, self.script_path])
            print("Script executed successfully.")
        except subprocess.CalledProcessError as e:
            print("Script execution failed.")
            print(e)

    def change_directory(self, path):
        try:
            os.chdir(path)
            print(f"Changed directory to: {path}")
        except FileNotFoundError:
            print("Directory not found. Please check the path and try again.")

    def reset_directory(self):
        os.chdir(self.current_directory)
        print(f"Reset directory to original: {self.current_directory}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python syncpath.py <script_path>")
        sys.exit(1)

    script_path = sys.argv[1]
    sync_path = SyncPath(script_path)

    # Example workflow
    sync_path.compile_script()
    sync_path.run_script()
    sync_path.reset_directory()

if __name__ == "__main__":
    main()