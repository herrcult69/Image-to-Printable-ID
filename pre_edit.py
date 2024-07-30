from tkinter import *
import PIL.Image, PIL.ImageTk
import tkinter.messagebox as messagebox
from tkinter import filedialog
import sys
class ImageRotator:
    def __init__(self, root):
        self.root = root

        # Create buttons
        self.load_button = Button(root, text="Load Image", command=self.load_image)
        self.rotate_button = Button(root, text="Rotate 90°", command=self.rotate_image)
        self.choose_button = Button(root, text="Choose Image", command=self.choose_image)
        self.exit_button = Button(root, text="Exit", command=sys.exit)
        self.exit_button.pack()
        self.load_button.pack()
        self.rotate_button.pack()
        self.choose_button.pack()
        self.choose_button["state"] = "disabled"
        self.rotate_button["state"] = "disabled"
        # Initialize image variables
        self.path = None
        self.extension = None
        self.image = None
        self.tk_image = None
        self.root.geometry("800x600")

    def load_image(self):
        # Get the image path from the entry widget
        path = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
        
        if not path:
            messagebox.showerror("Error", "Please enter a valid image path.")
            return

        try:
            self.path = path
            self.extension = path.split('/')[-1]
            # Load image
            self.image = PIL.Image.open(path)
            w, h = self.image.size
            print(w, h)
            self.tk_image = PIL.ImageTk.PhotoImage(self.image)
            self.root.geometry(f"{w}x{h}")
            # Display image
            self.image_label = Label(self.root, image=self.tk_image)
            self.image_label.pack()
            self.rotate_button["state"] = "normal"
            self.choose_button["state"] = "normal"
            self.load_button["state"] = "disabled"
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"Error loading image: {str(e)}")

    def rotate_image(self):
        if self.image:
            # Rotate 90 degrees
            self.image = self.image.rotate(90, expand=True)
            self.tk_image = PIL.ImageTk.PhotoImage(self.image)

            # Update displayed image
            self.image_label.config(image=self.tk_image)

            # Adjust window size to fit the rotated image
            w, h = self.image.size
            self.root.geometry(f"{w}x{h}")
        else:
            messagebox.showerror("Error", "No Image Found.")
            return

    def choose_image(self):
        if self.image:
            width, height = self.image.size
            if width * height > 1600 * 900:
                self.image = self.resize_image(width, height, 1600, 900)
            # Save rotated image
            self.image.save("process_inputs/" + self.extension)
            print(f"Saved rotated image as {'process_inputs/img.' + self.extension}")
            self.path = "process_inputs/" + self.extension
            self.root.destroy()
        else:
            messagebox.showerror("Error", "No Image Found.")
            return

    def resize_image(self, width, height, max_width, max_height):
        scale_factor = min(max_width / width, max_height / height)
        new_width = width * scale_factor
        new_height = height * scale_factor
        return self.image.resize((int(new_width), int(new_height)), PIL.Image.BILINEAR)
    def get_path(self):
        self.path =  filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
        return 

if __name__ == "__main__":
    root = Tk()
    root.title("Image Rotator")
    app = ImageRotator(root)
    root.mainloop()
