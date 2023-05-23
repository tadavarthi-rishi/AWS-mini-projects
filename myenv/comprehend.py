import tkinter as tk
import boto3



root = tk.Tk()
root.geometry("400x240")
root.title("Sentiment Analysis")
textexample = tk.Text(root,height=10)
textexample.pack()

def getText():
    aws_mag_con = boto3.session.Session(profile_name='polly')
    client = aws_mag_con.client(service_name='comprehend',region_name='us-east-1')
    result = textexample.get("1.0","end")
    print(result)
    response = client.detect_sentiment(Text=result,LanguageCode='en')
    print('The prominant sentiment is: ',response['Sentiment'])
    print('The SentimentScore is:',response['SentimentScore'])
    
btnRead = tk.Button(root,height=1,width=10,text="Read",command=getText)
btnRead.pack()
root.mainloop()
