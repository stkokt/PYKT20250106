import tkinter as tk
from tkinter import ttk
#import idiomsFunc




# create MainWindow
mainwindow = tk.Tk()
mainwindow.geometry('600x400')
mainwindow.title('Sprichwortgenerator')
mainwindow.configure(background="#ffb366")


# create Frames and place them
upperFrm1=tk.Frame(master=mainwindow, bg="#ffb366")
upperFrm2=tk.Frame(master=mainwindow, bg="#ffb366")
middleFrm=tk.Frame(master=mainwindow, bg="#ffb366")
lowerFrm=tk.Frame(master=mainwindow, bg="#ffb366") #, bg="Red"
upperFrm1.place(relx=0, rely=0.05, relheight=0.2, relwidth=1)
upperFrm2.place(relx=0, rely=0.3, relheight=0.2, relwidth=1)
middleFrm.place(relx=0, rely=0.7, relheight=0.2, relwidth=1)
lowerFrm.place(relx=0, rely=0.9, relheight=0.1, relwidth=1)

# create Buttons and pack them
btnSaveNew=tk.Button(master=middleFrm, text="Speichern")
btnNew=tk.Button(master=lowerFrm, text="Neues Sprichwort eingeben")
btnGeneriere=tk.Button(master=lowerFrm, text="Generiere ein Sprichwort")
btnGeneriereKont=tk.Button(master=lowerFrm, text="Generiere Sprichworte")
btnNew.pack(padx=30, side= "left")
btnGeneriere.pack(padx=25, side= "left")
btnGeneriereKont.pack(padx=25, side= "left")

# generate Labels and pack/ place them
lblIdiomA=ttk.Label(master=upperFrm1, text="Viel Spaß", anchor="center", font=("Times New Roman",16,"bold", "italic"), foreground="red", background="#ffb366")
lblIdiomB=ttk.Label(master=upperFrm2, text="mit geschüttelten Sprichwörtern!", anchor="center", font=("Times New Roman",16,"bold", "italic"), background="#ffb366", foreground="red")
lblIdiomC=ttk.Label(master=middleFrm, font=("Times New Roman", 12), background="#ffb366")
lblIdiomA.place(relx=0, rely=0, relheight=1, relwidth=1)
lblIdiomB.place(relx=0, rely=0, relheight=1, relwidth=1)


# create Entry
inIdiom=tk.Entry(master=middleFrm)



def saveToDB():
    if inIdiom.get().find(';')==-1:
        lblIdiomC.config(text="Bitte Trennzeichen ';' einfügen.", foreground="red")
    else:
        btnSaveNew.pack_forget()
        lblIdiomC.pack_forget()
        inIdiom.pack_forget()

def toggleNewVisible():
    inIdiom.delete(0, len(inIdiom.get()))
    lblIdiomC.config(text='Gebe ein Sprichwort ein. Setze ein ";" (Semikolon) dort, wo es getrennt werden soll.', foreground='Black')
    if btnSaveNew.winfo_viewable() == False:        
        btnSaveNew.pack(padx=5, side="bottom", anchor="e")
        lblIdiomC.pack(side="bottom", anchor="w", padx=10)
        inIdiom.pack(side="top", anchor='w', padx=10, fill='x', expand=True )
    else:
        btnSaveNew.pack_forget()
        lblIdiomC.pack_forget()
        inIdiom.pack_forget()



btnNew.config(command=toggleNewVisible)
btnSaveNew.config(command=saveToDB)


# run
mainwindow.mainloop()

