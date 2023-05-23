import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

my_window = tk.Tk()
my_window.geometry("1000x1000")
my_window.title("AWS Textract")
label1 = tk.Label(my_window, text = "Upload an image", width = 30, font =('times',18,'bold'))
label1.pack()
button1 = tk.Button(my_window ,text='Upload File and see what it has!!!',width = 30, command =lambda:upload_file())
button1.pack()

#writing function to upload file
def upload_file():
    global img
    file_types = [['All Files','*.jpg']]
    filename = filedialog.askopenfile(filetypes = file_types)
    img = Image.open(filename, format = 'JPEG')
    #resizing the image
    img_resize = img.resize((400,200))
    img = ImageTk.PhotoImage(img_resize)
    
    b2=tk.Button(my_window, image = img)
    b2.pack()


    
    
    

my_window.mainloop()

