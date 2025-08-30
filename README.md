# Invisible_Cloak

A fun Computer Vision project using Python & OpenCV to simulate Harry Potter’s Invisibility Cloak. Uses color detection (HSV) and background replacement to make the cloak wearer invisible in real-time.I used my red plain shirt for the invisibility as it is simple to use and blends easily.

Features:
Works in real-time with webcam
Adjustable HSV sliders for better color detection
Fun mix of Computer Vision + a little magic 

How It Works:-

1) Capture the background frame
2) Detect the chosen cloak color using HSV values
3) Replace the cloak area with the saved background → now you are invisible

🛠️ Tech Stack

1) Python 3
2) OpenCV (cv2)
3) NumPy

Full step by step installation:-
1) Create a virtual environment
     python -m venv venv
     venv\Scripts\activate(For windows)
     source venv/bin/activate(For mac)

2) Install dependencies
      pip install opencv-python numpy

3) Run the script
      Wait for 3 seconds → background is captured
      Wear your cloak (e.g., red)
      Adjust the HSV sliders until your cloak blends into the background
      Press Q to quit


