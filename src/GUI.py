import tkinter as tk
from tkinter import messagebox, scrolledtext
from main import generate_characters, export_character, export_characters_to_json, export_characters_to_html

class CharacterGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("🌟 Генератор персонажей")
        master.geometry("700x900")
        master.configure(bg="#1e1e2f")

        self.text = scrolledtext.ScrolledText(
            master, font=("Consolas", 12),
            wrap=tk.WORD, bg="#2d2d44", fg="white",
            insertbackground="white", padx=10, pady=10,
            borderwidth=2, relief=tk.RIDGE
        )
        self.text.pack(padx=20, pady=15, expand=True, fill=tk.BOTH)

        control_frame = tk.Frame(master, bg="#1e1e2f")
        control_frame.pack(pady=10)

        tk.Label(control_frame, text="Количество персонажей:", fg="white", bg="#1e1e2f", font=("Arial", 12)).grid(row=0, column=0, padx=5)

        self.count_entry = tk.Entry(control_frame, width=5, font=("Arial", 12))
        self.count_entry.insert(0, "1")
        self.count_entry.grid(row=0, column=1, padx=5)

        self.generate_button = tk.Button(
            control_frame, text="🎲 Сгенерировать",
            command=self.generate, font=("Arial", 12, "bold"),
            bg="#4e88af", fg="white", activebackground="#3c6c8e",
            width=15, relief=tk.RAISED, bd=2
        )
        self.generate_button.grid(row=0, column=2, padx=5)

        self.export_txt_button = tk.Button(
            control_frame, text="💾 Экспорт TXT",
            command=self.export_txt, font=("Arial", 12, "bold"),
            bg="#2196f3", fg="white", activebackground="#1976d2",
            width=12, relief=tk.RAISED, bd=2
        )
        self.export_txt_button.grid(row=1, column=0, padx=5, pady=10)

        self.export_json_button = tk.Button(
            control_frame, text="💾 Экспорт JSON",
            command=self.export_json, font=("Arial", 12, "bold"),
            bg="#4caf50", fg="white", activebackground="#388e3c",
            width=12, relief=tk.RAISED, bd=2
        )
        self.export_json_button.grid(row=1, column=1, padx=5, pady=10)

        self.export_html_button = tk.Button(
            control_frame, text="💾 Экспорт HTML",
            command=self.export_html, font=("Arial", 12, "bold"),
            bg="#ff9800", fg="white", activebackground="#f57c00",
            width=12, relief=tk.RAISED, bd=2
        )
        self.export_html_button.grid(row=1, column=2, padx=5, pady=10)

        self.characters = []

    def generate(self):
        try:
            count = int(self.count_entry.get())
            if count < 1:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное положительное число")
            return

        self.characters = generate_characters(count)
        self.text.delete("1.0", tk.END)

        for i, c in enumerate(self.characters, 1):
            self.text.insert(tk.END, f"--- Персонаж #{i} ---\n")
            for key, value in c.items():
                if key == "Навыки":
                    self.text.insert(tk.END, "Навыки:\n")
                    for skill, lvl in value.items():
                        self.text.insert(tk.END, f"  • {skill}: {lvl}\n")
                elif key == "История":
                    self.text.insert(tk.END, "\nИстория:\n")
                    self.text.insert(tk.END, value + "\n\n")
                else:
                    self.text.insert(tk.END, f"{key}: {value}\n")
            self.text.insert(tk.END, "\n\n")

    def export_txt(self):
        if not self.characters:
            messagebox.showwarning("Внимание", "Сначала сгенерируйте персонажей")
            return

        # Экспортируем по одному в отдельные файлы персонажей
        for idx, character in enumerate(self.characters, 1):
            export_character(character, filename=f"персонаж_{idx}.txt")
        messagebox.showinfo("Успех", f"Экспортировано {len(self.characters)} TXT файлов")

    def export_json(self):
        if not self.characters:
            messagebox.showwarning("Внимание", "Сначала сгенерируйте персонажей")
            return

        export_characters_to_json(self.characters)
        messagebox.showinfo("Успех", "Экспортировано в 'персонажи.json'")

    def export_html(self):
        if not self.characters:
            messagebox.showwarning("Внимание", "Сначала сгенерируйте персонажей")
            return

        export_characters_to_html(self.characters)
        messagebox.showinfo("Успех", "Экспортировано в 'персонажи.html'")

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterGeneratorApp(root)
    root.mainloop()
