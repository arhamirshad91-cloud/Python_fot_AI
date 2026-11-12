from langchain_core.messages import SystemMessages
from langgraph.graph import START , MessageState , Stategraph
from langchain_openai import ChatOpenAI
from modules.ai_agent.tools import TOOLS
from core.services.llms import LLMs

systemPrompt = """You are the friendly customer support assistant for Xander Restaurant.
Keep replies short. Prices are in Pakistani rupees. Use fetch_menu for menu/prices.
For complaints, collect customer name, phone, complaint and order ID. Validate the
order ID with validate_order_id, then call log_complaint only for a valid order.
Never invent facts. Ask for missing details.
"""

def create_chat_model(llm = "grok"):
    return ChatOpenAI(**LLMS(llm),temperature = 0)

def assistant(state: MessageState,model_with_tools):
    reply = model_with_tools.invoke(
        [SystemMessage(content = SYSTEM_PROMPT ), *state["messages"]])
    return {"messages":[reply]}

def buil_graph():
    tools = TOOLS if tools in None else tools
    model = create_chat_model()

    model_with_tools = model.blind_tools(tools)
    builder = StateGraph(MessageState)