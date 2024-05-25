from tkinter import *
import PIL.Image, PIL.ImageTk
import tkinter.messagebox as messagebox


class ImageRotator:
    def __init__(self, root):
        self.root = root

        # Create an entry widget for the image path
        self.path_entry = Entry(root)
        self.path_entry.pack()

        # Create buttons
        self.load_button = Button(root, text="Load Image", command=self.load_image)
        self.rotate_button = Button(root, text="Rotate 90°", command=self.rotate_image)
        self.save_button = Button(root, text="Save Image", command=self.save_image)
        self.load_button.pack()
        self.rotate_button.pack()
        self.save_button.pack()

        # Initialize image variables
        self.path = None
        self.image = None
        self.tk_image = None
        self.root.geometry("800x600")

    def load_image(self):
        # Get the image path from the entry widget
        path = self.path_entry.get()
        if not path:
            messagebox.showerror("Error", "Please enter a valid image path.")
            return

        try:
            # Load image
            self.image = PIL.Image.open(path)
            self.path = path
            w, h = self.image.size
            print(w, h)
            self.tk_image = PIL.ImageTk.PhotoImage(self.image)
            self.root.geometry(f"{w}x{h}")
            # Display image
            self.image_label = Label(self.root, image=self.tk_image)
            self.image_label.pack()
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"Error loading image: {str(e)}")

    def rotate_image(self):
        if self.image:
            # Rotate 90 degrees
            self.image = self.image.rotate(90)
            self.tk_image = PIL.ImageTk.PhotoImage(self.image)

            # Update displayed image
            self.image_label.config(image=self.tk_image)
        else:
            messagebox.showerror("Error", "No Image Found.")
            return

    def save_image(self):
        if self.image:
            width, height = self.image.size
            if width * height > 1800 * 1000:
                self.image = self.resize_image(width, height, 1800, 1000)
            # Save rotated image
            self.image.save("process_" + self.path)
            print(f"Saved rotated image as {'process_' + self.path}")
            self.path = "process_" + self.path
            self.root.destroy()
        else:
            messagebox.showerror("Error", "No Image Found.")
            return

    def resize_image(self, width, height, max_width, max_height):
        scale_factor = min(max_width / width, max_height / height)
        new_width = width * scale_factor
        new_height = height * scale_factor
        return self.image.resize((int(new_width), int(new_height)), PIL.Image.BILINEAR)


if __name__ == "__main__":
    root = Tk()
    root.title("Image Rotator")
    app = ImageRotator(root)
    root.mainloop()
