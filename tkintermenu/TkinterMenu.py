#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-06-02 13:38:57
# 
#    /\`.   ,'/\
#   //\\0 " 0//\\       @Last Modified by:   Your name
#  //    ,^.    \\      @Last Modified time: 2022-06-08 19:10:55
#  \\           //
#   \\         //
#

from threading import Thread
from tkinter import LEFT, X, Button, Frame, Menu
from tkinter.tix import PopupMenu


class MenuFrame(Frame):
    def __init__(self, master=None, background="grey", foreground="white") -> None:
        self.background = background
        self.foreground = foreground
        self._popup_menu = None
        self._menu_button = None
        super().__init__(master, background=self.background)
        super().pack(fill=X)
    
    def addMenuButton(self, **kwargs):
        try:
            _menu_button = _MenuButton(
            self,
            background=self.background,
            foreground=self.foreground,
            **kwargs
            )
            _menu_button.pack(side=LEFT, ipadx=5)
            return _menu_button
        except TypeError as e:
            print("ERROR: %s"%(e))
            return _MenuButton(self, **kwargs).pack(side=LEFT, ipadx=5)
    

            
    
class _MenuButton(Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._drop_down_menu = None        

    
    def createMenuDropDown(self, **kwargs):
        self._drop_down_menu = Menu(self, **kwargs)
    
    def addDropDownMenuButton(self, **kwargs):
        self._drop_down_menu.add_command(**kwargs)
        
    
    def displayDropDownButton(self, event):
        def meme():
            try:
                self._drop_down_menu.tk_popup(self.winfo_rootx(), self.winfo_rooty()+self.winfo_height())
            finally:
                self._drop_down_menu.grab_release()
        Thread(target=lambda: meme()).start()
    
    def bindDropDownMenu(self):
        self.bind("<Button-1>", self.displayDropDownButton)

            
        
        


class DropDownMenu():
    def __init__(self, master, **kwargs) -> None:
        self.master =  master
        self._drop_down_menu = Menu(self.master, **kwargs)

    def addPopupMenuButton(self, **kwargs):
        self._drop_down_menu.add_command(**kwargs)
    
    def _createPopupMenu(self, event):
        try:
            self._drop_down_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self._drop_down_menu.grab_release()
    def displayMenu(self):
        self.master.bind("<Button-1>", self._createPopupMenu)

    # def pack(self, **kwargs):
    #     super().pack()
