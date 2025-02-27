# Book Tracker

Book Tracker is a simple application to keep track of books you have read or want to read. It allows you to add, edit, delete, and search for books in your collection. The application uses a SQLite database to store book information and features a modern user interface with `ttk` widgets and additional styling.

## Features

- Add new books with title and author
- Edit existing book details
- Delete books from the collection
- Search for books by title or author
- Modern user interface with `ttk` widgets
- Background image and custom styling

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Pillow (for image handling)
- SQLite (usually included with Python)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/book-tracker.git
    cd book-tracker
    ```

2. Install the required packages:
    ```bash
    pip install pillow
    ```

3. Place a background image named `background.png` in the project directory, or update the path to your image in the code.

## Usage

1. Run the application:
    ```bash
    python book_tracker.py
    ```

2. Use the interface to add, edit, delete, and search for books.

## Project Structure

- `book_tracker.py`: Main application code
- `database.py`: Database operations module
- `background.png`: Background image (included in the repository)

## Code Overview

### `book_tracker.py`

This file contains the main application code, including the user interface and event handling. It uses the `Database` class from `database.py` to interact with the SQLite database.

### `database.py`

This file contains the `Database` class, which handles all database operations such as creating tables, adding, updating, deleting, and searching for books.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
