import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil


# Function to rename and copy MP3 files to a new folder
def rename_mp3_files():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        # Create the new folder named "Netice" inside the selected folder
        new_folder = os.path.join(folder_selected, "Netice")
        os.makedirs(new_folder, exist_ok=True)

        mp3_files = [f for f in os.listdir(folder_selected) if f.endswith(".mp3")]
        for i, filename in enumerate(mp3_files, start=1):
            new_name = f"{i}.mp3"
            old_path = os.path.join(folder_selected, filename)
            new_path = os.path.join(new_folder, new_name)
            shutil.copy2(old_path, new_path)  # Copy and rename the file

        messagebox.showinfo(
            "Uğurlu",
            f"{len(mp3_files)} sayda mp3 fayl yenidən adlandırıldı və Netice qovluğuna kopyalandı!",
        )


# Create the main window
app = ctk.CTk()
app.title("Enigma MP3 Renamer v1.1 @ncniyazov")
app.geometry("600x200")

# Add a label with instructions
label = ctk.CTkLabel(
    app,
    text="MP3 fayllarını yenidən adlandırmaq və kopyalamaq üçün qovluğu seç.\nQovluğu seçdikdən sonra \nyenidən adlandırma və kopyalama prosesi avtomatik başlayacaq.\nYenidən adlandırma və kopyalama bitəndən sonra bu barədə bildiriş çıxacaq.",
)
label.pack(pady=15)

# Add a button to open the folder dialog and rename files
select_button = ctk.CTkButton(app, text="Qovluğu seç", command=rename_mp3_files)
select_button.pack(padx=20, pady=20)

# Run the application
app.mainloop()
