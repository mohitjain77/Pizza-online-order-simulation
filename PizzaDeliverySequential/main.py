import Orderclass  # importing order class
from Pizza import Pizza  # importing Pizza class
import time  # importing time package
from threading import *  # importing threading package
from Ingredients import Ingredients  # importing Ingredients class


# cooking pizza order-wise
def order_wise_cook(batch):
    for _ in range(len(Orderclass.orderData)):
        Pizza().cooking_pizza(batch)


# delivering pizza order-wise
def order_wise_deliver():
    total_order = len(Orderclass.loadedData)
    while total_order != 0:
        if len(Orderclass.deliver_queue) > 0:
            Pizza().deliver_pizza()
            time.sleep(0.05)
            total_order -= 1
        if len(Orderclass.deliver_queue) > 0 and not threads[0].is_alive():
            break


if __name__ == "__main__":
    # fetching new batch of ingredients here
    new_batch = Ingredients().get_new_batch()

    # implementing thread function
    threads = [Thread(target=order_wise_cook, args=(new_batch,)), Thread(target=order_wise_deliver),
               Thread(
                   target=Ingredients().reload_partially_filled_container, args=(Ingredients.partial_batch_remaining,)
               )]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
