# use load the data into json file
from mydb import Database

# use display message to user
from tkinter import messagebox

from myapi import API

from tkinter import *

class NLPApp:
    def __init__(self):
        # create db object
        self.dbo = Database()
        # create api object
        self.apio = API()
        # login ka GUI load karne ke liye
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resourses/favicon.ico')
        self.root.geometry('350x520')
        self.root.configure(bg='#34495E')

        self.login_gui()

        self.root.mainloop()

    # login_gui function use to login the user
    def login_gui(self):

        self.clear_gui()

        # Help to place the Title lable on GUI
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady = (30,30))
        heading.configure(font=('verdana',24,'bold'))

        # Help to take the eamil as input from user
        lable1 = Label(self.root,text='Enter Your Email',bg='#34495E',fg='black')
        lable1.pack(pady=(10,10))
        lable1.configure(font=('verdana',12,'bold'))
        
        self.email_input = Entry(self.root,width=45)
        self.email_input.pack(pady=(5,10),ipady=4)

        # Help to take the password as input from user
        lable2 = Label(self.root,text='Enter Your Password',bg='#34495E',fg='black')
        lable2.pack(pady=(10,5))
        lable2.configure(font=('verdana',12,'bold'))

        self.password_input = Entry(self.root,width=45,show='*')
        self.password_input.pack(pady=(10,5),ipady=4)


        # Login Button create karne ke liye
        login_button = Button(self.root,text='Login',width=10,height=2,command=self.perform_login)
        login_button.pack(pady=(20,5))
        login_button.configure(font=('verdata',10,'bold'))

        # Not a member lable GUI par place karne ke liye
        lable3 = Label(self.root,text='Not a member?',bg='#34495E')
        lable3.pack(pady=(15,10))
        lable3.configure(font=('verdana',10,'bold'))

        # Register Button create karne ke liye
        redirect_button = Button(self.root,text='Register',width=10,height=2,command=self.register_gui)
        redirect_button.pack(pady=(10,15))
        redirect_button.configure(font=('verdata',10,'bold'))

    #clear_gui function use to clear GUI screen
    def clear_gui(self):
        for i in self.root.pack_slaves():
            i.destroy()

    # register_gui function use to register the user
    def register_gui(self):
        self.clear_gui()
       
         # Help to place the Title lable on GUI
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady = (30,30))
        heading.configure(font=('verdana',24,'bold'))

        # User se name input lene ke liye
        lable0 = Label(self.root,text='Enter Your Name',bg='#34495E',fg='black')
        lable0.pack(pady = (10,2))
        lable0.configure(font=('verdana',10,'bold'))

        self.name_input = Entry(self.root,width=35)
        self.name_input.pack(pady=(5,15),ipady=2)

        # Help to take the eamil as input from user
        lable1 = Label(self.root,text='Enter Your Email',bg='#34495E',fg='black')
        lable1.pack(pady=(10,10))
        lable1.configure(font=('verdana',12,'bold'))
        
        self.email_input = Entry(self.root,width=45)
        self.email_input.pack(pady=(2,15),ipady=4)

        # Help to take the password as input from user
        lable2 = Label(self.root,text='Enter Your Password',bg='#34495E',fg='black')
        lable2.pack(pady=(10,10))
        lable2.configure(font=('verdana',12,'bold'))

        self.password_input = Entry(self.root,width=45,show='*')
        self.password_input.pack(pady=(2,15),ipady=4)

        # Register button create karne ke liye
        register_button = Button(self.root, text='Register',width=8,height=1,command=self.perform_registration)
        register_button.pack()
        register_button.configure(font=('verdata',10,'bold'))

        # (Already a member) lable GUI par place karne ke liye
        lable3 = Label(self.root,text='Already a member?',bg='#34495E')
        lable3.pack(pady=(10,10))
        lable3.configure(font=('verdana',10,'bold'))

        # Redirect Button create karne ke liye
        redirect_button = Button(self.root,text='Login',width=8,height=1,command=self.login_gui)
        redirect_button.pack(pady=(5,5))
        redirect_button.configure(font=('verdata',10,'bold'))

    def perform_registration(self):
        # fetch the data from the GUI
        name = self.name_input.get()  
        email = self.email_input.get()  
        password = self.password_input.get()  
        
        response = self.dbo.app_data(name,email,password)

        if response:
            messagebox.showinfo('Success','Registration Successful. You can log now')
        else:
            messagebox.showerror('Error','Email Already Exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('success','Login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect email/password')

    # Giving options to user like SA,NER and Emotion Prediction
    def home_gui(self):
        self.clear_gui()

        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady = (30,30))
        heading.configure(font=('verdana',24,'bold'))

        sentiment_button = Button(self.root,text='Sentiment Analysis',width=20,height=3,command=self.sentiment_gui)
        sentiment_button.pack(pady=(20,10))
        sentiment_button.configure(font=('verdata',12,'bold'))

        emotion_button = Button(self.root,text='Emotion Prediction',width=20,height=3,command=self.emotion_gui)
        emotion_button.pack(pady=(10,10))
        emotion_button.configure(font=('verdata',12,'bold'))

        predict_abuse_button = Button(self.root,text='Abuse Prediction',width=20,height=3,command=self.abuse_gui)
        predict_abuse_button.pack(pady=(10,10))
        predict_abuse_button.configure(font=('verdata',12,'bold'))

        logout_button = Button(self.root,text='Logout',width=10,height=2,command=self.login_gui)
        logout_button.pack(pady=(20,10))
        logout_button.configure(font=('verdana',8,'bold'))

