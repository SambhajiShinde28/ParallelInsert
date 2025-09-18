# ⚡ Parallel Insert Simulation – Python & SQLite

This project simulates a **distributed system** where different types of data (Users, Orders, Products) are stored in **separate SQLite databases**.  
The system performs **parallel/concurrent insertions** into these databases using **multithreading**, ensuring that multiple records can be inserted simultaneously.

This project was developed as part of a **Python & Django Developer Assignment**.

---

## ✨ Features
- 📂 Three independent SQLite databases:
  - **users.db** → Stores user information (id, name, email).  
  - **products.db** → Stores product details (id, name, price).  
  - **orders.db** → Stores order details (id, user_id, product_id, quantity).  
- ⚡ **Multithreading** → Simulates at least 10 simultaneous insert operations per model.  
- 🛠️ **Application-level validation** → Database-level validation is avoided; handled in Python logic.  
- ✅ Final output displays the **results of all insertions in a single command execution**.  

---

## 🛠️ Tech Stack
- **Python 3.x**  
- **SQLite** (for databases)  
- **Threading** (for parallel insertions)  

---

## 📂 Input Data
The assignment provides sample data for insertion:

### 👤 Users Table
| id | name    | email              |
|----|---------|--------------------|
| 1  | Alice   | alice@example.com  |
| 2  | Bob     | bob@example.com    |
| 3  | Charlie | charlie@example.com|
| ...| ...     | ...                |

### 🛒 Products Table
| id | name         | price  |
|----|--------------|--------|
| 1  | Laptop       | 1000.0 |
| 2  | Smartphone   | 700.0  |
| ...| ...          | ...    |

### 📦 Orders Table
| id | user_id | product_id | quantity |
|----|---------|------------|----------|
| 1  | 1       | 1          | 2        |
| 2  | 2       | 2          | 1        |
| ...| ...     | ...        | ...      |

---

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
     git clone https://github.com/<your-username>/ParallelInsert.git
     cd ParallelInsert
   ```

2. Create a virtual environment:
   ```bash
      python -m venv venv
      source venv/bin/activate   # On Linux/Mac
      venv\Scripts\activate      # On Windows
   ```

3. Install requirements (if any are provided in requirements.txt):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python manage.py runserver
   ```

---

## The program will:

- Create three SQLite databases (users.db, products.db, orders.db).
- Insert 10 records simultaneously into each database using threads.
- Print the results of all insertions in one command output.

💡 Python | Django | Multithreading | Database Management
