import tkinter as tk
import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
white = 17  # Replaced red with white
green = 27  # Replaced blue with green
yellow = 22  # Replaced green with yellow

GPIO.setup(white, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)  # Changed from blue to green
GPIO.setup(yellow, GPIO.OUT)  # Changed from green to yellow

# PWM setup
whitepwm = GPIO.PWM(white, 1000)
greenpwm = GPIO.PWM(green, 1000)  # Changed from blue to green
yellowpwm = GPIO.PWM(yellow, 1000)  # Changed from green to yellow

whitepwm.start(0)
greenpwm.start(0)  # Changed from blue to green
yellowpwm.start(0)  # Changed from green to yellow

# GUI function to update LED intensities
def update_intensities(event):
    whiteintensity = int(whiteslider.get())
    greenintensity = int(greenslider.get())  # Changed from blue to green
    yellowintensity = int(yellowslider.get())  # Changed from green to yellow

    whitepwm.ChangeDutyCycle(whiteintensity)
    greenpwm.ChangeDutyCycle(greenintensity)  # Changed from blue to green
    yellowpwm.ChangeDutyCycle(yellowintensity)  # Changed from green to yellow

# GUI creation
root = tk.Tk()
root.title("LED Intensity Control")
root.geometry("400x200")
root.configure(bg="#f0f0f0")  # Light gray background

# Create a frame to center the sliders and buttons
slider_frame = tk.Frame(root, bg="#f0f0f0")  # Match the background color
slider_frame.pack(pady=10, expand=True)

# White LED intensity slider
whiteslider = tk.Scale(
    slider_frame,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    command=update_intensities,
    label="White",
    fg="black",
    bg="white",
    troughcolor="lightgray",
    font=("Arial", 10, "bold"),
)
whiteslider.grid(row=0, column=0, padx=10)

# Green LED intensity slider (changed from blue to green)
greenslider = tk.Scale(
    slider_frame,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    command=update_intensities,
    label="Green",
    fg="white",
    bg="green",
    troughcolor="lightgreen",
    font=("Arial", 10, "bold"),
)
greenslider.grid(row=0, column=1, padx=10)

# Yellow LED intensity slider (changed from green to yellow)
yellowslider = tk.Scale(
    slider_frame,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    command=update_intensities,
    label="Yellow",
    fg="black",
    bg="yellow",
    troughcolor="lightyellow",
    font=("Arial", 10, "bold"),
)
yellowslider.grid(row=0, column=2, padx=10)

# Exit button with black text
exitbutton = tk.Button(
    root,
    text="Exit",
    command=root.quit,
    fg="white",
    bg="#333333",  # Dark gray button
    font=("Arial", 12, "bold"),
    relief=tk.RAISED,
)
exitbutton.pack(pady=20)

# Center the main window
root.eval("tk::PlaceWindow . center")

# Start the GUI
root.mainloop()

# Cleanup GPIO
GPIO.cleanup()
