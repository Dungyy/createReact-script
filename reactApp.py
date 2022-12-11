import os 
import subprocess
import shutil
import sys 

app_name = sys.argv[1]

# Creates a React App then waits after install

process = subprocess.Popen(f"npx create-react-app {app_name}", 
shell = True)
process.wait()

# change into current dir 

os.chdir(app_name)

# Path to files you would liked deleted. 

file_path = "src/index.css"
if os.path.exists(file_path):
    os.remove(file_path)

file_path = f"src/setupTests.js"
if os.path.exists(file_path):
    os.remove(file_path)

file_path = "src/reportWebVitals.js"
if os.path.exists(file_path):
    os.remove(file_path)

file_path = "src/App.test.js"
if os.path.exists(file_path):
    os.remove(file_path)    