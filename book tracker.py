import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3

# Initialize the main application window
class BookTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Tracker")
        self.create_widgets()
        self.setup_database()
        self.load_books()

    def create_widgets(self):
        # Create main window widgets
        self.title_label = tk.Label(self.root, text="Book Tracker", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Book", command=self.open_add_book_window)
        self.add_button.pack(pady=5)

        self.book_listbox = tk.Listbox(self.root)
        self.book_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def open_add_book_window(self):
        # Create a new window for adding a book
        self.add_book_window = tk.Toplevel(self.root)
        self.add_book_window.title("Add Book")

        self.title_entry_label = tk.Label(self.add_book_window, text="Title:")
        self.title_entry_label.pack(pady=5)
        self.title_entry = tk.Entry(self.add_book_window)
        self.title_entry.pack(pady=5)

        self.author_entry_label = tk.Label(self.add_book_window, text="Author:")
        self.author_entry_label.pack(pady=5)
        self.author_entry = tk.Entry(self.add_book_window)
        self.author_entry.pack(pady=5)

        self.save_button = tk.Button(self.add_book_window, text="Save", command=self.save_book)
        self.save_button.pack(pady=10)

    def setup_database(self):
        # Connect to the SQLite database
        self.conn = sqlite3.connect('books.db')
        self.cursor = self.conn.cursor()
        # Create the books table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def save_book(self):
        # Save the book details to the database
        title = self.title_entry.get()
        author = self.author_entry.get()
        if title and author:
            self.cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
            self.conn.commit()
            self.book_listbox.insert(tk.END, f"{title} by {author}")
            self.add_book_window.destroy()
        else:
            tk.messagebox.showerror("Error", "Please enter both title and author")

    def load_books(self):
        # Load books from the database
        self.cursor.execute('SELECT title, author FROM books')
        for row in self.cursor.fetchall():
            self.book_listbox.insert(tk.END, f"{row[0]} by {row[1]}")

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BookTrackerApp(root)
    root.mainloop()