import tkinter as tk
from datetime import datetime
import time

class DigitalClockGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Digital Clock")
        self.window.geometry("500x300")
        self.window.configure(bg='black')
        self.window.resizable(False, False)
        
    
        title = tk.Label(
            self.window,
            text="Digital CLOCK",
            font=('Arial', 20, 'bold'),
            bg='black',
            fg='white'
        )
        title.pack(pady=20)
        


        
        self.time_label = tk.Label(
            self.window,
            text="",
            font=('DS-Digital', 80, 'bold'),
            bg='black',
            fg='#00ff00'
        )
        self.time_label.pack(pady=20)
        
        # Date display
        self.date_label = tk.Label(
            self.window,
            text="",
            font=('Arial', 16),
            bg='black',
            fg='white'
        )
        self.date_label.pack()
        
        self.update_time()
        self.window.mainloop()
    
    def update_time(self):
        """Update the clock display"""
        now = datetime.now()
        
        
        time_str = now.strftime('%H:%M:%S')
        self.time_label.config(text=time_str)
        
        # Date
        date_str = now.strftime('%A, %B %d, %Y')
        self.date_label.config(text=date_str)
        
        
        if now.second % 2 == 0:
            self.time_label.config(fg="#adef41")
        else:
            self.time_label.config(fg="#2c8cf2")
        
        self.window.after(1000, self.update_time)

DigitalClockGUI()
