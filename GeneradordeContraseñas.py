import random
from string import punctuation
from tkinter import *
import tkinter

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here


def randomPassword():
  entry.delete("1.0","end")
  uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
  uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
  lowercaseLetter1=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
  lowercaseLetter2=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
  digit1=chr(random.randint(48,57))
  digit2=chr(random.randint(48,57))
  punctuationSign1=chr(random.randint(33, 64))
  punctuationSign2=chr(random.randint(33, 64))
  password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
  shuffle(password)
  entry.insert(tkinter.END,password)

#Generate password using all the characters, in random order



#Main Window
Pass = Tk()
Pass.title("Generador de Contraseñas")
Pass['bg']='Yellow'
Pass.resizable(0,0)


label=Label(Pass, text="Generador de Contraseñas", font=('arial',30,'bold'),
			bg='Yellow', fg='#000000', justify= 'right').grid(row=0,columnspan=16)

entry=Text(Pass,width=48,font=('arial',12,'bold'))
entry.grid(row=18,columnspan=21)


Accion = tkinter.Button(Pass,text='Generar Contraseña', width=18,bg='Yellow', fg='#000000',
					   activebackground="#ffffff", activeforeground='#000990',relief='raised',
					   padx=14, pady=10 , bd=12,font=('arial',10,'bold'),
					   command=randomPassword).grid(row=21,column=7)


#Ouput

Pass.mainloop()
