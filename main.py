import re
import tkinter as tk
from tkinter import scrolledtext

def clean_text(text):
    # Remove markdown symbols like ###, **, and extra spaces, but retain line breaks
    cleaned_text = re.sub(r'(\*\*|###|---)', '', text)  # Remove **, ###, ---
    cleaned_text = re.sub(r'^\s*-\s*', '', cleaned_text, flags=re.MULTILINE)  # Remove bullet points
    cleaned_text = re.sub(r'[ \t]+', ' ', cleaned_text)  # Remove extra spaces within lines

    # Retain line breaks but strip leading and trailing spaces on each line
    cleaned_text = "\n".join(line.strip() for line in cleaned_text.splitlines())
    return cleaned_text.strip()

def process_text():
    input_text = input_text_area.get("1.0", tk.END)
    cleaned_text = clean_text(input_text)
    output_text_area.delete("1.0", tk.END)
    output_text_area.insert(tk.END, cleaned_text)

# Set up the main window
root = tk.Tk()
root.title("Text Cleaner")
root.geometry("800x600")

# Input text label and area
input_label = tk.Label(root, text="Input Text:")
input_label.pack()
input_text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=15)
input_text_area.pack(padx=10, pady=5)

# Button to process the text
process_button = tk.Button(root, text="Clean Text", command=process_text)
process_button.pack(pady=10)

# Output text label and area
output_label = tk.Label(root, text="Cleaned Text:")
output_label.pack()
output_text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=15)
output_text_area.pack(padx=10, pady=5)

# Run the application
root.mainloop()
