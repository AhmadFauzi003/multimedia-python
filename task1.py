import pygame
import PIL
import cv2
import moviepy.editor as mp
import pkg_resources
import tkinter as tk

def check_installation():
    # Pygame
    try:
        print("✅ Pygame version:", pygame.__version__)
    except AttributeError:
        print("❌ Pygame version not found")
    
    # Pillow
    try:
        print("✅ Pillow version:", PIL.__version__)
    except AttributeError:
        print("❌ Pillow version not found")
    
    # OpenCV
    try:
        print("✅ OpenCV version:", cv2.__version__)
    except AttributeError:
        print("❌ OpenCV version not found")
    
    # MoviePy
    try:
        moviepy_version = pkg_resources.get_distribution("moviepy").version
        print("✅ MoviePy version:", moviepy_version)
    except pkg_resources.DistributionNotFound:
        print("❌ MoviePy is not installed")
    
    # Pydub
    try:
        pydub_version = pkg_resources.get_distribution("pydub").version
        print("✅ Pydub version:", pydub_version)
    except pkg_resources.DistributionNotFound:
        print("❌ Pydub is not installed")
    
    # Tkinter
    try:
        root = tk.Tk()
        root.title("Tkinter Test")
        root.geometry("200x100")
        label = tk.Label(root, text="Tkinter is working!")
        label.pack()
        root.update()
        print("✅ Tkinter is installed and working!")
        root.destroy()
    except tk.TclError:
        print("❌ Tkinter is not installed or not working")

if __name__ == "__main__":
    check_installation()
