def print_price(index, order, food_items):
    print(f'{order[index]} - ${food_items[order[index]]}')

def print_order(order, food_items):
    for index in range(len(order)):
        print_price(index, order, food_items)
        
        #...a bunch of code...
	#print_price(0, order, food_items)
	#print_price(1, order, food_items)
	#print_price(2, order, food_items)
	#print_price(3, order, food_items)

food_items = {'burger': 5.99, 'fries': 2.99, 'shake': 4.99, 'salad': 3.99}
order = ['burger', 'fries', 'shake', 'salad']
print_order(order, food_items)