# Library Management System

**Project Name:** Library Management System  
**Student Name:** Ahmad Salem Khan  
**Registration Number:** 25BAI11418  
**Course:** B.Tech Computer Science and Engineering  
**Institution:** VIT Bhopal University  
**Professor:** Dr. Preetam Suman  
**Date:** 24 November 2025

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [System Requirements](#system-requirements)
4. [Installation and Setup](#installation-and-setup)
5. [Usage Guide](#usage-guide)
6. [Project Structure](#project-structure)
7. [Screenshots](#screenshots)
8. [Technical Implementation](#technical-implementation)
9. [Future Enhancements](#future-enhancements)
10. [Contributors](#contributors)
11. [License](#license)

---

## Project Overview

The **Library Management System** is a console-based Python application designed to streamline library operations through digital management of book records. This system provides an efficient solution for managing library inventory, enabling users to perform essential operations such as adding books, viewing available inventory, searching for specific titles, and removing books from the collection.

### Problem Statement

Traditional manual library management systems are time-consuming, prone to errors, and difficult to scale. This project addresses these challenges by providing a computerized solution that ensures accuracy, speed, and ease of use in managing library resources.

### Objectives

- Develop a user-friendly console-based library management application
- Implement CRUD (Create, Read, Update, Delete) operations for book records
- Provide efficient search functionality for quick book retrieval
- Ensure data integrity through proper input validation
- Create a scalable foundation for future database integration

### Scope

This project focuses on the fundamental operations of library management:
- Book inventory management
- Search and retrieval functionality
- User-friendly menu-driven interface
- In-memory data storage using Python data structures

---

## Features

### Core Functionalities

1. **Add Book**
   - Capture book title, author name, and publication year
   - Store book information in a structured dictionary format
   - Provide confirmation upon successful addition

2. **Show All Books**
   - Display complete library inventory
   - Present books in a formatted, numbered list
   - Show book count and availability status

3. **Search Book**
   - Case-insensitive title-based search
   - Display detailed information for matching books
   - Provide "not found" notification for unavailable titles

4. **Delete Book**
   - Remove books by title search
   - Confirm successful deletion
   - Handle cases where the book doesn't exist

5. **Exit**
   - Gracefully terminate the application
   - Display farewell message

### Key Highlights

- **User-Friendly Interface:** Clean, menu-driven console interface
- **Data Validation:** Proper handling of user inputs and edge cases
- **Efficient Search:** Quick title-based search with case-insensitive matching
- **Modular Design:** Function-based architecture for maintainability
- **Error Handling:** Appropriate messages for invalid operations

---

## System Requirements

### Hardware Requirements

- **Processor:** Intel Core i3 or equivalent (minimum)
- **RAM:** 2 GB or higher
- **Storage:** 50 MB free disk space
- **Display:** Standard monitor with 1024x768 resolution

### Software Requirements

- **Operating System:** Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python Version:** Python 3.6 or higher
- **IDE/Editor:** VS Code, PyCharm, IDLE, or any Python-compatible editor
- **Terminal:** Command Prompt, PowerShell, or Unix Terminal

---

## Installation and Setup

### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer and ensure "Add Python to PATH" is checked
3. Verify installation by running:
   ```bash
   python --version
   ```

### Step 2: Download Project Files

1. Clone or download the project repository
2. Extract files to your preferred directory
3. Ensure `code.py` is in the project folder

### Step 3: Run the Application

Navigate to the project directory and execute:

```bash
python code.py
```

Or using Python 3 explicitly:

```bash
python3 code.py
```

---

## Usage Guide

### Starting the Application

1. Open terminal/command prompt
2. Navigate to project directory
3. Run `python code.py`
4. The main menu will be displayed

### Menu Options

#### Option 1: Add Book

1. Select option `1` from the main menu
2. Enter book title when prompted
3. Enter author name
4. Enter publication year
5. System confirms successful addition

**Example:**
```
Choose option (1-5): 1
Enter book title: Crime and Punishment
Enter author name: Fyodor Dostoevsky
Enter publication year: 1866
Book added successfully!
```

#### Option 2: Show All Books

1. Select option `2` from the main menu
2. System displays all books with details
3. If no books exist, appropriate message is shown

**Example Output:**
```
There are 1 book(s) in the library:

1. Title  : Crime and Punishment
   Author : Fyodor Dostoevsky
   Year   : 1866
```

#### Option 3: Search Book

1. Select option `3` from the main menu
2. Enter the title to search
3. System displays book details if found

**Example:**
```
Choose option (1-5): 3
Enter title to search: Crime and Punishment

Book found!
Title  : Crime and Punishment
Author : Fyodor Dostoevsky
Year   : 1866
```

#### Option 4: Delete Book

1. Select option `4` from the main menu
2. Enter the title to delete
3. System confirms deletion or notifies if not found

#### Option 5: Exit

1. Select option `5` to exit
2. Application closes with farewell message

---

## Project Structure

```
LibraryManagementSystem/
│
├── code.py                          # Main Python application file
├── README.md                        # Project documentation (this file)
├── DOCUMENTATION.md                 # Detailed technical documentation
├── Screenshots/
│   ├── Screenshot-2025-11-22-at-9.47.39-PM.jpg    # Main menu interface
│   ├── Screenshot-2025-11-22-at-9.48.10-PM.jpg    # Add and Show Books demo
│   └── Screenshot-2025-11-22-at-9.48.57-PM.jpg    # Application execution
└── Flowcharts/
    └── system_flowchart.png         # System workflow diagram
```

---

## Screenshots

### Main Code
The system displays a clean, formatted menu with five options for user interaction.

![Main Menu](https://github.com/SalemKhan1242/Library-Management-System/blob/main/Project-Screenshots/WhatsApp%20Image%202025-11-23%20at%2011.14.38%20PM.jpeg)

![Add and Show Books](https://github.com/SalemKhan1242/Library-Management-System/blob/main/Project-Screenshots/WhatsApp%20Image%202025-11-23%20at%2011.14.21%20PM.jpeg)

### Code Execution
Shows the complete workflow of the application including menu navigation and user interactions.

![Application Execution](https://github.com/SalemKhan1242/Library-Management-System/blob/main/Project-Screenshots/WhatsApp%20Image%202025-11-23%20at%2011.13.50%20PM.jpeg)

---

## Technical Implementation

### Programming Language
- **Python 3.x** - Chosen for its simplicity, readability, and extensive built-in data structures

### Data Structures Used

1. **List (`library`)** - Stores all book records in memory
2. **Dictionary (`book`)** - Represents individual book with key-value pairs:
   - `"title"`: Book title (string)
   - `"author"`: Author name (string)
   - `"year"`: Publication year (string)

### Key Functions

| Function Name | Purpose | Parameters | Return Type |
|---------------|---------|------------|-------------|
| `add_book()` | Adds new book to library | None | None |
| `show_books()` | Displays all books | None | None |
| `search_book()` | Searches for a book by title | None | None |
| `delete_book()` | Removes a book from library | None | None |

### Control Flow
- **Main Loop:** `while True` - Continuous menu display until exit
- **Conditional Statements:** `if-elif-else` - Menu option selection
- **Iteration:** `for` loops - Displaying and searching books
- **String Methods:** `.lower()` - Case-insensitive comparison

---

## Future Enhancements

### Phase 1: Database Integration
- Implement SQLite/MySQL for persistent storage
- Add data backup and recovery features

### Phase 2: Advanced Features
- User authentication and role-based access control
- Book issuing and return tracking
- Fine calculation for late returns
- Member management system

### Phase 3: GUI Development
- Develop graphical interface using Tkinter or PyQt
- Add data visualization for library statistics
- Implement barcode/QR code scanning

### Phase 4: Web Application
- Build web-based version using Flask/Django
- Add REST API for mobile app integration
- Implement cloud storage and synchronization

---

## Contributors

**Ahmad Salem Khan**  
Registration Number: 25BAI11418  
VIT Bhopal University  
B.Tech Computer Science and Engineering  

**Supervisor:**  
Dr. Preetam Suman  
Professor, Department of Computer Science and Engineering  
VIT Bhopal University

---

## License

This project is created for academic purposes as part of the CSE curriculum at VIT Bhopal University. All rights reserved by the author and the institution.

---

## Acknowledgments

- VIT Bhopal University for providing the opportunity and resources
- Dr. Preetam Suman for guidance and mentorship
- Python Software Foundation for the programming language
- Open-source community for documentation best practices

---

## Contact

For queries, suggestions, or contributions, please contact:

**Ahmad Salem Khan**   
Institution: VIT Bhopal University  
Department: CSE AI ML

---

**Project Submission Date:** 24 November 2025  
**Version:** 1.0  
**Status:** Completed and Submitted
