
import os
from google import genai
from google.genai import types
import json


api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# Load model configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(BASE_DIR, "model config.json")

#reads configurement file
with open(config_path, 'r') as f:
    config = json.load(f)

# Function to generate a reply from Gemini
def generate_gemini_reply(user_message: str) -> str:
    chat = client.chats.create(model = "gemini-2.5-flash", config= types.GenerateContentConfig(
    system_instruction = config.get("system_instruction"),
    temperature = config.get("temperature"),
    max_output_tokens = config.get("maxOutputTokens"))
    )
    response = chat.send_message(user_message)
    print("Raw Gemini response:", response)
    return response.text


#################

# # load data
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# data1_path = os.path.join(BASE_DIR, "week1.json")

# with open(data1_path) as f:
#     business_data = json.load(f)


# # dynamic pricing function
# def dynamic_pricing(sales, inventory):
   
#    adjustments = []
#    for sale in sales:
#        item_name = sale.get("item_name")
#        current_price = sale.get("current_price",0)
#        units_sold = sale.get("units_sold",0)
#        inv_count = next((i["count"] for i in inventory if i["item_name"] == item_name),0)
      
#        if inv_count == 0:
#            demand_ratio = 1.0
#        else:
#            demand_ratio = units_sold / inv_count
      
#        # Adjust price proportionally to demand deviation
#        proposed_price = current_price * (1 + 0.1 * (demand_ratio))  # 10% max swing
      
#        # Ensure legislation compliance
#        max_increase = current_price * 0.15
#        min_price = current_price * 0.5
#        proposed_price = min(current_price + max_increase, max(min_price, proposed_price))
      
#        adjustments.append({
#            "item": item_name,
#            "current_price": current_price,
#            "proposed_price": round(proposed_price,2),
#            "reasoning": f"Units sold: {units_sold}, Available Inventory: {inv_count - units_sold}, adjusted within legal limits."
#        })
#    return adjustments

# # Stock suggestions
# def wholesale_suggestion(sales, inventory):
#    suggestions = []
#    for item in inventory:
#        sold = next((s.get("units_sold",0) for s in sales if s.get("item_name") == item["item_name"]),0)
#        projected_needed = int(sold * 1.2)
#        if projected_needed > item["count"] - sold:
#            suggestions.append({
#                "item": item["item_name"],
#                "order_qty": projected_needed - (item["count"] - sold),
#                "reasoning": f"Sold {sold}, stock {item['count'] - sold}, recommended order to cover next week."
#            })
#    return suggestions

# # Seasonal item suggestions
# def seasonal_suggestions(sales, product_info):
#    suggestions = []
#    for s in sales:
#        item_name = s.get("item_name") or s.get("iten_name")
#        units = s["units_sold"]
#        if units > 150:  # threshold
#            response = chat.send_message(f"Suggest a seasonal variant of '{item_name}' that I can sell for my business. Keep your answer to one or two sentences only.")
#            suggestions.append({
#                "item": item_name,
#                "reasoning": response.text
#            })
#    return suggestions

# # Calculates revenue
# def calculate_revenue(sales, budget):
#    total_sales = sum(s.get("current_price",0) * s.get("units_sold",0) for s in sales)
#    total_expenses = budget["total_weekly_budget"]
#    current_profit = total_sales - total_expenses
  
#    # weight growth by relative sales
#    avg_units_sold = sum(s.get("units_sold",0) for s in sales)/len(sales)
#    projected_sales = 0
#    for s in sales:
#        units_sold = s.get("units_sold",0)
#        growth_factor = (units_sold/avg_units_sold - 1) * 0.1  # 10% weight
#        projected_units = units_sold * (1 + growth_factor)
#        projected_sales += projected_units * s.get("current_price",0)
#    projected_profit = projected_sales - total_expenses
  
#    # breakdown per item
#    breakdown = []
#    for s in sales:
#        revenue = s.get("current_price",0) * s.get("units_sold",0)
#        breakdown.append(f"- {s.get('item_name') or s.get('iten_name')}: {s.get('units_sold',0)} units * ${s.get('current_price',0):.2f} = ${revenue:.2f}")
  
#    reasoning = "\n".join(breakdown)
#    reasoning += f"\nTotal Revenue = ${total_sales:.2f}\nCosts = ${total_expenses:.2f}\nCurrent Profit = ${current_profit:.2f}\nProjected Profit = ${projected_profit:.2f}"
  
#    return current_profit, projected_profit, reasoning



# dynamic_prices = dynamic_pricing(business_data["sales"], business_data["inventory"])
# wholesale_orders = wholesale_suggestion(business_data["sales"], business_data["inventory"])
# seasonal_items = seasonal_suggestions(business_data["sales"], business_data["product_information"])


# # calc revenue
# current_profit, projected_profit, revenue_reasoning = calculate_revenue(business_data["sales"], business_data["budget"])







####################




# # EVERYTHING BELOW IS USED SOLELY FOR PRINTING IN TERMINAL!!! when you put it on the app ignore this section but take inspo for potential formatting. idk.
# # report
# print("\n--- RECOMMENDATIONS ---\n")


# print("\nDynamic Pricing:")
# for d in dynamic_prices:
#    print(f"- {d['item']}: ${d['current_price']:.2f} -> ${d['proposed_price']:.2f}")
#    print(f"  Reasoning: {d['reasoning']}")


# print("\nPrice Restriction Guarantee:")
# print("- All proposed price changes respect current legislation.")


# print("\nWholesale Purchase Suggestions:")
# if not wholesale_orders:
#    print("- No wholesale orders needed this week.")
# else:
#    for w in wholesale_orders:
#        print(f"- {w['item']}: order {w['order_qty']} units")
#        print(f"  Reasoning: {w['reasoning']}")


# print("\nSeasonal Items Suggestions:")
# for s in seasonal_items:
#    print(f"- {s['item']}")
#    print(f"  Reasoning: {s['reasoning']}")


# print("\n--- REVENUE ---\n")
# print(f"Current Profit: ${current_profit:.2f}")
# print(f"Projected Profit: ${projected_profit:.2f}")

# print("\nReasoning / Calculation:")
# print(revenue_reasoning)


# # questions bot
# print("\n--- Interactive Chat: Type 'quit' to exit ---\n")
# while True:
#    user_input = input("Enter: ")
#    if user_input.lower() == "quit":
#        break
#    response = chat.send_message(user_input)
#    print(f"Guy: {response.text}")
