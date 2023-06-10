import subprocess

packages = [
    'opencv-python',
    'certifi',
    'chardet',
    'click',
    'cmake',
    'decorator',
    'dlib',
    'face-recognition',
    'face-recognition-models',
    'idna',
    'imageio',
    'imageio-ffmpeg',
    'moviepy',
    'numpy',
    'opencv-python',
    'Pillow',
    'proglog',
    'requests',
    'tqdm',
    'urllib3'
]

for package in packages:
    try:
        output = subprocess.check_output(['pip', 'show', package]).decode()
        print(f"{package} is installed")
    except subprocess.CalledProcessError:
        print(f"{package} is not installed")
