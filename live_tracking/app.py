import tinker as tk
import customtkinter as ck
import pandas as pd
import numpy as np
import pickle

import mediapipe as mp
import cv2
from PIL import Image, ImageTk

from landmarks import landmark

window = tk.Tk()
window.geometry("480x700")
window.title("Swoleboi")
ck.set_appearance_mode("dark")
window.mainloop()