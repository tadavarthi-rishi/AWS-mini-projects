#basic GUI for Text to Speech

import tkinter as tk
import boto3



root = tk.Tk()
root.geometry("400x400")
root.title("T2S-converter Amazon Polly")
textexample = tk.Text(root,height=10)
textexample.pack()
import os
import sys
from tempfile import gettempdir
from contextlib import closing

def gettext():
    aws_mag_con = boto3.session.Session(profile_name='polly')
    client = aws_mag_con.client(service_name='polly',region_name='us-east-1')
    result = textexample.get("1.0","end")
    print(result)
    response = client.synthesize_speech(Text=result,Engine='neural',OutputFormat = 'mp3',VoiceId='Joanna')
    print(response)
    if "AudioStream" in response:
        with closing(response['AudioStream']) as stream:
            output = os.path.join(gettempdir(),"speech.mp3")
            try:
                with open(output,"wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print("AWS could not find the stream")
        sys.exit(-1)        
    if sys.platform == 'win32':
        os.startfile(output)
button = tk.Button(root,height = 1,width=10, text = 'Read',command = gettext)
button.pack()



root.mainloop()