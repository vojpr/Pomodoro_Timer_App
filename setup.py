"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
APP_NAME = "Pomodoro Timer"
DATA_FILES = ["tomato_2.png", "sound.mp3"]
OPTIONS = {
    'iconfile': 'tomato_2.icns',
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