# sentiment analysis GUI
    def sentiment_gui(self):
        self.clear_gui()

        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady = (30,30))
        heading.configure(font=('verdana',24,'bold'))

        sub_heading = Label(self.root,text='Sentiment Analysis',bg='#34495E',fg='white')
        sub_heading.pack(pady=(10,20))
        sub_heading.configure(font=('verdana',20))

        lable1 = Label(self.root,text='Enter the Text',bg='#34495E',fg='black')
        lable1.pack(pady=(10,10))
        lable1.configure(font=('verdana',12,'bold'))

        self.sentiment_input = Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(5,10),ipady=12)

        sentiment_button = Button(self.root,text='Analyze Sentiment',width=15,height=2,command=self.do_sentiment_analysis)
        sentiment_button.pack(pady=(10,10))
        sentiment_button.configure(font=('verdana',10,'bold'))


        self.sentiment_result = Label(self.root,text='',bg='#34495E',fg='white')
        self.sentiment_result.pack(pady=(10,5))
        self.sentiment_result.configure(font=('verdana',14))

        # Button use to redirect to home page
        goback_button = Button(self.root,text='Go Back',width=10,height=2,command=self.home_gui)
        goback_button.pack(pady=(10,10))
        goback_button.configure(font=('verdana',10,'bold'))

# do_sentiment_analysis fucntion

    def do_sentiment_analysis(self):
        response = self.apio.sentiment_anlysis(self.sentiment_input)
        
        txt = ''
        for i in response['sentiment']:
            txt = txt + i + '->' + str(response['sentiment'][i]) + '\n'
            # print(i,response['sentiment'][i])

        self.sentiment_result['text'] = txt


# Emotion prediction GUI
    def emotion_gui(self):
        self.clear_gui()
        
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady = (30,15))
        heading.configure(font=('verdana',24,'bold'))

        sub_heading = Label(self.root,text='Emotion Prediction',bg='#34495E',fg='white')
        sub_heading.pack(pady=(10,10))
        sub_heading.configure(font=('verdana',20))
        
        lable1 = Label(self.root,text='Enter the Text',bg='#34495E',fg='black')
        lable1.pack(pady=(5,5))
        lable1.configure(font=('verdana',12,'bold'))

        self.emotion_input = Entry(self.root,width=50)
        self.emotion_input.pack(pady=(5,5),ipady=12)

        emotion_button = Button(self.root,text='Predict Emotion',width=15,height=2,command=self.do_emotion_prediction)
        emotion_button.pack(pady=(10,5))
        emotion_button.configure(font=('verdana',10,'bold'))

        # display result on GUI
        self.emotion_result = Label(self.root,text='',bg='#34495E',fg='white')
        self.emotion_result.pack(pady=(10,5))
        self.emotion_result.configure(font=('verdana',14))

        # Button use to redirect to home page
        goback_button = Button(self.root,text='Go Back',width=10,height=2,command=self.home_gui)
        goback_button.pack(pady=(10,10))
        goback_button.configure(font=('verdana',10,'bold'))
        
# do_emotion_prediction function 
    def do_emotion_prediction(self):
        response = self.apio.emotion_prediction(self.emotion_input)

        txt = ''
        for i in response['emotion']:
            txt = txt + i + '->' + str(round(response['emotion'][i],2)) + '\n'
            print(i,response['emotion'][i])

        self.emotion_result['text'] = txt


# Abuse Prediction GUI

    def abuse_gui(self):
        self.clear_gui()

        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady = (30,15))
        heading.configure(font=('verdana',24,'bold'))

        sub_heading = Label(self.root,text='Abuse Prediction',bg='#34495E',fg='white')
        sub_heading.pack(pady=(10,10))
        sub_heading.configure(font=('verdana',15))
        
        lable1 = Label(self.root,text='Enter the Text',bg='#34495E',fg='black')
        lable1.pack(pady=(5,5))
        lable1.configure(font=('verdana',12,'bold'))

        self.text_input = Entry(self.root,width=50)
        self.text_input.pack(pady=(5,5),ipady=12)

        check_abuse_button = Button(self.root,text='Predict Abuse',width=13,height=2,command=self.check_abuse)
        check_abuse_button.pack(pady=(10,5))
        check_abuse_button.configure(font=('verdana',10,'bold'))

        self.check_abuse_result = Label(self.root,text='',bg='#34495E',fg='white')
        self.check_abuse_result.pack(pady=(10,5))
        self.check_abuse_result.configure(font=('verdana',14))

        # Button use to redirect to home page
        goback_button = Button(self.root,text='Go Back',width=10,height=2,command=self.home_gui)
        goback_button.pack(pady=(10,10))
        goback_button.configure(font=('verdana',10,'bold'))

# is_abuse function
    def check_abuse(self):
        response = self.apio.abuse_prediction(self.text_input)
        txt = ''
        for i in response:
            txt = txt + i + '->' + str(round(response[i],4)) + '\n'
        self.check_abuse_result['text'] = txt
        print(response)
        
nlp = NLPApp()