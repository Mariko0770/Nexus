# Nexus
Personal Life Organizer web app – final project
## Project Description
Nexus is a web app I made to help people organize their life in one place.
It combines tasks, projects, events, and important dates so you don’t need multiple apps or notebooks.
You can quickly see what you need to do, what’s coming next, and what you have already planned.

I made this project because staying organized can be hard, and I wanted to make something simple and useful.

---

## Features
- Home page shows everything at once
- Tasks: add, view, delete
- Projects: track your work with start and target dates
- Events: keep track of important dates
- Birthdays: remember friends and family
- Clean, simple interface
- Uses a database to store all information

---

## Technologies Used
- Python (for backend)
- Flask (to handle web pages and forms)
- SQLite (database to save information)
- HTML & CSS (to make the pages look good)
- JavaScript (for navigation and interaction)

---

## How to Run the Project

1. Open the **Nexus folder** in CS50 Codespace or your terminal.
2. Make sure the database exists. If not, create:
```bash
sqlite3 database/nexus.db
.read database/schema.sql
.exit
---

## Known Limitations
- No login system (only one user)
- Data is saved locally, not online
- No notifications or reminders
- Not fully mobile-friendly

---

## Possible Future Improvements
- Add user login so multiple people can use it
- Save data online in the cloud
- Add reminders or notifications
- Improve design for mobile devices
- Add search and filtering options

---

## AI Tools and Help
I used AI tools to get ideas and help with some code problems.
I also talked with my cousin for ideas about features.
Everything else, I coded myself and I understand how it works.
