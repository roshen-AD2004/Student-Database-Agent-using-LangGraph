from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools import get_low_attendance_students, get_student_count, get_student_info, get_students_above_marks, get_top_student
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph
from langgraph.prebuilt import tools_condition
import gradio as gr
from langchain_core.messages import SystemMessage
from langgraph.graph.message import add_messages

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

tools = [
    get_student_info,
    get_top_student,
    get_students_above_marks,
    get_low_attendance_students,
    get_student_count
]
llm_with_tools = llm.bind_tools(
    tools
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):

    response = llm_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }

tool_node = ToolNode(tools)
builder = StateGraph(State)
builder.add_node(
    "chatbot",
    chatbot
)

builder.add_node(
    "tools",
    tool_node
)

builder.set_entry_point(
    "chatbot"
)

builder.add_conditional_edges(
    "chatbot",
    tools_condition
)

builder.add_edge(
    "tools",
    "chatbot"
)

graph = builder.compile()

def chat(message, history):

    system_prompt = SystemMessage(
        content="""
You are a Student Database Agent.

You help users retrieve and analyze student information stored in a PostgreSQL database.

Available capabilities:
1. Retrieve information about a specific student using student ID.
2. Find the top-performing student.
3. List students scoring above a specified mark.
4. List students with attendance below a specified threshold.
5. Count the total number of students.

Rules:
- Use tools whenever database information is required.
- Never invent student data.
- If a question can be answered without tools, answer directly.
- If the user asks about your capabilities, explain them.
- If a requested capability is unavailable, politely mention that it is not yet implemented.
"""
    )

    response = llm_with_tools.invoke(
        [system_prompt] + state["messages"]
    )

    return {
        "messages": [response]
    }

demo = gr.ChatInterface(
    fn=chat,
    title="Student Database Agent",
    description="Ask questions about students"
)

demo.launch()