import time  # importing time package
from time import strftime, gmtime   # importing time package
from Orderclass import *  # importing Order class
from Ingredients import Ingredients  # importing Ingredients class
from operator import itemgetter  # importing itemgetter from operation package


class Pizza:

    @staticmethod
    def making_of_pizza(all_ingredients, order):  # making pizza here
        time_in_sec = time.time()
        time_of_acceptance = strftime("%H:%M:%S", gmtime(time_in_sec))
        making_pizza = Ingredients().storage_capacity_remaining(order, all_ingredients)
        making_pizza['time_of_acceptance'] = time_of_acceptance
        time.sleep(0.02)
        return making_pizza

    def cooking_pizza(self, all_ingredients, delivery_queue, order):  # cooking pizza here
        cooked_pizza = self.making_of_pizza(all_ingredients, order)
        if cooked_pizza is not None:
            time.sleep(0.01 * cooked_pizza['total_quantity'])
            delivery_queue.append(cooked_pizza)
            delivery_queue.sort(key=itemgetter('total_quantity'), reverse=True)
            return True
        else:
            return None

    @staticmethod
    def deliver_pizza(delivery_queue):  # getting pizza here one-by-one from here according to the quantity
        order_to_deliver = delivery_queue.pop(0)
        time_in_sec = time.time()
        time_of_collection = strftime("%H:%M:%S", gmtime(time_in_sec))
        order_to_deliver["time_of_collection"] = time_of_collection
        Order().creating_csv(order_to_deliver)
