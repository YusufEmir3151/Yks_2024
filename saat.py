import tkinter as tk
from datetime import datetime, timedelta


def update_timer():
    current_time = datetime.now()
    time_left = target_date - current_time
    days_left = time_left.days
    hours_left, remainder = divmod(time_left.seconds, 3600)
    minutes_left, seconds_left = divmod(remainder, 60)
    if days_left != 0 and hours_left != 0 and minutes_left != 0 and seconds_left != 0:
        timer_label.config(text=f"{days_left} gün, {hours_left} saat, {minutes_left} dakika, {seconds_left} saniye")
    elif days_left == 0 and hours_left == 0 and minutes_left == 0:
        timer_label.config(text=f"{seconds_left} saniye")
    elif days_left == 0 and hours_left == 0:
        timer_label.config(text=f"{minutes_left} dakika, {seconds_left} saniye")
    elif days_left == 0:
        timer_label.config(text=f"{hours_left} saat, {minutes_left} dakika, {seconds_left} saniye")

    timer_label.after(1000, update_timer)


target_date = datetime(2024, 6, 22, 10, 0, 0)

app = tk.Tk()
app.title("Kalan Süre")
app.geometry("400x80")

timer_label = tk.Label(app, text="", font=("Helvetica", 14))
timer_label.pack(pady=20)

update_timer()
app.mainloop()
