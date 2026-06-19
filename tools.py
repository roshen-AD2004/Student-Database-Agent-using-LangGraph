from langchain_core.tools import tool
from db import get_connection

@tool
def get_student_info(student_id: int):
    """
    Retrieve student information from the PostgreSQL database.

    Use this tool whenever the user asks about:
    - student details
    - student information
    - student marks
    - student attendance
    - student records

    Args:
        student_id: Integer student identifier.

    Returns:
        Student details including student_id, name, marks, and attendance.
    """

    conn = get_connection()

    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM students
        WHERE student_id = %s
        """,
        (student_id,)
    )

    result = cur.fetchone()

    cur.close()
    conn.close()

    if not result:
        return "Student not found"

    return {
        "student_id": result[0],
        "name": result[1],
        "marks": result[2],
        "attendance": result[3]
    }

@tool
def get_top_student():
    """
    Retrieve the student with the highest marks from the student database.

    Use this tool when the user asks questions such as:
    - Who is the topper?
    - Who scored the highest marks?
    - Show the top-performing student.
    - Which student has the highest score?
    - Who ranks first in the class?

    Returns:
        Details of the student with the highest marks, including:
        - Student ID
        - Student Name
        - Marks
        - Attendance
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM students
        ORDER BY marks DESC
        LIMIT 1
        """
    )

    result = cur.fetchone()

    cur.close()
    conn.close()

    if not result:
        return "No student records found."

    return {
        "student_id": result[0],
        "name": result[1],
        "marks": result[2],
        "attendance": result[3]
    }

@tool
def get_students_above_marks(min_marks: int):
    """
    Retrieve students whose marks are greater than the specified threshold.

    Use this tool when the user asks questions such as:
    - Show students scoring above 80
    - List students with marks greater than 90
    - Who scored more than 85?
    - Students above 70 marks
    - Show high-performing students

    Args:
        min_marks: Minimum marks threshold.

    Returns:
        A list of students whose marks are greater than the specified value,
        including student ID, name, marks, and attendance.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM students
        WHERE marks > %s
        ORDER BY marks DESC
        """,
        (min_marks,)
    )

    results = cur.fetchall()

    cur.close()
    conn.close()

    if not results:
        return f"No students found with marks above {min_marks}."

    return [
        {
            "student_id": row[0],
            "name": row[1],
            "marks": row[2],
            "attendance": row[3]
        }
        for row in results
    ]

@tool
def get_low_attendance_students(max_attendance: int):
    """
    Retrieve students whose attendance is below the specified percentage.

    Use this tool when the user asks questions such as:
    - Show students with attendance below 75%
    - Who has low attendance?
    - List students with poor attendance
    - Students below 80% attendance
    - Show attendance defaulters

    Args:
        max_attendance: Attendance threshold percentage.

    Returns:
        A list of students whose attendance is below the specified value,
        including student ID, name, marks, and attendance.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM students
        WHERE attendance < %s
        ORDER BY attendance ASC
        """,
        (max_attendance,)
    )

    results = cur.fetchall()

    cur.close()
    conn.close()

    if not results:
        return f"No students found with attendance below {max_attendance}%."

    return [
        {
            "student_id": row[0],
            "name": row[1],
            "marks": row[2],
            "attendance": row[3]
        }
        for row in results
    ]

@tool
def get_low_attendance_students(max_attendance: int):
    """
    Retrieve students whose attendance is below a specified percentage.

    Use this tool when the user asks:
    - Show students with attendance below 75%
    - Who has low attendance?
    - List attendance defaulters
    - Students below 80% attendance
    - Show students with poor attendance

    Args:
        max_attendance: Attendance threshold percentage.

    Returns:
        A list of students whose attendance is below the specified value.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM students
        WHERE attendance < %s
        ORDER BY attendance ASC
        """,
        (max_attendance,)
    )

    results = cur.fetchall()

    cur.close()
    conn.close()

    if not results:
        return f"No students found with attendance below {max_attendance}%."

    return [
        {
            "student_id": row[0],
            "name": row[1],
            "marks": row[2],
            "attendance": row[3]
        }
        for row in results
    ]

@tool
def get_student_count():
    """
    Retrieve the total number of students in the database.

    Use this tool when the user asks:
    - How many students are there?
    - Total student count
    - Number of students in the database
    - Count all students

    Returns:
        The total number of student records.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT COUNT(*)
        FROM students
        """
    )

    result = cur.fetchone()

    cur.close()
    conn.close()

    return {
        "total_students": result[0]
    }