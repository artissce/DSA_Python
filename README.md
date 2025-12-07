# 🧠 DSA Visualizer

**DSA Visualizer** is an interactive educational tool designed to bring Data Structures and Algorithms to life. Built with **Python** and **Streamlit**, this application renders dynamic diagrams of data structures (starting with Linked Lists) to help visualize pointer manipulation, logic flow, and edge cases in real-time.

🔗 **Live Demo:** [CLICK HERE TO VIEW THE APP](https://dsapython-artissce.streamlit.app/)

---

## ✨ Key Features

### 🔗 Singly Linked List
* **Dynamic Operations:** Add (Append) and Delete nodes interactively.
* **Visual Feedback:** Real-time rendering of nodes and pointers using **Graphviz**.
* **Code Inspection:** Displays the actual **Python code** executed for each operation (Append, Delete, Search, Reverse) directly below the visualization.
* **Algorithmic Logic:**
    * **Reverse List:** In-place reversal visualization.
    * **Duplicate Removal:** Implementation using Hash Sets for O(n) efficiency.
    * **Cycle Detection:** Visual simulation of **Floyd’s Tortoise and Hare** algorithm.

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Frontend framework:** Streamlit
* **Visualization Engine:** Graphviz
* **Architecture:** Modular design (MVC-like pattern) separating logic (`data_structures`) from presentation (`views`).

## 📂 Project Structure

This project follows a modular architecture to allow easy scalability for future structures (Stacks, Trees, Graphs):

```text
DSA_Python/
├── app.py                   # Main entry point and Router
├── data_structures/         # Pure algorithmic logic
│   └── linkedListSingly.py
├── views/                   # Streamlit UI components
│   └── linkedListSingly_view.py
├── packages.txt             # System-level dependencies (Graphviz)
└── requirements.txt         # Python dependencies
