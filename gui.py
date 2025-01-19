import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
from sors import process_image
import logging
from pathlib import Path

class BackgroundRemoverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Remover")
        self.root.geometry("800x600")
        
        # Initialize variables
        self.input_path = None
        self.output_image = None
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create UI elements
        self._create_buttons()
        self._create_image_displays()
        self._create_status_bar()
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

    def _create_buttons(self):
        # Buttons frame
        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.grid(row=0, column=0, columnspan=2, pady=5, sticky=tk.W)
        
        # Select image button
        self.select_btn = ttk.Button(btn_frame, text="Select Image", command=self._select_image)
        self.select_btn.grid(row=0, column=0, padx=5)
        
        # Process button
        self.process_btn = ttk.Button(btn_frame, text="Remove Background", command=self._process_image, state=tk.DISABLED)
        self.process_btn.grid(row=0, column=1, padx=5)
        
        # Save button
        self.save_btn = ttk.Button(btn_frame, text="Save Image", command=self._save_image, state=tk.DISABLED)
        self.save_btn.grid(row=0, column=2, padx=5)

    def _create_image_displays(self):
        # Image frames
        self.input_frame = ttk.LabelFrame(self.main_frame, text="Input Image", padding="5")
        self.input_frame.grid(row=1, column=0, padx=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.output_frame = ttk.LabelFrame(self.main_frame, text="Output Image", padding="5")
        self.output_frame.grid(row=1, column=1, padx=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Image labels
        self.input_label = ttk.Label(self.input_frame)
        self.input_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.output_label = ttk.Label(self.output_frame)
        self.output_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for image frames
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.rowconfigure(0, weight=1)
        self.output_frame.columnconfigure(0, weight=1)
        self.output_frame.rowconfigure(0, weight=1)

    def _create_status_bar(self):
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self.main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        self.status_bar.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))
        self.status_var.set("Ready")

    def _select_image(self):
        file_types = [
            ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"),
            ("All files", "*.*")
        ]
        filename = filedialog.askopenfilename(filetypes=file_types)
        
        if filename:
            self.input_path = filename
            self._display_input_image()
            self.process_btn.config(state=tk.NORMAL)
            self.status_var.set(f"Selected image: {os.path.basename(filename)}")

    def _display_input_image(self):
        image = Image.open(self.input_path)
        image.thumbnail((350, 350))  # Resize for display
        photo = ImageTk.PhotoImage(image)
        
        self.input_label.configure(image=photo)
        self.input_label.image = photo  # Keep a reference

    def _process_image(self):
        if not self.input_path:
            return
        
        try:
            self.status_var.set("Processing image...")
            self.root.update()
            
            # Create temporary file for output
            temp_output = str(Path(self.input_path).parent / "temp_output.png")
            
            # Process the image
            process_image(self.input_path, temp_output)
            
            # Display the output image
            self.output_image = Image.open(temp_output)
            self._display_output_image()
            
            # Enable save button
            self.save_btn.config(state=tk.NORMAL)
            self.status_var.set("Background removed successfully")
            
            # Clean up temporary file
            os.remove(temp_output)
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_var.set("Error processing image")

    def _display_output_image(self):
        if self.output_image:
            image_copy = self.output_image.copy()
            image_copy.thumbnail((350, 350))  # Resize for display
            photo = ImageTk.PhotoImage(image_copy)
            
            self.output_label.configure(image=photo)
            self.output_label.image = photo  # Keep a reference

    def _save_image(self):
        if not self.output_image:
            return
            
        file_types = [("PNG files", "*.png")]
        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=file_types,
            initialfile="background_removed.png"
        )
        
        if filename:
            try:
                self.output_image.save(filename)
                self.status_var.set(f"Image saved as: {os.path.basename(filename)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save image: {str(e)}")
                self.status_var.set("Error saving image")

def main():
    root = tk.Tk()
    app = BackgroundRemoverGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()