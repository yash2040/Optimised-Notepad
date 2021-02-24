import os
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import HuffmanCoding
def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    textArea.delete(1.0,END)

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        textArea.delete(1.0,END)
        f=open(file,"r")
        originalText=f.read()
        #decrypt OriginalText

        textArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",
                               defaultextension=".txt",
                               filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            #Save as a new file
            f=open(file,"w")
            originalText=textArea.get(1.0,"end-1c")
            codes=HuffmanCoding.init(originalText)

            tempFileLoc = str(file).split('.')[0] + "secret1" + ".txt"
            tempFile = open(tempFileLoc, 'w')
            tempFile.write(str(codes))
            tempFile.close()

            encryptedText=''
            for i in originalText:
                encryptedText=encryptedText+str(codes[i])
            #encryptOriginalText
            f.write(encryptedText)
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
            #File Saved
    else:
        # Save the file
        f = open(file, "w")
        originalText = textArea.get(1.0, "end-1c")

        codes=HuffmanCoding.init(originalText)

        tempFileLoc=str(file).split('.')[0]+"secret1"+".txt"
        tempFile = open(tempFileLoc , 'w')
        tempFile.write(str(codes))
        tempFile.close()

        encryptedText = ''
        for i in originalText:
            encryptedText = encryptedText + str(codes[i])
        # encryptOriginalText
        f.write(encryptedText)
        # encryptOriginalText

        f.close()

def quitApp():
    root.destroy()

def cut():
    textArea.event_generate("<<Cut>>")

def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")

def about():
    showinfo("Notepad","Notepad By Yash Khandelwal")

if __name__ == '__main__':
    root=Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x788")

    #Adding Text Area
    textArea=Text(root,font="lucida 13")
    textArea.pack(expand=True,fill=BOTH)
    file=None

    #Creating a Menu Bar
    menuBar=Menu(root)


    #FileMenu starts
    fileMenu=Menu(menuBar,tearoff=0)

    #Open a new file
    fileMenu.add_command(label="New",command=newFile)

    #Open an Existing file
    fileMenu.add_command(label="Open",command=openFile)

    #Save the currentFile
    fileMenu.add_command(label="Save",command=saveFile)

    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",command=quitApp)
    menuBar.add_cascade(label="File",menu=fileMenu)
    #File Menu ends

    #Edit Menu
    editMenu=Menu(menuBar,tearoff=0)

    #Cut,Copy,Paste feature
    editMenu.add_command(label="Cut",command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)

    menuBar.add_cascade(label="Edit",menu=editMenu)
    #Edit Menu ends

    #Help Menu starts
    helpMenu=Menu(menuBar,tearoff=0)
    helpMenu.add_command(label="About Notepad",command=about)

    menuBar.add_cascade(label="Help",menu=helpMenu)
    #Help Menu ends

    root.config(menu=menuBar)

    #Adding ScrollBar
    scrollBar=Scrollbar(textArea)
    scrollBar.pack(side=RIGHT,fill=Y)
    scrollBar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scrollBar.set)

    root.mainloop()