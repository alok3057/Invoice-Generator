#https://www.youtube.com/watch?v=HdWIhY1n6i0
import tkinter as tk
from tkinter import ttk
from docxtpl import DocxTemplate
from tkinter import messagebox

# Create main Window and frame
window = tk.Tk()
window.title("Cyber Tec Invoice V 2.0")
window.geometry("600x500")
window.configure(bg="lightblue")
main_frame = tk.Frame(window, width=500, height=300, bg="lightblue", bd=5, relief="groove")
#main_frame.pack(pady=20) # Add some padding for better visual separation
#---------------------------------------

productList=[]

def generateInvoice():
    d= date_var.get()
    n= name_var.get()
    a=add_var.get()
    m=mobile_var.get()
    total =sum(item[3] for item in productList)
    doc = DocxTemplate("Invoice.docx")
    doc.render({"date":d,"name":n,"address":a,"mobile":m,"itemList":productList,"total":total})
    doc.save("new_invoice.docx")
    messagebox.showinfo("Success", "Invoice Printed....")

    # Exit the application
    window.destroy()
    
def addProduct():
    
    i=product_var.get()
    q=qty_var.get()
    p=price_var.get()
    t= q*p
    tabel.insert("",0, values=(i,q,p,t))
    productList.append([i,q,p,t])
    clearProductField()
    
def clearProductField():
    product_var.set("")
    qty_var.set(1)
    price_var.set(0.0)
    
    
################################    
date_label = ttk.Label(window,text="Date")
date_label.grid(row=0, column=0)
date_var= tk.StringVar()
date_entry= ttk.Entry(window,textvariable=date_var)
date_entry.grid(row=1, column=0)

################################
name_label = ttk.Label(window,text="Full Name")
name_label.grid(row=0, column=1)
name_var = tk.StringVar()
name_entry= ttk.Entry(window,textvariable=name_var)
name_entry.grid(row=1, column=1)
###################################

###################################\
add_label = ttk.Label(window,text="Full Address")
add_label.grid(row=0, column=2)
add_var = tk.StringVar()
add_entry= ttk.Entry(window,textvariable=add_var)
add_entry.grid(row=1, column=2)
##################################

#################################

mobile_label = ttk.Label(window,text="Mobile")
mobile_label.grid(row=0, column=3)
mobile_var = tk.StringVar()
mobile_entry= ttk.Entry(window,textvariable=mobile_var)
mobile_entry.grid(row=1, column=3)
###############################

###############################
product_label = ttk.Label(window,text="Product Name")
product_label.grid(row=3, column=0)
product_var = tk.StringVar()
product_entry= ttk.Entry(window,textvariable=product_var)
product_entry.grid(row=4, column=0)
################################

###############################
qty_label = ttk.Label(window,text="Quantity")
qty_label.grid(row=3, column=1)
qty_var = tk.IntVar(value=1)
qty_entry= ttk.Entry(window,textvariable=qty_var)
qty_entry.grid(row=4, column=1)
################################

###############################
price_label = ttk.Label(window,text="Price/Per Unit")
price_label.grid(row=3, column=2)
price_var = tk.DoubleVar()
price_entry= ttk.Entry(window,textvariable=price_var)
price_entry.grid(row=4, column=2)
################################

###### Add Button ################

add_button = ttk.Button(window, text="Add Product",command=addProduct)
add_button.grid(row=5, column=2 ,columnspan=3, ipadx=15, ipady=10)

new_button = ttk.Button(window, text="New Invoice")
new_button.grid(row=7, column=1 ,columnspan=3, ipadx=15, ipady=10)

genarate_button = ttk.Button(window, text="Genarate Invoice",command=generateInvoice)
genarate_button.grid(row=7, column=3 ,columnspan=3,padx=50,ipadx=15, ipady=10)

  
####################################

###########Create Table#############

tabel = ttk.Treeview(window, columns=("name","quantity","price","total"),show="headings")
tabel.grid(row=6, column=0,columnspan=3,sticky="ewns",padx=50)

tabel.heading("name",text="Name",anchor="w")
tabel.heading("quantity",text="Quantity",anchor="w")
tabel.heading("price",text="Price",anchor="w")
tabel.heading("total",text="Total",anchor="w")






    
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=6)
window.rowconfigure(7, weight=1)
window.rowconfigure(8, weight=1)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)


    
#generateInvoice()

window.mainloop()
