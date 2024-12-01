import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Create the main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x400")

# Initialize the Translator object
translator = Translator()

# Function to translate the text
def translate_text():
    # Get the text from the input and selected languages
    input_text = text_to_translate.get("1.0", "end-1c")
    source_lang = source_lang_combobox.get()
    target_lang = target_lang_combobox.get()

    if input_text.strip() == "":
        output_text.delete(1.0, "end")
        output_text.insert("1.0", "Please enter some text to translate.")
        return

    # Perform translation using googletrans
    translated = translator.translate(input_text, src=source_lang, dest=target_lang)
    output_text.delete(1.0, "end")
    output_text.insert("1.0", translated.text)

# Creating the input section
input_label = tk.Label(root, text="Enter Text:")
input_label.pack(pady=10)

text_to_translate = tk.Text(root, height=5, width=50)
text_to_translate.pack(pady=5)

# Creating the language selection section
language_label = tk.Label(root, text="Select Languages:")
language_label.pack(pady=10)

source_lang_label = tk.Label(root, text="From Language:")
source_lang_label.pack(pady=5)

# Dropdown for selecting source language
source_lang_combobox = ttk.Combobox(root, values=['English', 'Spanish', 'French', 'German', 'Italian', 'Portuguese', 'Hindi', 'Japanese', 'Russian', 'Chinese'])
source_lang_combobox.set("en")
source_lang_combobox.pack(pady=5)

target_lang_label = tk.Label(root, text="To Language:")
target_lang_label.pack(pady=5)

# Dropdown for selecting target language
target_lang_combobox = ttk.Combobox(root, values=['English', 'Spanish', 'French', 'German', 'Italian', 'Portuguese', 'Hindi', 'Japanese', 'Russian', 'Chinese'])
target_lang_combobox.set("es")
target_lang_combobox.pack(pady=5)

# Button to perform the translation
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=20)

# Creating the output section
output_label = tk.Label(root, text="Translated Text:")
output_label.pack(pady=10)

output_text = tk.Text(root, height=5, width=50)
output_text.pack(pady=5)

# Start the GUI event loop
root.mainloop()
