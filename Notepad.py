from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
import time

if __name__=='__main__':
    #Basic tkinter setup
    root=Tk()
    root.geometry("700x788")
    root.title("Untitled-Notepad")
    root.iconbitmap(r'notepad-icon\favicon.ico')

    #Variable Declaration
    Statusvar=StringVar()
    Statusvar.set("  Ready")
    
    #File-functions
    def NewFile():
        Statusvar.set("Creating New File")
        Statusbar.update()
        time.sleep(0.5)
        global file
        root.title("Untitled-Notepad")
        file=None
        TextArea.delete(1.0,END)
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def OpenFile():
        Statusvar.set("Opening File")
        Statusbar.update()
        time.sleep(0.5)
        global file
        file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Doccuments","*.txt")])
        if file == "":
            file=None
        else:
            root.title(os.path.basename(file)+"-Notepad")
            TextArea.delete(1.0,END)
            f=open(file,"r")
            TextArea.insert(1.0,f.read())
            f.close()
            
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def SaveFile():
        Statusvar.set("Creating New File")
        Statusbar.update()
        time.sleep(0.5)
        global file
        if file==None:
            file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Doccuments","*.txt")])

            if file=="":
                file=None
            else:
                #save as new file
                f=open(file,"w")
                f.write(TextArea.get(1.0,END))
                f.close()
                root.title(os.path.basename(file)+"-Notepad")
        else:
            #save the file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
        
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def quitApp():
        root.destroy()
        print("Exit")
    
    #Edit-Function
    def undo():
        TextArea.event_generate(("<<Undo>>"))
    def Cut():
        Statusvar.set("Cutting")
        Statusbar.update()
        time.sleep(0.5)
        TextArea.event_generate(("<<Cut>>"))
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def Copy():
        Statusvar.set("Copping")
        Statusbar.update()
        time.sleep(0.5)
        TextArea.event_generate(("<<Copy>>"))
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def Paste():
        Statusvar.set("Pasting")
        Statusbar.update()
        time.sleep(0.5)
        TextArea.event_generate(("<<Paste>>"))
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def delete():
        Statusvar.set("deleting")
        Statusbar.update()
        time.sleep(0.5)
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def Find():
        Statusvar.set("Finding")
        Statusbar.update()
        time.sleep(0.5)
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def FindNext():
        Statusvar.set("Find Next")
        Statusbar.update()
        time.sleep(0.5)
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def FindPrevious():
        Statusvar.set("Find Previous")
        Statusbar.update()
        time.sleep(0.5)
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def Replace():
        Statusvar.set("Replace")
        Statusbar.update()
        time.sleep(0.5)
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def goto():
        Statusvar.set("Goto")
        Statusbar.update()
        time.sleep(0.5)
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def selectAll():
        Statusvar.set("Select All")
        Statusbar.update()
        time.sleep(0.5)
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def Time():
        Statusvar.set("Timing")
        Statusbar.update()
        time.sleep(0.5)
        Statusvar.set("  Ready")
        Statusbar.update()
        
    #Formate-Function
    def WordWrap():
        Statusvar.set("WordWrap")
        Statusbar.update()
        time.sleep(0.5)
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def Font():
        Statusvar.set("Font")
        Statusbar.update()
        time.sleep(0.5)
        Statusvar.set("  Ready")
        Statusbar.update()
        
    
    #View-Function
    def Zoom():
        Statusvar.set("Zooming")
        Statusbar.update()
        time.sleep(0.5)
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def StatusBar():
        Statusvar.set("Status-Bar")
        Statusbar.update()
        time.sleep(0.5)
        Statusvar.set("  Ready")
        Statusbar.update()
        

    #Help-Function:
    def viewhelp():
        Statusvar.set("You clicked on help")
        Statusbar.update()
        time.sleep(0.5)
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def SendFeed():
        Statusvar.set("You Sending Feedback")
        Statusbar.update()
        time.sleep(0.5)
        Statusvar.set("  Ready")
        Statusbar.update()
        
    def About():
        Statusvar.set("You Clicked on About")
        Statusbar.update()
        time.sleep(0.5)
        messagebox.showinfo("Notepad","This Notepad is created by Satish\nVersion- 1.0\nConnect")
        Statusvar.set("  Ready")
        Statusbar.update()
    
    #Add textArea
    TextArea=Text(root,font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)

    #Menubar-File
    Menubar=Menu(root)
    filemenu=Menu(Menubar,tearoff=0)
    filemenu.add_command(label="New",command=NewFile)
    filemenu.add_command(label="Open",command=OpenFile)
    filemenu.add_command(label="Save",command=SaveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=quitApp)
    Menubar.add_cascade(label="File",menu=filemenu)

    #Edit
    Edit=Menu(Menubar,tearoff=0)
    Edit.add_command(label="Undo",command=undo)
    Edit.add_separator()
    Edit.add_command(label="Cut",command=Cut)
    Edit.add_command(label="Copy",command=Copy)
    Edit.add_command(label="Pest",command=Paste)
    Edit.add_command(label="Delete",command=delete)
    Edit.add_separator()
    Edit.add_command(label="Find",command=Find)
    Edit.add_command(label="Find Next",command=FindNext)
    Edit.add_command(label="Find Previous",command=FindPrevious)
    Edit.add_command(label="Replace",command=Replace)
    Edit.add_command(label="goto",command=goto)
    Edit.add_separator()
    Edit.add_command(label="Select all",command=selectAll)
    Edit.add_command(label="Time/Date",command=Time)
    Menubar.add_cascade(label="Edit",menu=Edit)

    #Formate
    FormateMenu=Menu(Menubar,tearoff=0)
    FormateMenu.add_command(label="Word Wrap",command=WordWrap)
    FormateMenu.add_command(label="Font..",command=Font)
    Menubar.add_cascade(label="Formate",menu=FormateMenu)

    #View
    ViewMenu=Menu(Menubar,tearoff=0)
    ViewMenu.add_command(label="Zoom",command=Zoom)
    ViewMenu.add_command(label="Status Bar",command=StatusBar)
    Menubar.add_cascade(label="View",menu=ViewMenu)

    #help
    HelpMenu=Menu(Menubar,tearoff=0)
    HelpMenu.add_command(label="Viewhelp",command=viewhelp)
    HelpMenu.add_command(label="Send Feedback",command=SendFeed)
    HelpMenu.add_command(label="About Notepad",command=About)
    Menubar.add_cascade(label="Help",menu=HelpMenu)
    root.config(menu=Menubar)

    #adding Vertical scrollbar
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    #adding Horizontal scrollbar
    """Scrollx=Scrollbar(TextArea)
    Scrollx.pack(side=BOTTOM,fill=X)
    Scrollx.config(command=TextArea.xview)
    TextArea.config(xscrollcommand=Scrollx.set)"""

    
    #Status-Bar
    Statusbar=Label(root,textvariable=Statusvar,relief=SUNKEN,anchor="w")
    Statusbar.pack(side=BOTTOM,fill=X)
    root.mainloop()
