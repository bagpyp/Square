# -*- coding: utf-8 -*-
"""
Created on Fri May 21 22:18:14 2021

@author: Dexter
"""

k = 10
screen_x,screen_y = 5,1

from tkinter import *
from random import randint
from winsound import Beep

scoot=Tk()



hero_x=7
hero_y=7 
philmo_x=randint(4,17)
philmo_y=randint(4,17)

def keydown(e):
    #this is global assignment might be a reason to consider revamping 
    #the entire program in a class frame so that keydown(e)->self.(position)=newPosition
    #class would be nice for defining player stats
    global hero_x
    global hero_y
    global philmo_x
    global philmo_y
    
    hero_movers={
        'a':(0,-1),
        'd':(0,1),
        'w':(-1,0),
        's':(1,0)}
    
    Beep(randint(50,290),randint(30,100))
    label=Label(scoot,padx=screen_x,pady=screen_y,bg=color_tuple(hero_x,hero_y,0)).grid(row=hero_y,column=hero_x)
    frame.configure(bg='#{}{}{}'.format(str(hex((5*hero_y))).zfill(2),
                    str(hex(16+int((44)**2)%256)),
                    str(hex(255-7*hero_x)).zfill(2)).replace('0x',''))
    hero_x+=hero_movers[e.char][1]
    hero_y+=hero_movers[e.char][0]
    if philmo_x<3 or philmo_y<3 or philmo_x>17 or philmo_y>17:
        philmo_x=randint(8,12)
        philmo_y=randint(8,12)
    philmo_x+=randint(-1,1)
    philmo_y+=randint(-1,1)
    philmo.grid(row=philmo_y,column=philmo_x)
    frame.grid(row=hero_y,column=hero_x)

def color_tuple(i=0,j=0,random=1):
    r = lambda x: str(hex(x*(random*randint(16,255)+i**2+j**2)%256))[2:]
    return '#' + f'{r(5)}{r(7)}{r(10)}'.zfill(6)
    
    
    
  
def keyup(e):
    Beep(randint(80,500),randint(20,70))    
frame_x=10
frame_y=10
init_color=str(hex(randint(0,255))).replace('0x','').zfill(2)
for i in range(k):
    for j in range(k*2):
        if i+j % 2 == 0:
#        label=Label(scoot,pady=screen_y,padx=screen_x,bg='#{}{}{}'.format(str(hex(16+int(i**(2))%256)).zfill(2),
#                    init_color,str(hex(16+int(j**(2))%256)).zfill(2)).replace('0x','')).grid(row=i,column=j)
            label=Label(scoot,padx=screen_x,pady=screen_y,bg=color_tuple()).grid(row=i,column=j)
        else: 
            label=Label(scoot,padx=screen_x,pady=screen_y,bg=color_tuple(i,j,0)).grid(row=i,column=j)

        
  
philmo = Frame(scoot, width=10, height=10,bg='cyan')
frame = Frame(scoot, width=10, height=10,bg='red')
frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)
philmo.bind("<KeyPress>", keydown)
frame.grid(row=hero_y,column=hero_x)
philmo.grid(column=philmo_x,row=philmo_y)
frame.focus_set()
scoot.mainloop()

    