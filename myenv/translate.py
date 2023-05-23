import tkinter as tk
import boto3



root = tk.Tk()
root.geometry("400x240")
root.title("AWS Translator")
textexample = tk.Text(root,height=10)
textexample.pack()

def getText():
    aws_mag_con = boto3.session.Session(profile_name='polly')
    client = aws_mag_con.client(service_name='translate',region_name='us-east-1')
    result = textexample.get("1.0","end")
    print(result)
    response = client.translate_text(Text=result,SourceLanguageCode='en',TargetLanguageCode='de')
    print('Translated Text: '+ response.get('TranslatedText'))
    print('source language code: '+ response.get('SourceLanguageCode'))
    print('target language code: '+ response.get('TargetLanguageCode'))
    
btnRead = tk.Button(root,height=1,width=10,text="Read",command=getText)
btnRead.pack()
root.mainloop()
