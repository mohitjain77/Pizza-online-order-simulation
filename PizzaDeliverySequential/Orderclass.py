import json  # importing json
import csv  # importing csv

file = open('order.json')  # reading json file
loadedData = json.load(file)  # loading data from json file
orderData = sorted(loadedData, key=lambda _: _['Order_ID'])  # sorting order data
deliver_queue = []  # initiating deliver queue


class Order:
    def __init__(self):
        self.header = ['Order Id', 'Time of acceptance', 'Time of collection', 'No. of Small Pizza',
                       'No. of Medium Pizza', 'No. of Large Pizza', 'Ingredients Ids']  # using header from here

    @staticmethod
    def get_order():  # get order on first come first serve basis
        order = orderData.pop(0)
        return order

    @staticmethod
    def sort_queue(queue):  # sorting the queue according to the quantity
        def get_total_quantity(order):
            return order['total_quantity']

        queue.sort(key=get_total_quantity, reverse=True)

    def creating_csv(self, for_delivery):  # creating csv here
        main_dictionary = {}
        for _ in for_delivery:
            main_dictionary['Order Id'] = for_delivery['order_id']
            main_dictionary['Time of acceptance'] = for_delivery['time_of_acceptance']
            main_dictionary['Time of collection'] = for_delivery['time_of_collection']
            main_dictionary['No. of Small Pizza'] = for_delivery['small_pizza']
            main_dictionary['No. of Medium Pizza'] = for_delivery['medium_pizza']
            main_dictionary['No. of Large Pizza'] = for_delivery['large_pizza']
            main_dictionary['Ingredients Ids'] = for_delivery['dough_container'] + for_delivery['sauce_container'] + \
                                                 for_delivery['toppings_container']
        with open('Delivery.csv', 'a+', ) as deliver:
            writer = csv.DictWriter(deliver, fieldnames=self.header)
            writer.writerow(main_dictionary)
