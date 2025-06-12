import tkinter as tk
from tkinter import messagebox
import pywhatkit
import datetime

def schedule_message():
    try:
        phone = phone_entry.get()
        message = message_entry.get("1.0", tk.END).strip()
        # hour = int(hour_entry.get())
        # minute = int(minute_entry.get())
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute  # Schedule for 1 minute later

        if not phone or not message:
            raise ValueError("Phone and message fields cannot be empty.")

        # pywhatkit.sendwhatmsg(phone, message, hour, minute)
        pywhatkit.sendwhatmsg(phone, message, now.hour, now.minute)

        messagebox.showinfo("Scheduled", f"Message scheduled for {hour:02d}:{minute:02d}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("WhatsApp Scheduler")
root.geometry("400x300")

tk.Label(root, text="Phone Number (+62...)").pack(pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.pack()

tk.Label(root, text="Message").pack(pady=5)
message_entry = tk.Text(root, height=4, width=30)
message_entry.pack()

# tk.Label(root, text="Schedule Time").pack(pady=5)
# time_frame = tk.Frame(root)
# time_frame.pack()

# tk.Label(time_frame, text="Hour (24h):").pack(side=tk.LEFT)
# hour_entry = tk.Entry(time_frame, width=5)
# hour_entry.pack(side=tk.LEFT)

# tk.Label(time_frame, text="Minute:").pack(side=tk.LEFT)
# minute_entry = tk.Entry(time_frame, width=5)
# minute_entry.pack(side=tk.LEFT)

# tk.Button(root, text="Schedule Message", command=schedule_message).pack(pady=15)
tk.Button(root, text="Send Now (1 min delay)", command=schedule_message).pack(pady=20)

root.mainloop()
