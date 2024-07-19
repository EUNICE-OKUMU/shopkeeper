import mysql.connector
import tkinter as tk
from tkinter import *

# Function to compute profit
def compute_profit():
    selling_price = float(selling_price_entry.get())
    buying_price = float(buying_price_entry.get())
    profit = selling_price - buying_price
    profit_label.config(text=f"Profit: {profit}")

# Function to display products
def display_products():
    try:
        my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="shopkeeper"
        )
        my_conn = my_connect.cursor()

        my_conn.execute("SELECT * FROM product LIMIT 10")
        products = my_conn.fetchall()

        products_text.delete(1.0, END)
        for product in products:
            products_text.insert(END, f"Product Number: {product[0]}, Product Name: {product[1]}, Selling Price: {product[2]}, Buying Price: {product[3]}\n")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if my_connect.is_connected():
            my_conn.close()
            my_connect.close()

# Create the main window
my_w = tk.Tk()
my_w.geometry("600x400")
my_w.title("Shopkeeping Management system")

# Labels and Entry Fields
product_number_label = Label(my_w, text="Product Number:")
product_number_label.grid(row=0, column=0, padx=10, pady=10)
product_number_entry = Entry(my_w)
product_number_entry.grid(row=0, column=1, padx=10, pady=10)

product_name_label = Label(my_w, text="Product Name:")
product_name_label.grid(row=1, column=0, padx=10, pady=10)
product_name_entry = Entry(my_w)
product_name_entry.grid(row=1, column=1, padx=10, pady=10)

selling_price_label = Label(my_w, text="Selling Price:")
selling_price_label.grid(row=2, column=0, padx=10, pady=10)
selling_price_entry = Entry(my_w)
selling_price_entry.grid(row=2, column=1, padx=10, pady=10)

buying_price_label = Label(my_w, text="Buying Price:")
buying_price_label.grid(row=3, column=0, padx=10, pady=10)
buying_price_entry = Entry(my_w)
buying_price_entry.grid(row=3, column=1, padx=10, pady=10)

profit_button = Button(my_w, text="Compute Profit", command=compute_profit)
profit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
profit_label = Label(my_w, text="Profit: ")
profit_label.grid(row=5, column=0, columnspan=2)

display_products_button = Button(my_w, text="Display Products", command=display_products)
display_products_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
products_text = Text(my_w, height=10, width=60)
products_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
my_w.mainloop()
