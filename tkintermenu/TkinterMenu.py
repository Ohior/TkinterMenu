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
        'add button to the menu frame'
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
        '''
        create menu drop down popup window, 
        always call this first before when
         you are creating a drop down window
        '''
        self._drop_down_menu = Menu(self, **kwargs)
    
    def addDropDownMenuButton(self, **kwargs):
        '''
        Add a label and command for the window
        self.addDropDownMenuButton(label="menu name", command=lambda: function())
        '''
        self._drop_down_menu.add_command(**kwargs)
        
    
    def _displayDropDownButton(self, event):
        '''
        this displays the drop down window, 
        also a thread is created so that the 
        menu click is animated correctly
        '''
        def meme():
            try:
                self._drop_down_menu.tk_popup(self.winfo_rootx(), self.winfo_rooty()+self.winfo_height())
            finally:
                self._drop_down_menu.grab_release()
        Thread(target=lambda: meme()).start()
    
    def bindDropDownMenu(self):
        '''
        alway call this last after you are through adding 
        and creating your drop down menu.
        this binds the drop down menu to the right menu button 
        '''
        self.bind("<Button-1>", self._displayDropDownButton)

            
        
        


