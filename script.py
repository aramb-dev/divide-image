import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

class ImageDividerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Divider")
        self.image_path = None
        self.save_folder = None
        self.num_rows = tk.IntVar()  # Variable to store the number of rows
        self.prefix = tk.StringVar(value="pic_")  # Variable to store the prefix

        # Create buttons to trigger the actions
        self.select_image_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_image_button.pack()
        self.image_label = tk.Label(root, text="Selected Image: None")
        self.image_label.pack()

        self.select_save_button = tk.Button(root, text="Select Save Folder", command=self.select_save_folder)
        self.select_save_button.pack()
        self.folder_label = tk.Label(root, text="Selected Folder: None")
        self.folder_label.pack()

        self.num_rows_label = tk.Label(root, text="Number of Rows:")
        self.num_rows_label.pack()

        self.num_rows_slider = tk.Scale(root, from_=1, to=100, orient="horizontal", variable=self.num_rows, label="Rows")
        self.num_rows_slider.pack()

        self.prefix_label = tk.Label(root, text="File Prefix:")
        self.prefix_label.pack()
        self.prefix_entry = tk.Entry(root, textvariable=self.prefix)
        self.prefix_entry.pack()

        self.divide_button = tk.Button(root, text="Divide Image", command=self.divide_image)
        self.divide_button.pack()

        # Create and configure a label for displaying information
        self.info_label = tk.Label(root, text="Select an image to divide into rows.")
        self.info_label.pack()

        # Create a Text widget to display size and pixel limit information
        self.info_text = tk.Text(root, height=5, width=40)
        self.info_text.pack()

    def select_image(self):
        self.image_path = filedialog.askopenfilename(title="Select an image to divide into rows")
        if self.image_path:
            self.image_label.config(text=f"Selected Image: {os.path.basename(self.image_path)}")
        else:
            self.image_label.config(text="Selected Image: None")

    def select_save_folder(self):
        self.save_folder = filedialog.askdirectory(title="Select a folder to save the divided rows")
        if self.save_folder:
            self.folder_label.config(text=f"Selected Folder: {self.save_folder}")
        else:
            self.folder_label.config(text="Selected Folder: None")

    def divide_image(self):
        if not self.image_path:
            self.info_label.config(text="No image selected.")
            return
        if not self.save_folder:
            self.info_label.config(text="No save folder selected.")
            return

        num_rows = self.num_rows.get()

        if num_rows < 1:
            self.info_label.config(text="Please select a valid number of rows.")
            return

        prefix = self.prefix.get()

        # Check if the save folder already contains files
        existing_files = [f for f in os.listdir(self.save_folder) if os.path.isfile(os.path.join(self.save_folder, f))]

        if existing_files:
            # Ask the user for confirmation to overwrite files
            confirm_message = "The selected folder already contains files. Do you want to overwrite them?"
            user_response = messagebox.askquestion("Confirmation", confirm_message)

            if user_response == "no":
                # Prompt the user to select another folder
                self.select_save_folder()
                return
            else:
                # Delete existing files in the folder
                for existing_file in existing_files:
                    file_path = os.path.join(self.save_folder, existing_file)
                    os.remove(file_path)

        try:
            image = Image.open(self.image_path)
            width, height = image.size
            row_height = height // num_rows

            for i in range(num_rows):
                file_name = f"{prefix}{i+1}.png"
                file_path = os.path.join(self.save_folder, file_name)
                row = image.crop((0, i * row_height, width, (i + 1) * row_height))
                row.save(file_path)

            # Update the Text widget with size and pixel limit information
            info_text = f"Image divided into {num_rows} rows and saved to the specified folder.\n"
            info_text += f"Image Size: {width}x{height} pixels\n"
            info_text += f"Row Height: {row_height} pixels"
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, info_text)
        except Exception as e:
            self.info_label.config(text=f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageDividerApp(root)
    root.mainloop()
