import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import boto3

my_window = tk.Tk()
my_window.geometry("450x400")
my_window.title("AWS Textract")
label1 = tk.Label(my_window, text = "Upload an image", width = 30, font =('times',18,'bold'))
label1.pack()
button1 = tk.Button(my_window ,text='Upload File and see what it has!!!',width = 30, command =lambda:upload_file())
button1.pack()

#writing function to upload file
def upload_file():
    aws_mag_con = boto3.session.Session(profile_name = 'polly')
    client = aws_mag_con.client(service_name='textract',region_name='us-east-1',)
    global img
    file_types = [('All Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=file_types)
    img = Image.open(filename)
    #resizing the image
    img_resize = img.resize((400,200))
    img = ImageTk.PhotoImage(img_resize)
    imgbytes = get_image_byte(filename)
    
    b2=tk.Button(my_window, image = img)
    b2.pack()
    response = client.detect_document_text(Document = {'Bytes':imgbytes})
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            print(item['Text'])
    
def get_image_byte(filename):
    with open(filename,'rb') as imgfile:
        return imgfile.read()
        

my_window.mainloop()
