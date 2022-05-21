import time  # importing random function
from Orderclass import *  # importing Order class
from Ingredients import Ingredients  # importing Ingredients class
from time import strftime, gmtime


class Pizza:

    @staticmethod
    def making_of_pizza(batch):  # making pizza here
        order = Order().get_order()
        time_in_sec = time.time()
        time_of_acceptance = strftime("%H:%M:%S", gmtime(time_in_sec))
        making_pizza = Ingredients().storage_capacity_remaining(order, batch)
        making_pizza['time_of_acceptance'] = time_of_acceptance
        time.sleep(0.02)
        return making_pizza

    def cooking_pizza(self, batch):  # cooking pizza here
        cooked_pizza = self.making_of_pizza(batch)
        time.sleep(0.01 * cooked_pizza['total_quantity'])
        deliver_queue.append(cooked_pizza)
        Order.sort_queue(deliver_queue)  # getting list of cooked pizza

    @staticmethod
    def deliver_pizza():  # getting pizza here one-by-one from here according to the quantity
        order_to_deliver = deliver_queue.pop(0)
        time_in_sec = time.time()
        time_of_collection = strftime("%H:%M:%S", gmtime(time_in_sec))
        order_to_deliver["time_of_collection"] = time_of_collection
        Order().creating_csv(order_to_deliver)
