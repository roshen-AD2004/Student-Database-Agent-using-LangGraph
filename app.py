from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools import get_low_attendance_students, get_student_count, get_student_info, get_students_above_marks, get_top_student
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph
from langgraph.prebuilt import tools_condition
import gradio as gr
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

    result = graph.invoke(
        {
            "messages": [
                ("user", message)
            ]
        }
    )

    return result["messages"][-1].content

demo = gr.ChatInterface(
    fn=chat,
    title="Student Database Agent",
    description="Ask questions about students"
)

demo.launch()