import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.root.geometry("400x200")

        self.languages = ["en", "es", "fr", "de", "ja", "ko", "zh-CN", "ru"]
        self.translator = Translator()

        self.create_widgets()

    def create_widgets(self):
        self.label_text = tk.Label(self.root, text="Enter text to translate:")
        self.label_text.pack(pady=10)

        self.text_entry = tk.Entry(self.root, width=40)
        self.text_entry.pack(pady=10)

        self.label_language = tk.Label(self.root, text="Select language to translate to:")
        self.label_language.pack(pady=5)

        self.language_combobox = ttk.Combobox(self.root, values=self.languages, state="readonly")
        self.language_combobox.set("en")  # Set default language to English
        self.language_combobox.pack(pady=10)

        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)
        self.translate_button.pack(pady=10)

        self.label_result = tk.Label(self.root, text="")
        self.label_result.pack(pady=10)

    def translate_text(self):
        input_text = self.text_entry.get()
        selected_language = self.language_combobox.get()

        if input_text:
            translated_text = self.translator.translate(input_text, dest=selected_language).text
            self.label_result.config(text=f"Translated Text: {translated_text}")
        else:
            self.label_result.config(text="Please enter text to translate.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()
