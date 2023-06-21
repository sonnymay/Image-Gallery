import tkinter as tk
from PIL import Image, ImageTk
import os

class ImageGallery(tk.Tk):
    def __init__(self, image_files):
        super().__init__()
        self.image_files = image_files
        self.index = 0
        
        # Load the first image
        image = Image.open(self.image_files[self.index])
        self.photo = ImageTk.PhotoImage(image)
        
        # Create a label to display the image
        self.image_label = tk.Label(self, image=self.photo)
        self.image_label.pack()
        
        # Create buttons to navigate through images
        tk.Button(self, text="<<", command=self.prev_image).pack(side="left")
        tk.Button(self, text=">>", command=self.next_image).pack(side="right")

    def prev_image(self):
        # Go to the previous image
        self.index = (self.index - 1) % len(self.image_files)
        self.update_image()
        
    def next_image(self):
        # Go to the next image
        self.index = (self.index + 1) % len(self.image_files)
        self.update_image()
    
    def update_image(self):
        # Update the photo in the label
        image = Image.open(self.image_files[self.index])
        new_photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=new_photo)
        self.image_label.image = new_photo
        

if __name__ == "__main__":
    # Get list of image files
    image_files = ["images/" + img for img in os.listdir("images/") if img.endswith((".png", ".jpg", ".gif"))]
    
    # Create the image gallery
    gallery = ImageGallery(image_files)
    gallery.mainloop()
