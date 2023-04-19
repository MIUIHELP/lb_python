import tkinter as tk
from tkinter import filedialog
import json

class ScreenshotsApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fraps Screenshots")
        self.root.geometry("300x200")

        # Додаткові змінні для збереження введених даних
        self.save_path = tk.StringVar()
        self.file_format = tk.StringVar()
        self.quality = tk.IntVar()
        self.hotkey = tk.StringVar()

        # Віджети для вводу даних
        tk.Label(self.root, text="Збереження в:").grid(row=0, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.save_path).grid(row=0, column=1)
        tk.Button(self.root, text="Обрати", command=self.choose_save_path).grid(row=0, column=2)

        tk.Label(self.root, text="Формат файлу:").grid(row=1, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.file_format).grid(row=1, column=1)

        tk.Label(self.root, text="Якість:").grid(row=2, column=0, sticky="e")
        tk.Scale(self.root, variable=self.quality, from_=1, to=100, orient="horizontal").grid(row=2, column=1)

        tk.Label(self.root, text="Гаряча клавіша:").grid(row=3, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.hotkey).grid(row=3, column=1)

        # Кнопка "Зберегти"
        tk.Button(self.root, text="Зберегти", command=self.save_settings).grid(row=4, columnspan=3)

        self.root.mainloop()

    def choose_save_path(self):
        self.save_path.set(filedialog.askdirectory())

    def save_settings(self):
        # Отримання введених даних
        save_path = self.save_path.get()
        file_format = self.file_format.get()
        quality = self.quality.get()
        hotkey = self.hotkey.get()

        # Збереження даних у форматі JSON у файл
        data = {
            "save_path": save_path,
            "file_format": file_format,
            "quality": quality,
            "hotkey": hotkey
        }
        with open("settings.json", "w") as f:
            json.dump(data, f)

        # Закриття вікна
        self.root.destroy()

if __name__ == "__main__":
    app = ScreenshotsApp()
