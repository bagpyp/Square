# -*- coding: utf-8 -*-
"""
Created on Fri May 21 22:18:14 2021

@author: Dexter
"""
start = 10
k = 30
screen_x,screen_y = 5,1
a,b,c=2,3,5
from tkinter import *
from random import randint
# from winsound import Beep

scoot=Tk()



hero_x=7
hero_y=7 
philmo_x=randint(4,17)
philmo_y=randint(4,17)
s=0

def keydown(e):
    #this is global assignment might be a reason to consider revamping 
    #the entire program in a class frame so that keydown(e)->self.(position)=newPosition
    #class would be nice for defining player stats
    global hero_x
    global hero_y
    global philmo_x
    global philmo_y
    global s
    
    hero_movers={
        'a':(0,-1),
        'd':(0,1),
        'w':(-1,0),
        's':(1,0)}
    
    # Beep(randint(50,290),randint(30,100))
    # label=Label(scoot,padx=screen_x,pady=screen_y,bg=color_tuple(hero_x,hero_y,0)).grid(row=hero_y,column=hero_x)
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
    build_background()
    s+=1

def color_tuple(steps,i=0,j=0,random=1):
    r = lambda x: str(hex(x*((random*randint(16,255)+i**2+(j+steps)**2))%256))[2:]
    return '#' + f'{r(a)}{r(b)}{r(c)}'.zfill(6)
    
    
    
  
def keyup(e):
    # Beep(randint(80,500),randint(20,70))
    return    
frame_x=10
frame_y=10
# init_color=str(hex(randint(0,255))).replace('0x','').zfill(2)

def build_background():
    global s
    for i in range(start,k+start):
        for j in range(start,(k+start)*2):
                label=Label(scoot,padx=screen_x,pady=screen_y,bg=color_tuple(s, random=0, i=i, j=j)).grid(row=i,column=j)
    
build_background()

        
  
philmo = Frame(scoot, width=screen_x, height=screen_y,bg='cyan')
frame = Frame(scoot, width=screen_x, height=screen_y,bg='red')
frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)
# philmo.bind("<KeyPress>", keydown)
frame.grid(row=hero_y,column=hero_x)
philmo.grid(column=philmo_x,row=philmo_y)
frame.focus_set()
scoot.mainloop()

    