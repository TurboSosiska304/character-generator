import tkinter as tk
from tkinter import messagebox, scrolledtext
from main import generate_character, export_character

class CharacterGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("🌟 Генератор персонажей")
        master.geometry("600x800")
        master.configure(bg="#1e1e2f")

        self.text = scrolledtext.ScrolledText(
            master, font=("Consolas", 12),
            wrap=tk.WORD, bg="#2d2d44", fg="white",
            insertbackground="white", padx=10, pady=10,
            borderwidth=2, relief=tk.RIDGE
        )
        self.text.pack(padx=20, pady=20, expand=True, fill=tk.BOTH)

        btn_frame = tk.Frame(master, bg="#1e1e2f")
        btn_frame.pack(pady=10)

        self.generate_button = tk.Button(
            btn_frame, text="🎲 Сгенерировать",
            command=self.generate, font=("Arial", 12, "bold"),
            bg="#4e88af", fg="white", activebackground="#3c6c8e",
            width=20, relief=tk.RAISED, bd=2
        )
        self.generate_button.grid(row=0, column=0, padx=10)

        self.export_button = tk.Button(
            btn_frame, text="💾 Экспортировать",
            command=self.export, font=("Arial", 12, "bold"),
            bg="#4caf50", fg="white", activebackground="#388e3c",
            width=20, relief=tk.RAISED, bd=2
        )
        self.export_button.grid(row=0, column=1, padx=10)

        self.current_character = None

    def generate(self):
        self.current_character = generate_character()
        self.text.delete("1.0", tk.END)
        self._display_character(self.current_character)

    def export(self):
        if not self.current_character:
            messagebox.showwarning("⚠️", "Сначала сгенерируй персонажа!")
            return
        export_character(self.current_character)
        messagebox.showinfo("✅ Успех", "Персонаж экспортирован в 'персонаж.txt'")

    def _display_character(self, character):
        self.text.insert(tk.END, "🌟 Характеристики персонажа:\n\n")
        for key, value in character.items():
            if key == "Навыки":
                self.text.insert(tk.END, "\n🔧 Навыки:\n")
                for skill, lvl in value.items():
                    self.text.insert(tk.END, f"  • {skill}: {lvl}\n")
            elif key == "История":
                self.text.insert(tk.END, "\n📜 История:\n")
                self.text.insert(tk.END, value + "\n")
            else:
                self.text.insert(tk.END, f"{key}: {value}\n")
