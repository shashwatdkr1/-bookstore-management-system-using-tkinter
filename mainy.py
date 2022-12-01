from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Bookstore Management")
root.geometry("700x500")
titleLabel = ttk.Label(root, text="Title")
titleLabel.grid(column=0, row=0, sticky=N)
title = ttk.Entry(root)
title.grid(column=1, row=0, sticky=(W, E))
authorLabel = ttk.Label(root, text="Author")
authorLabel.grid(column=2, row=0, sticky=N)
author = ttk.Entry(root)
author.grid(column=3, row=0, sticky=(W, E))
yearLabel = ttk.Label(root, text="Year")
yearLabel.grid(column=0, row=1, sticky=N)
year = ttk.Entry(root)
year.grid(column=1, row=1, sticky=(W, E))
isbnLabel = ttk.Label(root, text="ISBN")
isbnLabel.grid(column=2, row=1, sticky=N)
isbn = ttk.Entry(root)
isbn.grid(column=3, row=1, sticky=(W, E))
listbox = ttk.Treeview(root, columns=("id","title", "author", 
"year", "isbn"),show="headings")
listbox.heading("id", text="Id")
listbox.heading("title", text="Title")
listbox.heading("author", text="Author")
listbox.heading("year", text="Year")
listbox.heading("isbn", text="ISBN")
listbox.column("id", width=50)
listbox.column("title", width=100)
listbox.column("author", width=100)
listbox.column("year", width=50)
listbox.column("isbn", width=100)
listbox.insert("", 0, text="First", values=("1", "Book1", "Author1", 
"2000", "1234567890"))
listbox.insert("", 1, text="Second", values=("2", "Book2", 
"Author2", "2001", "1234567890"))
listbox.insert("", 2, text="Third", values=("3", "Book3", "Author3", 
"2002", "1234567890"))
listbox.insert("", 3, text="Fourth", values=("4", "Book4", 
"Author4", "2003", "1234567890"))
listbox.insert("", 4, text="Fifth", values=("5", "Book5", "Author5", 
"2004", "1234567890"))
listbox.insert("", 5, text="Sixth", values=("6", "Book6", "Author6", 
"2005", "1234567890"))
listbox.insert("", 6, text="Seventh", values=("7", "Book7", 
"Author7", "2006", "1234567890"))
listbox.insert("", 7, text="Eighth", values=("8", "Book8", 
"Author8", "2007", "1234567890"))
listbox.insert("", 8, text="Ninth", values=("9", "Book9", "Author9", 
"2008", "1234567890"))
listbox.insert("", 9, text="Tenth", values=("10", "Book10", 
"Author10", "2009", "1234567890"))
listbox.insert("", 10, text="Eleventh", values=("11", "Book11", 
"Author11", "2010", "1234567890"))
listbox.grid(column=0, row=2, columnspan=2,rowspan=5, sticky=(N, W, 
E, S))
scrollbar = ttk.Scrollbar(root, orient=VERTICAL, 
command=listbox.yview)
scrollbar.grid(column=2, row=2, sticky=(N, S),rowspan=5)
listbox.configure(yscrollcommand=scrollbar.set)
addButton = ttk.Button(root, text="Add")
addButton.grid(column=3, row=3, sticky=(W, E))
updateButton = ttk.Button(root, text="Update")
updateButton.grid(column=3, row=4, sticky=(W, E))
deleteButton = ttk.Button(root, text="Delete")
deleteButton.grid(column=3, row=5, sticky=(W, E))
closeButton = ttk.Button(root, text="Close")
closeButton.grid(column=3, row=6, sticky=(W, E))
root.mainloop()