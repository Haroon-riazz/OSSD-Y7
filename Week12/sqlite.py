import sqlite3

# Step 1: Connect to (or create) the database
con = sqlite3.connect("project.db")
cursor = con.cursor()

# Step 2: Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        grade TEXT NOT NULL
    )
""")

# Step 3: Insert data
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Ali", "A"))
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Sara", "B"))
con.commit()

# Step 4: Read/select data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("Current students:")
for row in rows:
    print(row)

# Step 5: Update data
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("A+", "Sara"))
con.commit()

# Step 6: Delete data
cursor.execute("DELETE FROM students WHERE name = ?", ("Ali",))
con.commit()

# Final check
cursor.execute("SELECT * FROM students")
print("\nStudents after update/delete:")
for row in cursor.fetchall():
    print(row)

con.close()


