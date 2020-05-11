import pyaudio
import speech_recognition as sr
import webbrowser
import win32com.client as wincl
import os


def openGoogle():
   webbrowser.open_new_tab('www.google.com')
   speak = wincl.Dispatch("SAPI.SpVoice")
   speak.Speak('Opening Google..')

r=sr.Recognizer()
r.energy_threshold=600
print("How can i help you!!")


with sr.Microphone() as source:
   audio = r.listen(source)
   recog = r.recognize_google(audio)
   try:
      print("Speech was:" + recog)
      while(recog != 'quit' or recog != 'close'):
         if(recog.find('Google')>=0):
            openGoogle()
            print('Opening Google....')
            break
         if(recog.find('latest news') > 0):
            lib = 'latest news'
            url = "https://www.google.co.in/search?q=" +(str(lib))+ "&oq="+(str(lib))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
            webbrowser.open_new(url)
            break
         if(recog == 'log out'):
            os.system("shutdown -l")
            break
         if(recog == 'restart'):
            os.system("shutdown /r /t 1")
            break
         if(recog.find('shut down') > 0):
            os.system("shutdown /s /t 1")
            break
         if(recog.find('open python') >= 0):
            os.startfile('C:\\Users\\roope\\AppData\\Local\\Programs\\Python\\Python37\\python.exe')
            break
         if(recog.find('object') >=0):
            os.system("start \"\" https://unh.zoom.us/j/768394635?tk=63tViH65PNBD2h_Fb9hwtTtS5VQbTPUHVTvS8tcCA-c.DQEAAAAALczFixZMbmsxb184SlNYdVJPVklMRUc3R3VRAA&pwd=RlI0d0hzWnpSanpJd0FrSmM0SVc1UT09&status=success")
            break
         if(recog.find('open Eclipse') >=0):
            os.startfile('C:\\Users\\roope\\eclipse\\java-2019-06\\eclipse\\eclipse.exe')
            break
         if(recog.find('networking')>=0):
            webbrowser.open_new_tab("https://unh.zoom.us/s/7613937359?status=success")
            break
         if(recog.find('play music')>=0):
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=Rw9EiwUn4Yg&list=RDRw9EiwUn4Yg&start_radio=1")
            break
         if(recog.find('WhatsApp')>=0):
            webbrowser.open_new_tab("https://web.whatsapp.com/")
            break
         
   except LookupError:
      print('Speech not understood')   
