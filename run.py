import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import os


# Function to rename MP3 files in the selected folder
def rename_mp3_files():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        mp3_files = [f for f in os.listdir(folder_selected) if f.endswith(".mp3")]
        for i, filename in enumerate(mp3_files, start=1):
            new_name = f"{i}.mp3"
            old_path = os.path.join(folder_selected, filename)
            new_path = os.path.join(folder_selected, new_name)
            os.rename(old_path, new_path)
        messagebox.showinfo("Uğurlu", f"{len(mp3_files)} sayda mp3 fayl yenidən adlandırıldı! ")


# Create the main window
app = ctk.CTk()
app.title("Enigma MP3 Renamer")
app.geometry("400x200")

# Add a button to open the folder dialog and rename files
label = ctk.CTkLabel(app, text="MP3 fayllarını yenidən adlandırmaq üçün qovluğu seç.\nQovluğu seçdikdən sonra \nyenidən adlandırma prosesi avtomatik başlayacaq.\nYenidən adlandırma bitəndən sonra bu barədə bildiriş çıxacaq.")
label.pack(pady=10)
select_button = ctk.CTkButton(
    app, text="Qovluğu seç", command=rename_mp3_files
)
select_button.pack(padx=20, pady=20)

# Run the application
app.mainloop()
