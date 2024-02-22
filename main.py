from tkinter import *
import customtkinter
from PIL import Image, ImageTk

class HomeScreen():
    def __init__(self):
        #Screen
        self.root = customtkinter.CTk()
        self.root.geometry("500x500")
        self.root.config(bg='#190C40')

    def text(self,name):
        title_style = customtkinter.CTkFont(family="Roboto", size=42, weight="bold")
        title = Label(self.root, text=f"Hey {name} \n How can I help you?", bg=self.root.cget("bg"), font=title_style)
        title.place(relx=0.5, rely=0.27, anchor=CENTER)
    
    def gif(self):
        gifImage = "./assets/siri-bubble.gif"
        openImage = Image.open(gifImage)
        imageObject = []
        try:
            while True:
                image = openImage.copy()
                image.thumbnail((200, 200))  # Resize the image to fit within 200x200 while preserving aspect ratio
                imageObject.append(ImageTk.PhotoImage(image))
                openImage.seek(len(imageObject))
        except EOFError:
            pass

        gif_Label = Label(self.root, borderwidth=0, relief="flat")  # Setting borderwidth to 0 and relief to "flat" to remove the border
        gif_Label.place(relx=0.5, rely=0.7, anchor=CENTER)

        def update_frame(count):
                frame = imageObject[count]
                gif_Label.configure(image=frame)
                gif_Label.image = frame  # Keep a reference to avoid garbage collection
                count += 1
                if count == len(imageObject):
                    count = 0
                self.root.after(20, update_frame, count)  # Decreased interval time for smoother animation

        update_frame(0)
        self.root.mainloop()

home = HomeScreen()

home.text("David")
home.gif()