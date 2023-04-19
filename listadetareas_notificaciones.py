import time
from win10toast import ToastNotifier

toaster = ToastNotifier()
tasks = [
    {"task": "Crear Cuenta Tiktok", "time": "23:35", "done": False},
    {"task": "Tarea 2", "time": "23:40", "done": False},
    {"task": "Tarea 3", "time": "23:45", "done": False}
]

while True:
    current_time = time.strftime("%H:%M")
    for task in tasks:
        if task["time"] == current_time and not task["done"]:
            toaster.show_toast(task["task"], "Hora de realizar la tarea", threaded=True, icon_path=None, duration=15)
            task["done"] = True
    time.sleep(60) # Check tasks every minute
