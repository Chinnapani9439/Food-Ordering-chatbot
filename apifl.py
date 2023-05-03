from flask import Flask, request, make_response, jsonify
from difflib import SequenceMatcher
import numpy as np
import random
import google.cloud.bigquery as bq
client = bq.Client.from_service_account_json("./your.json")



prices = [2*i+0.75*i for i in range(1,29)]
random.shuffle(prices) 
prices = [str(i) for i in prices]
cart = []

def export_items_to_bigquery(name, email, phone, cart):
    # Instantiates a client
    #bigquery_client = bigquery.Client()

    # Prepares a reference to the dataset
    dataset_ref = client.dataset('wendy_bot')

    table_ref = dataset_ref.table('user_info')
    table = client.get_table(table_ref)  

    rows_to_insert = [
        (name, email, phone, " , ".join(cart)),
    ]
    errors = client.insert_rows(table, rows_to_insert) 
    assert errors == []
    
app = Flask(__name__)

items = ["Pineapple Mango Lemonade", "Tropical Berry Lemonade", "Strawberry Lemonade",  "Iced Tea", "Fresh Brewed Coffee", "Vanilla Frosty", "Chocolate Frosty", "Maple Bacon Chicken Croissant", "Sausage, Egg & Swiss Croissant", "Bacon, Egg & Swiss Croissant", "French Fries", "Pub Fries", "Baconator Fries", "Chili Cheese Fries", "Bourbon Bacon Cheeseburger", 	"Pretzel Bacon Pub Cheeseburger", "Bconator Cheeseburger", "Big Bacon Classic", "Bacon Double Stack", "Jr. Bacon CheeseBurger", "Jr. Cheeseburger", "Double Stack", "Spicy Jalpeno Popper Sandwich", "Classic Jalpeno Popper Sandwich", "Spicy Chicken Sandwich", "Classic Chicken Sandwich", "Grilled Chicken Sandwich", "Crispy Chicken Sandwich"]
itemprice = {"Pineapple Mango Lemonade":random.sample(prices, 1)[0], "Tropical Berry Lemonade":random.sample(prices, 1)[0], "Strawberry Lemonade":random.sample(prices, 1)[0],  "Iced Tea":random.sample(prices, 1)[0], "Fresh Brewed Coffee":random.sample(prices, 1)[0], "Vanilla Frosty":random.sample(prices, 1)[0], "Chocolate Frosty":random.sample(prices, 1)[0], "Maple Bacon Chicken Croissant":random.sample(prices, 1)[0], "Sausage, Egg & Swiss Croissant":random.sample(prices, 1)[0], "Bacon, Egg & Swiss Croissant":random.sample(prices, 1)[0], "French Fries":random.sample(prices, 1)[0], "Pub Fries":random.sample(prices, 1)[0], "Baconator Fries":random.sample(prices, 1)[0], "Chili Cheese Fries":random.sample(prices, 1)[0], "Bourbon Bacon Cheeseburger":random.sample(prices, 1)[0], 	"Pretzel Bacon Pub Cheeseburger":random.sample(prices, 1)[0], "Bconator Cheeseburger":random.sample(prices, 1)[0], "Big Bacon Classic":random.sample(prices, 1)[0], "Bacon Double Stack":random.sample(prices, 1)[0], "Jr. Bacon CheeseBurger":random.sample(prices, 1)[0], "Jr. Cheeseburger":random.sample(prices, 1)[0], "Double Stack":random.sample(prices, 1)[0], "Spicy Jalpeno Popper Sandwich":random.sample(prices, 1)[0], "Classic Jalpeno Popper Sandwich":random.sample(prices, 1)[0], "Spicy Chicken Sandwich":random.sample(prices, 1)[0], "Classic Chicken Sandwich":random.sample(prices, 1)[0], "Grilled Chicken Sandwich":random.sample(prices, 1)[0], "Crispy Chicken Sandwich":random.sample(prices, 1)[0]}

def cart_view():
	sum=0
	res2 = {"fulfillmentMessages": [ ]}
	if len(cart)==0:
		res2["fulfillmentMessages"].append({"text": {"text": ["Your Cart is Empty"]}})
	for i in cart:
		#i+=str( random.sample(prices, 1)[0])
		res2["fulfillmentMessages"].append({"text": {"text": [i+" @ "+itemprice[i]+"$"]}})
		sum+=float(itemprice[i])
	res2["fulfillmentMessages"].append({"text": {"text": ["Total Price of Items in Cart"]}})
	res2["fulfillmentMessages"].append({"text": {"text": [str(sum)+" $"]}})
	return res2

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
	request_data = request.get_json()
	if (request_data['queryResult']['intent']['displayName'])=="view.cart":
		return make_response(jsonify(cart_view()))
	elif (request_data['queryResult']['intent']['displayName'])=="menu.remove":
		anchor = request_data['queryResult']['queryText']
		item = ""
		score = 0
		for it in items:
			z = SequenceMatcher(None, str(anchor), str(it)).ratio()
			if z>score:
				score=z
				item=it
		if score>0.3:		
			cart.remove(item)
			
			return make_response(jsonify({"fulfillmentText": [ {"text": {"text": [f'Oaky I have removed {item} from your Cart']}}
]}))
		else:
			return make_response(jsonify({"fulfillmentMessages": [ {"text": {"text": [f'Sorry your Cart does not contain {item}']}}]}))
	elif (request_data['queryResult']['intent']['displayName'])=="redirect_decision_no - yes":
		#print(request_data)
		print(request_data['queryResult']['outputContexts'][0]['parameters']['name']['name'])
		print(request_data['queryResult']['outputContexts'][0]['parameters']['email'])
		print(request_data['queryResult']['outputContexts'][0]['parameters']['phone-number'])
		name = request_data['queryResult']['outputContexts'][0]['parameters']['name']['name']
		email = request_data['queryResult']['outputContexts'][0]['parameters']['email']
		phone = request_data['queryResult']['outputContexts'][0]['parameters']['phone-number']
		export_items_to_bigquery(name, email, int(phone), cart)
		cart.clear()
		return make_response(jsonify({"fulfillmentMessages": [ {"text": {"text": [f'Your Order has been placed']}}, {"text": {"text": [f"We can't wait to have you again !"]}}, {"text": {"text": [f'Have a great day !']}}]}))
				
	else:
		anchor = request_data['queryResult']['queryText']
		item = ""
		score = 0
		for it in items:
			z = SequenceMatcher(None, str(anchor), str(it)).ratio()
			if z>score:
				score=z
				item=it
		if score>0.5:		
			cart.append(item)
			return make_response(jsonify({"fulfillmentText": [ {"text": {"text": [f'Very Well I have added {item} to your Cart']}}]}))
		else:
			return make_response(jsonify({"fulfillmentMessages": [ {"text": {"text": [f'Sorry Please Specify you choice correctly']}}]}))
			
if __name__ == '__main__':
	app.run(port=8000,debug=True)

