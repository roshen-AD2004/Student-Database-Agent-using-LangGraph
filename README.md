# Student Database Agent

A LangGraph-powered AI Agent that interacts with a PostgreSQL database using tool calling. The agent can retrieve student information, identify top performers, analyze attendance, and answer student-related queries through natural language.

## Features

### Student Information Retrieval

* Get details of a student using Student ID
* View marks and attendance
* Retrieve complete student records

### Academic Analysis

* Find the top-performing student
* List students scoring above a specified mark threshold

### Attendance Analysis

* Identify students with low attendance
* Filter students below a given attendance percentage

### Database Statistics

* Get the total number of students in the database

### AI-Powered Query Understanding

The agent understands natural language and automatically selects the appropriate tool to retrieve information from PostgreSQL.

Examples:

* Show details of student 101
* What are the marks of student 102?
* Who is the topper?
* Show students scoring above 85
* Show students below 75% attendance
* How many students are there?

---

# Tech Stack

* Python 3.10.11
* LangGraph
* LangChain
* Groq API
* PostgreSQL
* Psycopg2
* Gradio
* Python Dotenv

---

# Project Architecture

```text
User
 │
 ▼
Gradio UI
 │
 ▼
LangGraph Agent
 │
 ▼
Tool Selection
 │
 ▼
PostgreSQL Database
 │
 ▼
Tool Response
 │
 ▼
LLM Response Generation
 │
 ▼
User
```

---

# Project Structure

```text
student-database-agent/
│
├── app.py
├── tools.py
├── db.py
├── test_tools.py
├── .env
├── requirements.txt
└── README.md
```

---

# Database Schema

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    marks INT,
    attendance FLOAT
);
```

---

# Implemented Tools

## 1. get_student_info(student_id)

Retrieves information for a specific student.

Example:

```text
Show details of student 101
```

---

## 2. get_top_student()

Returns the student with the highest marks.

Example:

```text
Who is the topper?
```

---

## 3. get_students_above_marks(min_marks)

Returns students scoring above a specified threshold.

Example:

```text
Show students scoring above 80
```

---

## 4. get_low_attendance_students(max_attendance)

Returns students whose attendance is below a specified percentage.

Example:

```text
Show students below 75% attendance
```

---

## 5. get_student_count()

Returns the total number of students.

Example:

```text
How many students are there?
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd student-database-agent
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

DB_NAME=studentdb
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

---

# Run the Application

```bash
python app.py
```

If using Gradio:

```bash
python app.py
```

Open the generated Gradio URL in your browser.

---

# Testing Tools

Run:

```bash
python test_tools.py
```

This validates all database tools independently before testing through LangGraph.

---

# Sample Queries

```text
Show details of student 101

Who is the topper?

Show students scoring above 85

Show students below 75% attendance

How many students are there?

Tell me about student 102
```

---

# Learning Objectives

This project demonstrates:

* LangGraph fundamentals
* Tool calling
* PostgreSQL integration
* Agent workflows
* Natural language query understanding
* Multi-tool orchestration
* Retrieval and response generation

---

# Future Enhancements

* Compare two students
* Average marks calculation
* Average attendance calculation
* Student ranking system
* CRUD operations
* Memory support
* Authentication and role-based access
* Multi-agent architecture

---

# Author

Built as a hands-on project to learn LangGraph, Tool Calling, PostgreSQL Integration, and Agentic AI workflows.
