from tkinter import ttk
from tkinter import *

import sqlite3

class product:

    db_name = 'database.db'


    def __init__(self, window):

        self.wind = window
        self.wind.title('products aplication')

        #creating frame
        frame = LabelFrame(self.wind, text = 'register a new product')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #label
        Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.grid(row = 1, column = 1)

        #Price input
        Label(frame, text = 'Price: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        #button add product
        ttk.Button(frame, text = 'Save product').grid(row = 3, columnspan = 2, sticky = W + E)

        #table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('#1', text = 'PRICE', anchor = CENTER)

        self.get_products()
        
    def run_query(self, query, parameters = ()):
        with sqlite3.connect('database.db') as conn:
            c = conn.cursor()
            result = c.execute(query, parameters)
            conn.commit()
        return result
 
    def get_products(self):
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        print(db_rows)

if __name__ == '__main__':
    window = Tk()
    application = product(window)
    window.mainloop()