from tkinter import *
import tkinter.messagebox
import pandas as pd
import tkinter.font as font

#button clear action
def clearEntry():
    entName.delete(0,END)
    entId_Number.delete(0,END)
    entTemperature.delete(0,END)
    entDate.delete(0,END)

#create action for submitting form data to database
def submitForm():
    
    path = 'excel.xlsx'
    df1 = pd.read_excel(path)

    SeriesA = df1['Name']
    SeriesB = df1['Id']
    SeriesC = df1['Temp']
    SeriesD = df1['Date']
    
    
    Name = pd.Series(entName.get())
    Id = pd.Series(entId_Number.get())
    Temp = pd.Series(entTemperature.get())
    Date = pd.Series(entDate.get())

    SeriesA = SeriesA.append(Name)
    SeriesB = SeriesB.append(Id)
    SeriesC = SeriesC.append(Temp)
    SeriesD = SeriesD.append(Date)
    

    df2 = pd.DataFrame({"Name":SeriesA, "Id":SeriesB,"Temp":SeriesC,"Date":SeriesD})



    df2.to_excel(path, index=False)

    temp1=float(entTemperature.get())

    if temp1 > 37.5:
       tkinter.messagebox.showinfo("Recoded", "High Risk. Tempereture is to high. Not be allowed to enter class. ")
    else:
        tkinter.messagebox.showinfo("Recorded", "Low risk. Allowed to enter the class.")
            
    #show message box for successful query
    #tkinter.messagebox.showinfo("Success", "Data inserted successfully.")
    
    #clear the form after button is hit & show existing data
    clearEntry()


#creating main window
root = Tk()
root.title("Attendent Record")
root.geometry("800x800")

#set window colour
root['background']='#e2ef90'

#creating LabelFrame
group1 = LabelFrame(root, borderwidth=5, text="Student Record",bg='#c5d36c',fg='#684400',padx=150,pady=50)
myFont = font.Font(family='Times New Roman', size=30)
group1 ['font']= myFont

#creating a label widget
lblTitle = Label(root,borderwidth=10, text = "Welcome Student",bg='#c5d36c',fg='#684400',padx=140)
myFont = font.Font(family='Castellar', size=35, weight='bold')
lblTitle ['font']= myFont
lblTitle.pack()

#creating frame widget for buttons
buttongroup = Frame(root)
#creating button widget
btnSave = Button(buttongroup, text="Save", command=submitForm)
btnClear = Button(buttongroup, text="Clear", command=clearEntry)


#showing it onto the screen
#myLabel.pack()  #using pack
#using grid layout
lblTitle.grid(row=0, column=0, columnspan=2)
group1.grid(row=1, column=0, padx=55,pady=100)
lblName.grid(row=2, column=0,pady=10)
lblId_Number.grid(row=4, column=0,pady=10)
lblTemperature.grid(row=6, column=0,pady=10)
lblDate.grid(row=8, column=0,pady=10)
lblformat.grid(row=9,column=1,pady=0)
entName.grid(row=2, column=1)
entId_Number.grid(row=4, column=1)
entTemperature.grid(row=6, column=1)
entDate.grid(row=8, column=1)
buttongroup.grid(row=60, column=0)
btnSave.grid(row=7, column=0)
btnClear.grid(row=7, column=1)
lblformat1.grid(row=3,column=1,pady=0)
lblformat2.grid(row=5,column=1,pady=0)
lblformat3.grid(row=7,column=1,pady=0)





#call the mainloop of tk
root.mainloop()
