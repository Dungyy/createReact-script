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

# Ask the user whether they want to install npm packages
install_packages = input('Do you want to install npm packages? (y/n) ')

if install_packages == 'y':
    # Ask the user which npm packages to install
    packages = input('Enter the npm packages to install, separated by a space: ')

if install_packages == 'n':
    # exits the program
    process.__exit__


# Install the npm packages
os.system(f'npm install {packages}')
