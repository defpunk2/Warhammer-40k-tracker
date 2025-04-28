import pandas as p
import math as m
import tkinter as tk
window = tk.Tk()

class game_record_inplay:
    
    
    def __init__(self):
        self.titlefont = "Impact 13"
        
        
    def layout(self):
        keywords = ["Faction","Player Name","Detachment","Vp 1","Cp 1","Vp 2","Cp 2","Vp 3","Cp 3","Vp 4","Cp 4","Vp 5","Cp 5"]
        keywords_posx = 200
        keywords_posy = 200
        values_posy = [300,500]
        values_posx = 175
        add = 100
        flipbit = 0
        
        player1_label = tk.Label(master=window,text="Player 1", font = self.titlefont)
        player1_label.place(x = 100, y=295)
        player2_label = tk.Label(master=window,text="Player 2", font = self.titlefont)
        player2_label.place(x = 100, y=495)
        for keyword in keywords:
            factiontypes_label = tk.Label(master=window,text=keyword, font = self.titlefont)
            factiontypes_label.place(x=keywords_posx,y=keywords_posy)
            keywords_posx += 100
        
         
        self.faction1 = tk.Entry(master=window, fg = "gray",width = 15)
        self.faction1.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.player1 = tk.Entry(master=window, fg = "gray",width = 15)
        self.player1.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.detachment1 = tk.Entry(master=window, fg = "gray",width = 15)
        self.detachment1.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Vp1_p1 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Vp1_p1.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Cp1_p1 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Cp1_p1.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Vp2_p1 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Vp2_p1.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Cp2_p1 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Cp2_p1.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Vp3_p1 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Vp3_p1.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Cp3_p1 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Cp3_p1.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Vp4_p1 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Vp4_p1.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Cp4_p1 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Cp4_p1.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Vp5_p1 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Vp5_p1.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Cp5_p1 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Cp5_p1.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        p1enterbutton = tk.Button(master = window,text = "<--",fg = "gray",command = self.getvalue1_store)
        p1enterbutton.place(x=values_posx, y=values_posy[flipbit])
        flipbit = 1
        values_posx = 175
        self.faction2 = tk.Entry(master=window, fg = "gray",width = 15)
        self.faction2.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.player2 = tk.Entry(master=window, fg = "gray",width = 15)
        self.player2.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.detachment2 = tk.Entry(master=window, fg = "gray",width = 15)
        self.detachment2.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Vp1_p2 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Vp1_p2.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Cp1_p2 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Cp1_p2.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Vp2_p2 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Vp2_p2.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Cp2_p2 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Cp2_p2.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Vp3_p2 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Vp3_p2.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Cp3_p2 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Cp3_p2.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Vp4_p2 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Vp4_p2.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Cp4_p2 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Cp4_p2.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Vp5_p2 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Vp5_p2.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        self.Cp5_p2 = tk.Entry(master=window, fg = "gray",width = 15)
        self.Cp5_p2.place(x=values_posx,y=values_posy[flipbit])
        values_posx += add
        p2enterbutton = tk.Button(master = window,text = "<--",fg = "gray",command = self.getvalue2_store)
        p2enterbutton.place(x=values_posx, y=values_posy[flipbit])
        
    def getvalue1_store(self):
        lst = []
        lst.append(self.faction1.get())
        lst.append(self.player1.get())
        lst.append(self.detachment1.get())
        lst.append(self.Vp1_p1.get())
        lst.append(self.Cp1_p1.get())
        lst.append(self.Vp2_p1.get())
        lst.append(self.Cp2_p1.get())
        lst.append(self.Vp3_p1.get())
        lst.append(self.Cp3_p1.get())
        lst.append(self.Vp4_p1.get())
        lst.append(self.Cp4_p1.get())
        lst.append(self.Vp5_p1.get())
        lst.append(self.Cp5_p1.get())
        print(lst)

            
    def getvalue2_store(self):
        lst = []
        lst.append(self.faction2.get())
        lst.append(self.player2.get())
        lst.append(self.detachment2.get())
        lst.append(self.Vp1_p2.get())
        lst.append(self.Cp1_p2.get())
        lst.append(self.Vp2_p2.get())
        lst.append(self.Cp2_p2.get())
        lst.append(self.Vp3_p2.get())
        lst.append(self.Cp3_p2.get())
        lst.append(self.Vp4_p2.get())
        lst.append(self.Cp4_p2.get())
        lst.append(self.Vp5_p2.get())
        lst.append(self.Cp5_p2.get())
        print(lst)

        
        
inst = game_record_inplay()
inst.layout()