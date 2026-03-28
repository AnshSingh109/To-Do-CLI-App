# 📝 To-Do CLI App (Python)

## 📌 Project Overview

This is a simple **Command Line To-Do List Application** built using Python. It allows users to manage their daily tasks directly from the terminal.

The app supports adding, viewing, marking tasks as completed, and deleting tasks, with data stored persistently using a JSON file.

---

## 🚀 Features

* ➕ Add new tasks
* 📋 View all tasks
* ✅ Mark tasks as completed
* 🗑️ Delete tasks
* 💾 Persistent storage using `tasks.json`

---

## 🛠️ Technologies Used

* Python 🐍
* JSON (for data storage)
* OS module (file handling)

---

## 📂 Project Structure

```
todo.py        # Main application file
tasks.json     # Stores tasks (auto-created)
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/AnshSingh109/todo-cli-app.git
```

2. Navigate to the folder:

```bash
cd todo-cli-app
```

3. Run the program:

```bash
python todo.py
```

---

## 💡 How It Works

* Tasks are stored as a list of dictionaries:

```python
{"task": "Learn Python", "done": False}
```

* Data is saved in `tasks.json` for persistence

---

## 📸 Sample Output

```
##----TO-DO App------
1. Add Task
2. View Task
3. Mark Done Task
4. Delete Task
5. Exit
```

---

## 🔮 Future Improvements

* Add due dates and priorities
* Add search/filter feature
* Convert to GUI (Tkinter / PyQt)
* Build a web version using Flask or Django

---

## 🤝 Contributing

Feel free to fork and improve this project!

---

## 📜 License

This project is open-source and available under the MIT License.
