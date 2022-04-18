# projet pendu #
#import tkinter#
from tkinter import *
# creation fenetre #
windows_first = Tk()


windows_first.title("le pendu ultime")
windows_first.geometry("1080x720")
windows_first.minsize(480,360)
windows_first.iconbitmap("image convertis.ico")
windows_first.config(background = '#5C1CEC')
# creation frame #
Frame = Frame(windows_first, bg = '#5C1CEC', bd = 1, relief = SUNKEN)
# personalisation #
Label_title = Label(Frame, text="bienvenue sur le jeu ultime du pendu", font=("courrier", 71), bg = '#4E4C4C', fg ='white')
Label_title.pack()
Label_sub_title = Label(Frame, text="cliquer sur le bouton commmencer pour demarer la partie", font=("courrier", 40), bg = '#4E4C4C', fg ='white')
Label_sub_title.pack()
# les bouttons
button1 = Button(Frame, text = "start",font = ("courrier", 20), bg = '#4E4C4C', fg ='black', command= quit)
button1.pack(pady=25)
def action_arreter():
    button2 = Button(Frame, text= "quit",font = ("courrier", 20), bg = '#4E4C4C', fg ='black',command= action_arreter)
    button2.pack(pady=25)
Frame.pack( expand = YES)
# interaction #




windows_first.mainloop()



 