from Pizza import Pizza  # importing Pizza class
import time  # importing time package
from Ingredients import Ingredients  # importing Ingredients class
from multiprocessing import Process, Manager  # importing multiprocessing package functions
import json  # importing json
import random  # importing random

"""
    Potential issue that I have noticed here is that chef needs to wait until storage is being filled and 
    he needs to wait for oven to get free for cooking.

    He needs to wait until the required ingredients are not available in the storage, he needs to hold on to
    that particular order and cannot send out this order for delivery.This causes deadlock in the system.

    Delivery person needs to wait for the orders that has been put on hold because of deadlock I have just mentioned.
    
    Cooking and delivering is a cyclical process in which the chef and delivery driver must do it until the storage 
    is empty or there are no orders to cook or deliver.
    
    Ingredients used in an order, order picked by a chef and order delivery given to a driver are locked/reserved for 
    using common resources wisely. If used otherwise will cause live locking.

    Process are getting paused if some ingredients are insufficient. This handles concurrent access.

    Multiprocessing is used to handle concurrent use of Pizza Oven by locking the critical part of code 
    to avoid live locking.
    
    By limiting the number of iterations the starvation with in this system was avoided.

"""


# cooking pizza order-wise
def order_wise_cook(locking, all_ingredients, all_orders, delivery_queue):
    try:
        while True:
            if len(all_orders) > 0:
                try:
                    locking.acquire()
                    order = all_orders.pop(0)
                    pizza_cooked = Pizza().cooking_pizza(all_ingredients, delivery_queue, order)
                    if pizza_cooked is True:
                        continue
                    if pizza_cooked is None:
                        break
                finally:
                    locking.release()
            else:
                break
    except IndexError:
        print("All orders has been delivered!!!")


# delivering pizza order-wise
def order_wise_deliver(locking, delivery_queue, all_orders):
    total_order = len(all_orders)
    limit = random.randint(100, 999)  # to limit the count for time been
    while total_order != 0:
        try:
            locking.acquire()
            if len(delivery_queue) > 0:
                Pizza().deliver_pizza(delivery_queue)
                time.sleep(0.05)
                total_order -= 1
            if True:
                if limit == 0:
                    break
                else:
                    limit -= 1
        finally:
            locking.release()


if __name__ == "__main__":
    manager = Manager()
    lock = Manager().Lock()

    # create an empty batch dictionary
    batch = manager.dict()
    ing_containers = ["dough_container", "sauce_container", "toppings_container"]
    # create empty list in shared batch dictionary
    for i in ing_containers:
        batch[i] = manager.list()

    # filling ingredients in empty batch
    for key in batch:
        if key == "dough_container":
            dough_id = Ingredients.generate_ids("dough_container")
            for i in range(Ingredients().dough_stock):
                batch[key].append(dough_id)
        elif key == "sauce_container":
            sauce_id = Ingredients.generate_ids("sauce_container")
            for i in range(Ingredients().sauce_stock):
                batch[key].append(sauce_id)
        elif key == "toppings_container":
            toppings_id = Ingredients.generate_ids("toppings_container")
            for i in range(Ingredients().toppings_stock):
                batch[key].append(toppings_id)

    # Queue which has all the processed orders initially empty
    deliver_queue = manager.list()
    # reading orders from json
    file = open('order.json')  # reading json file
    loadedData = json.load(file)  # loading data from json file
    orderData = sorted(loadedData, key=lambda _: _['Order_ID'])  # sorting order data

    shared_resource_orders = manager.list(orderData)

    hired_chef = int(input("Provide number of hired chefs:- "))
    hired_drivers = int(input("Provide number of hired drivers:- "))

    processes = []
    # applying multiprocessing for multiple chef
    for _ in range(hired_chef):
        process = Process(target=order_wise_cook, args=(lock, batch, shared_resource_orders, deliver_queue,))
        processes.append(process)
    # applying multiprocessing for multiple delivers
    for _ in range(hired_drivers):
        process = Process(target=order_wise_deliver, args=(lock, deliver_queue, shared_resource_orders,))
        processes.append(process)

    for _ in processes:
        _.start()
    for _ in processes:
        _.join()
