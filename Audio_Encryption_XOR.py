import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os

def encrypt_audio():
    try:
        input_file_path = file_path_entry.get()
        key = key_entry.get()
        output_file_path = output_path_entry.get()

        # Open the input file in binary mode
        with open(input_file_path, 'rb') as file:
            # Read the contents of the file
            data = file.read()

        # Perform XOR encryption
        encrypted_data = bytes([data[i] ^ ord(key[i % len(key)]) for i in range(len(data))])

        # Save the encrypted data to the output file
        with open(output_file_path, 'wb') as file:
            file.write(encrypted_data)

        messagebox.showinfo("Success", "File encrypted successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_audio():
    try:
        input_file_path = file_path_entry.get()
        key = key_entry.get()
        output_file_path = output_path_entry.get()

        # Open the input file in binary mode
        with open(input_file_path, 'rb') as file:
            # Read the contents of the file
            data = file.read()

        # Perform XOR decryption
        decrypted_data = bytes([data[i] ^ ord(key[i % len(key)]) for i in range(len(data))])

        # Save the decrypted data to the output file
        with open(output_file_path, 'wb') as file:
            file.write(decrypted_data)

        messagebox.showinfo("Success", "File decrypted successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file():
    file_path = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

def browse_output_path():
    output_path = filedialog.asksaveasfilename(defaultextension=".mp3")
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, output_path)

def clear_fields():
    file_path_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    output_path_entry.delete(0, tk.END)

def validate_input_file():
    input_file_path = file_path_entry.get()
    if not os.path.isfile(input_file_path):
        messagebox.showerror("Error", "Please select a valid input file.")

# Create the main window
window = tk.Tk()
window.title("Audio Encryption by XOR Encryption")

# Set the style of the widgets using the ttk module
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=('Helvetica', 10), background='#4CAF50', foreground='white')

# Create the widgets
file_path_label = tk.Label(window, text="Select Input File:")
file_path_entry = tk.Entry(window, width=50)
file_path_browse_button = ttk.Button(window, text="Browse", command=browse_file)

key_label = tk.Label(window, text="Enter Encryption Key:")
key_entry = tk.Entry(window, width=50)

output_path_label = tk.Label(window, text="Select Output File:")
output_path_entry = tk.Entry(window, width=50)
output_path_browse_button = ttk.Button(window, text="Browse", command=browse_output_path)

encrypt_button = ttk.Button(window, text="Encrypt", command=encrypt_audio)
decrypt_button = ttk.Button(window, text="Decrypt", command=decrypt_audio)
clear_button = ttk.Button(window, text="Clear", command=clear_fields)

# Add the widgets to the window
file_path_label.grid(row=0, column=0, padx=5, pady=5)
file_path_entry.grid(row=0, column=1, padx=5, pady=5)
file_path_browse_button.grid(row=0, column=2, padx=5, pady=5)

key_label.grid(row=1, column=0, padx=5, pady=5)
key_entry.grid(row=1, column=1, padx=5, pady=5)

output_path_label.grid(row=2, column=0, padx=5, pady=5)
output_path_entry.grid(row=2, column=1, padx=5, pady=5)
output_path_browse_button.grid(row=2, column=2, padx=5, pady=5)

encrypt_button.grid(row=3, column=0, padx=5, pady=5)
decrypt_button.grid(row=3, column=1, padx=5, pady=5)
clear_button.grid(row=3, column=2, padx=5, pady=5)

# Set default values for some widgets
key_entry.insert(0, "mysecretkey")

# Add validation to the input file path field
file_path_entry.bind("<FocusOut>", lambda event: validate_input_file())

# Run the main event loop
window.mainloop()