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

TOOLS = [
    fetch_menu,
    validate_order_id,
    log_complain
]