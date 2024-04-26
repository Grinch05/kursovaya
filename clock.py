import tkinter as tk
import time
import math

def update_clock():
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Очистка старых стрелок и цифр
    canvas.delete("clock")

    # Рисование часовой стрелки
    hour_angle = math.radians((hours % 12) * 30 + (minutes / 2))
    hour_x = center_x + math.sin(hour_angle) * (clock_radius * 0.5)
    hour_y = center_y - math.cos(hour_angle) * (clock_radius * 0.5)
    canvas.create_line(center_x, center_y, hour_x, hour_y, width=5, tags="clock")

    # Рисование минутной стрелки
    minute_angle = math.radians(minutes * 6 + (seconds / 10))
    minute_x = center_x + math.sin(minute_angle) * (clock_radius * 0.7)
    minute_y = center_y - math.cos(minute_angle) * (clock_radius * 0.7)
    canvas.create_line(center_x, center_y, minute_x, minute_y, width=3, tags="clock")

    # Рисование секундной стрелки
    second_angle = math.radians(seconds * 6)
    second_x = center_x + math.sin(second_angle) * (clock_radius * 0.9)
    second_y = center_y - math.cos(second_angle) * (clock_radius * 0.9)
    canvas.create_line(center_x, center_y, second_x, second_y, fill="red", width=1, tags="clock")

    # Рисование цифр на циферблате
    for i in range(1, 13):
        angle = math.radians(i * 30)
        digit_x = center_x + math.sin(angle) * (clock_radius * 0.85)
        digit_y = center_y - math.cos(angle) * (clock_radius * 0.85)
        canvas.create_text(digit_x, digit_y, text=str(i), font=("Arial", 12, "bold"), tags="clock")

    # Повторно вызываем функцию через 1 секунду
    root.after(1000, update_clock)

# Создание графического интерфейса
root = tk.Tk()
root.title("Аналоговые часы")

# Создание холста
canvas_width = 400 
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack() # Этот метод упаковывает холст в родительское окно, чтобы он был видимым на графическом интерфейсе.

# Определение центра часов
center_x = canvas_width / 2
center_y = canvas_height / 2
clock_radius = min(canvas_width, canvas_height) / 2 - 10 # Для того, чтобы определить радиус окружности, вписанной в холст, так чтобы часы были целиком видны внутри этой окружности.

# Запуск функции обновления часов
update_clock() 

# Запуск основного цикла обработки событий
root.mainloop()
