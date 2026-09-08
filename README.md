# University Management System

A Python-based University Management System built using **Object-Oriented Programming (OOP)** principles, with **persistent JSON data storage**, bidirectional object relationships, and an interactive command-line interface.

---

## 📌 Overview

The **University Management System** is a command-line application developed in Python to manage core university entities such as **students, teachers, courses, and course enrollments**.

The project was designed to apply Object-Oriented Programming concepts in a practical system rather than using isolated examples. It focuses on class relationships, encapsulation, inheritance, polymorphism, persistent data storage, and maintaining consistency between related objects.

The application also implements a custom data management system that serializes the application's object structure into JSON and reconstructs the required relationships when the program starts again.

---

## ✨ Features

* 👨‍🎓 Student management
* 👨‍🏫 Teacher/faculty management
* 📚 Course management
* 📝 Student course enrollment
* 🔗 Bidirectional relationships between students and courses
* 💾 Persistent JSON-based data storage
* 🔄 Automatic relationship reconstruction when loading saved data
* 🔐 Encapsulation using private attributes and controlled access
* 🧬 Inheritance between related entities
* 🔁 Polymorphic behavior across classes
* 🖥️ Interactive menu-driven Command-Line Interface (CLI)

---

## 🧠 Object-Oriented Programming Concepts

This project was primarily developed to strengthen practical understanding of Object-Oriented Programming in Python.

### 1. Inheritance

A base `Person` class provides common attributes and behavior for people within the university system.

`Student` and `Teacher` inherit from `Person`, allowing common functionality to be reused while each class maintains its own specialized behavior.

```text
Person
├── Student
└── Teacher
```

---

### 2. Encapsulation

Encapsulation is implemented by protecting internal attributes and controlling how they are accessed or modified.

For example, sensitive attributes such as teacher salary are kept private and accessed through custom getters and setters.

This provides controlled access to internal object state.

---

### 3. Polymorphism

Different classes can provide their own implementations of common behavior while maintaining a consistent interface.

This allows the system to work with different university entities without requiring completely separate interfaces for each type.

---

### 4. Abstraction

The system separates the responsibilities of different components and classes.

For example:

* Entity classes represent university objects.
* The data manager handles persistence.
* The CLI handles user interaction.

This separation keeps the system more organized and maintainable.

---

### 5. Object Relationships

Students and courses maintain a relationship with each other.

When a student is enrolled in a course, the relationship is maintained from both sides:

```text
Student
   │
   ├── courses
   │
   ▼
Course
   │
   └── students
```

This prevents the system from having inconsistent relationship states.

---

## 🔄 Bidirectional State Synchronization

One of the key design aspects of this project is maintaining **bidirectional relationships** between objects.

For example, when a student enrolls in a course:

```text
Student.courses
        ↕
Course.students
```

The enrollment operation updates both objects automatically.

Instead of manually modifying both sides of the relationship, the system is designed to keep them synchronized.

This provides a more consistent internal state and demonstrates how relationships between objects can be managed in an OOP-based application.

---

## 💾 Data Persistence

The system uses Python's built-in `json` module to provide persistent storage.

The application converts its object data into JSON-compatible structures before saving it.

Conceptually:

```text
Python Objects
      ↓
Serialization
      ↓
JSON Data
      ↓
Persistent Storage
```

When the application starts again:

```text
JSON Data
      ↓
Deserialization
      ↓
Python Objects
      ↓
Relationship Reconstruction
```

Because JSON cannot directly store Python object references, the system reconstructs the relationships between objects when the data is loaded.

This allows information such as students, courses, teachers, and their relationships to persist across program executions.

---

## 🗂️ Data Management

A dedicated `data_manager` component is responsible for handling the conversion between the application's object-oriented structure and JSON data.

Its responsibilities include:

* Serializing objects into JSON-compatible structures
* Saving application data
* Loading previously stored data
* Reconstructing objects from stored data
* Restoring relationships between related objects

This separates persistence logic from the entity classes and keeps responsibilities organized.

---

## 🖥️ Command-Line Interface

The application provides an interactive, menu-driven CLI through which users can manage the university system.

The interface allows users to perform operations such as:

* Managing students
* Managing teachers
* Managing courses
* Enrolling students
* Viewing records
* Exiting the application

Example:

```text
=================================
   UNIVERSITY MANAGEMENT SYSTEM
=================================

1. Manage Students
2. Manage Teachers
3. Manage Courses
4. Manage Enrollments
5. Display Records
6. Exit

Enter your choice:
```

> The exact menu options depend on the current implementation of the project.

---

## 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming**
* **JSON**
* **File I/O**
* **Command-Line Interface (CLI)**

The project primarily uses Python's standard library and does not rely on external frameworks.

---

## 📁 Project Structure

The project is organized around the responsibilities of its different components.

A typical structure is:

```text
university-management-system/
│
├── main.py
├── data_manager.py
│
├── models/
│   ├── person.py
│   ├── student.py
│   ├── teacher.py
│   └── course.py
│
├── data/
│   └── university_data.json
│
├── README.md
├── .gitignore
└── LICENSE
```

> The structure above represents the logical organization of the project. File and folder names may vary depending on the current implementation.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3** installed on your system.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/anayafrancium-cmyk/university-management-system.git
```

### 2. Navigate to the project directory

```bash
cd university-management-system
```

### 3. Run the application

If the main entry point is `main.py`:

```bash
python main.py
```

On some systems, you may need:

```bash
python3 main.py
```

---

## 📊 Data Storage

Application data is stored in JSON format.

The JSON file allows the system to retain information between different executions of the application.

For example:

```text
Application Run 1
      ↓
Create Student
      ↓
Enroll Student
      ↓
Save Data
      ↓
JSON File

Application Run 2
      ↓
Load JSON
      ↓
Reconstruct Objects
      ↓
Restore Relationships
```

This means the application does not need to start from an empty state every time it is executed.

---

## 🎯 Learning Objectives

This project was developed to gain practical experience with:

* Designing classes and objects
* Applying OOP principles to a real-world scenario
* Understanding inheritance and polymorphism
* Implementing encapsulation
* Managing relationships between objects
* Working with persistent data
* Serializing and deserializing structured data
* Reconstructing object relationships from stored data
* Designing a menu-driven CLI
* Separating responsibilities between different components

---

## 🔮 Future Improvements

Possible improvements for future versions include:

* [ ] Add automated unit tests
* [ ] Improve input validation and error handling
* [ ] Add search and filtering functionality
* [ ] Add authentication and role-based access
* [ ] Introduce a graphical user interface (GUI)
* [ ] Replace JSON storage with a relational database such as PostgreSQL or MySQL
* [ ] Add logging
* [ ] Add automated testing and CI/CD
* [ ] Develop a web-based version using a Python web framework

---

## 📚 Project Context

This project was developed as a practical application of **Object-Oriented Programming in Python**.

Rather than implementing OOP concepts as isolated exercises, the project combines them into a single system where multiple objects interact, maintain relationships, and persist their state.

The project particularly focuses on understanding how object-oriented design can be used to model real-world entities and their relationships.

---

## 👩‍💻 Author

**Anaya**

BS Computer Science Student
Lahore, Pakistan

---
