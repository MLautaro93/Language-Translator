from tkinter import PhotoImage, ttk
import tkinter as tk
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk

# Window
root = tk.Tk()
root.geometry('512x384')
root.resizable(False, False)
root.title('Translator')

# Translator
translator = Translator()

# Labels
header = tk.Label(text = 'Translator', font = 'lucida 20 bold', fg = 'white', bg = 'dark blue')
header.pack()
text_box = tk.Text(font = 'lucida 10', width = 25, height = 5)
text_box.place(relx = .25, y = 100, anchor = tk.CENTER)
text_box.insert(tk.END, 'Insert text here.')
translation_box = tk.Text(font = 'lucida 10', width = 25, height = 5, state = 'disabled')
translation_box.place(relx = .75, y = 100, anchor = tk.CENTER)

# Combobox
languages = [i.capitalize() for i in list(LANGUAGES.values())]
src_combobox = ttk.Combobox(values = languages, state = 'readonly')
src_combobox.place(relx = .25, y = 200, anchor = tk.CENTER)
dest_combobox = ttk.Combobox(values = languages, state = 'readonly')
dest_combobox.place(relx = .75, y = 200, anchor = tk.CENTER)

# Detect language
def detect():
    text = text_box.get(1.0, tk.END)
    lang = translator.detect(text).lang
    language = LANGUAGES[lang].capitalize()
    src_combobox.set(language)

# Translate function
def translate(*args):
    text = text_box.get(1.0, tk.END)
    translation_box.config(state = 'normal')
    translation_box.delete(1.0, tk.END)
    if len(text) >= 2:
        translation = translator.translate(text, src = src_combobox.get(), dest = dest_combobox.get())
        translation_box.insert(tk.END, translation.text)
    translation_box.config(state = 'disabled')

# Function to swap languages
def swap():
    a = text_box.get(1.0, tk.END)
    b = translation_box.get(1.0, tk.END)
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, b)
    translation_box.config(state = 'normal')
    translation_box.delete(1.0, tk.END)
    translation_box.insert(tk.END, a)
    translation_box.config(state = 'disabled')

    x = src_combobox.get()
    y = dest_combobox.get()
    src_combobox.set(y)
    dest_combobox.set(x)

# "Detect language" button
detect_button = tk.Button(text = 'Detect language', command = detect)
detect_button.place(relx = .25, y = 167, anchor = tk.CENTER)

# Translate button
translate_button = tk.Button(text = 'Translate', fg = 'white', bg = 'dark blue', command = translate)
translate_button.place(relx = .5, y = 200, anchor = tk.CENTER)
root.bind('<Return>', translate)

# Swap button
img = Image.open('swap.png').resize((25, 25))
image = ImageTk.PhotoImage(img)
swap_button = tk.Button(image = image, command = swap)
swap_button.place(relx = .5, y = 100, anchor = tk.CENTER)

root.mainloop()