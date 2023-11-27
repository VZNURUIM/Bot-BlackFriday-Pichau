import subprocess

libraries = ['pyautogui', 'opencv-python']

for lib in libraries:
    try:
        subprocess.check_call(['pip', 'install', lib])
        print(f'Successfully installed {lib}')
        exit()
    except subprocess.CalledProcessError as e:
        print(f'Failed to install {lib}: {e}')
        exit()
