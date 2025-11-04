import tkinter as tk
from tkinter import *
from tkinter import messagebox

project = tk.Tk()
project.geometry("800x500")
project.title("BILLIT")
project.config(background="grey")

def billing_soft():
    try:
        product_name = product_name_entry.get()
        quantity = quantity_entry.get()
        price = price_entry.get()
        quantity_value = int(quantity)
        product_price = int(price)
        total_price = quantity_value*product_price
        messagebox.showinfo("Item Added", 
                    f"Product: {product_name}\n"
                    f"Quantity: {quantity_value}\n"
                    f"Price: ₹{product_price:.2f}\n"
                    f"Item Total: ₹{total_price:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please ensure Quantity is a whole number and Price is a valid decimal number.")

#label for product_name
Label(project ,text="Enter Product Name:").pack(pady=5)
product_name_entry = Entry(project)
product_name_entry.pack(pady=5)

#label for quantity
Label(project, text="Quantity:").pack(pady=5)
quantity_entry = Entry(project)
quantity_entry.pack(pady=5)

# label for Price
Label(project, text="Price:").pack(pady=5)
price_entry = Entry(project) 
price_entry.pack(pady=5)

Button(project, text="Add Item to Bill", command = billing_soft , 
       font=('Arial', 12, 'bold'), bg='black', fg='white').pack(pady=20)

project.mainloop()