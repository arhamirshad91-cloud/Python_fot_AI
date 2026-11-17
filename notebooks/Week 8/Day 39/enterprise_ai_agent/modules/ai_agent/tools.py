from langchain_core import tool

@tool 
def fetch_menu() -> list[dict]:
    return{
        {"name":"Zinger Burger" , "price":850 },
        {"name":"Chicken Biryani" , "price":450 },
        {"name":"Club Sandwitch" , "price":700 },
    }

@tool
def validate_order_id(order_id : str) -> bool :
    if order_id in order_list:
        return True
    return False

@tool

def log_complain(customer_name: str, order_id:str , phone :str , complain: str) -> dict:
    temp_dict = {
            "customer_name": customer_name,
            "order_id": order_id,
            "phone": phone,
            "complaint": complaint,
            "status": "Pending"
        }
    complain_list.append(temp_dict)
    return {
        "message" : f"saved! Total complains : {len(complain_list)}"
    }

@tool
def get_discounts() -> dict:
    """this tool tell about today's discount"""
    return {
        "message": "*** Today's Discount *** -- Buy 2 Zinger Burgers get 1 Club Sandwich"
    }

TOOLS = [
    fetch_menu,
    validate_order_id,
    log_complaint,
    get_discounts
]



















# VALID_ORDER_IDS = {"OR-1045", "OR-1046", "OR-1047"}


# @tool
# def fetch_menu() -> list[dict]:
#     """Get the demo restaurant's standard menu and current demo prices in PKR."""
#     return [
#         {"name": "Zinger Burger", "price": 850},
#         {"name": "Chicken Biryani", "price": 450},
#         {"name": "Club Sandwich", "price": 700},
#     ]

# @tool
# def validate_order_id(order_id: str) -> bool:
#     """Check whether an order ID exists before logging a complaint."""
#     return order_id in VALID_ORDER_IDS


# @tool
# def log_complaint(customer_name: str, order_id: str, phone: str, complaint: str) -> dict:
#     """Save a complaint after collecting the customer's name, valid order ID, phone and complaint."""
#     # Enforce the rule in Python even if the model skips the validation tool.
#     if order_id not in VALID_ORDER_IDS:
#         return {"error": "Invalid order ID. Ask for OR-1045, OR-1046 or OR-1047 for this demo."}
#     if not all(value.strip() for value in [customer_name, phone, complaint]):
#         return {"error": "Collect the customer name, phone and complaint before saving."}
#     return save_complaint(customer_name, order_id, phone, complaint)


# @tool
# def retrieve_restaurant_info(query: str) -> str:
#     """Search restaurant documents for branch locations, hours, history, exclusive dishes and policies."""
#     return search_knowledge(query)


# TOOLS = [fetch_menu, validate_order_id, log_complaint, retrieve_restaurant_info]
