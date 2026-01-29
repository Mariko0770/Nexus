# Nexus – Personal Life Organizer

## Project Description
Nexus is a web app I made to help people organize their life in one place.  
It combines tasks, projects, events and important dates so you don’t need multiple apps or notebooks.  
You can quickly see what you need to do, what’s coming next, and what you have already planned.

I made this project because staying organized can be hard and I wanted to make something simple and useful.

---

## Features
- Home page shows everything at once
- Tasks: add, view, delete
- Projects: track your work with start and target dates
- Events: keep track of important dates
- Birthdays: remember friends and family
- Search bar to quickly find tasks, events, notes, birthdays, projects
- Clean, professional interface (black & neon pink)
- Uses a database to store all information

---

## Technologies Used
- Python (for backend)
- Flask (to handle web pages and forms)
- SQLite (database to save information)
- HTML & CSS (to make the pages look good)
- JavaScript (for interactions and search)

---

## How to Run the Project

1. Open the **Nexus folder** in your terminal or IDE.
2. Make sure the database exists. If not, create it:

```bash
sqlite3 database/nexus.db
.read database/schema.sql
.exit
