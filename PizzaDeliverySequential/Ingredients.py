import random  # importing random function
import time  # importing random function


class Ingredients:
    partial_batch_remaining = {}

    def __init__(self, dough_stock=60, sauce_stock=40, toppings_stock=90):
        self.dough_stock = dough_stock  # initiating quantity of dough
        self.sauce_stock = sauce_stock  # initiating quantity of sauce
        self.toppings_stock = toppings_stock  # initiating quantity of toppings
        self.small_pizza_components = {"doughCom": 1, "sauceCom": 1,
                                       "toppingsCom": 2}  # required ingredients in small pizza
        self.medium_pizza_components = {"doughCom": 2, "sauceCom": 1,
                                        "toppingsCom": 3}  # required ingredients in medium pizza
        self.large_pizza_components = {"doughCom": 3, "sauceCom": 2,
                                       "toppingsCom": 4}  # required ingredients in large pizza

    @staticmethod
    def generate_ids(container):  # getting id from this function
        initials = ""
        if container == "dough_container":
            initials = "DOU"
        elif container == "sauce_container":
            initials = "SAU"
        elif container == "toppings_container":
            initials = "TOP"
        value = f'ING-{initials}-{random.randint(10000, 99999)}'
        return value

    @staticmethod
    def get_quantity(order):  # fetching quantity from this function
        total_quantity = 0
        for _ in order:
            total_quantity = order["Small_Pizza"] + order["Medium_Pizza"] + order["Large_Pizza"]
        return total_quantity

    def get_new_batch(self):  # creating new batch here
        batch = {"dough_container": [], "sauce_container": [], "toppings_container": []}
        for key in batch:
            if key == "dough_container":
                dough_id = Ingredients.generate_ids("dough_container")
                for i in range(self.dough_stock):
                    batch[key].append(dough_id)
            elif key == "sauce_container":
                sauce_id = Ingredients.generate_ids("sauce_container")
                for i in range(self.sauce_stock):
                    batch[key].append(sauce_id)
            elif key == "toppings_container":
                toppings_id = Ingredients.generate_ids("toppings_container")
                for i in range(self.toppings_stock):
                    batch[key].append(toppings_id)
        return batch

    def reload_partially_filled_container(self, partial_batch): #reloading_partially_filled container here
        time.sleep(3)
        for key in partial_batch:
            if key == "dough_container":
                dough_id = Ingredients.generate_ids("dough_container")
                for i in range(self.dough_stock - len(partial_batch[key])):
                    partial_batch[key].append(dough_id)
            elif key == "sauce_container":
                sauce_id = Ingredients.generate_ids("sauce_container")
                for i in range(self.sauce_stock - len(partial_batch[key])):
                    partial_batch[key].append(sauce_id)
            elif key == "toppings_container":
                toppings_id = Ingredients.generate_ids("toppings_container")
                for i in range(self.toppings_stock - len(partial_batch[key])):
                    partial_batch[key].append(toppings_id)
        return partial_batch

    def storage_capacity_remaining(self, order, new_batch):
        """
        type new_batch: dictionary containing list of ingredient ids.
        type order: dictionary containing quantities of pizzas required.
        """
        used_ingredients = {}
        list_for_dough = []
        list_for_sauce = []
        list_for_toppings = []
        if len(new_batch["dough_container"]) >= self.large_pizza_components['doughCom'] and \
                len(new_batch["sauce_container"]) >= self.large_pizza_components[
            'sauceCom'] and len(new_batch["toppings_container"]) >= \
                self.large_pizza_components['toppingsCom']:
            for key in order:
                if key == "Large_Pizza":
                    for i, j in self.large_pizza_components.items():
                        total_quantity = j * order[key]
                        if i == "doughCom" and len(new_batch['dough_container']) >= total_quantity:
                            for k in range(total_quantity):
                                list_for_dough.append(new_batch['dough_container'].pop())
                        elif i == "sauceCom" and len(new_batch['sauce_container']) >= total_quantity:
                            for k in range(total_quantity):
                                list_for_sauce.append(new_batch['sauce_container'].pop())
                        elif i == "toppingsCom" and len(new_batch['toppings_container']) >= total_quantity:
                            for k in range(total_quantity):
                                list_for_toppings.append(new_batch['toppings_container'].pop())

            if len(new_batch["dough_container"]) >= self.medium_pizza_components['doughCom'] and \
                    len(new_batch["sauce_container"]) >= self.medium_pizza_components[
                'sauceCom'] and len(new_batch["toppings_container"]) >= \
                    self.medium_pizza_components['toppingsCom']:
                for key in order:
                    if key == "Medium_Pizza":
                        for i, j in self.medium_pizza_components.items():
                            total_quantity = j * order[key]
                            if i == "doughCom" and len(new_batch['dough_container']) >= total_quantity:
                                for k in range(total_quantity):
                                    list_for_dough.append(new_batch['dough_container'].pop())
                            elif i == "sauceCom" and len(new_batch['sauce_container']) >= total_quantity:
                                for k in range(total_quantity):
                                    list_for_sauce.append(new_batch['sauce_container'].pop())
                            elif i == "toppingsCom" and len(new_batch['toppings_container']) >= total_quantity:
                                for k in range(total_quantity):
                                    list_for_toppings.append(new_batch['toppings_container'].pop())

                if len(new_batch["dough_container"]) >= self.small_pizza_components[
                    'doughCom'] and \
                        len(new_batch["sauce_container"]) >= self.small_pizza_components[
                    'sauceCom'] and len(new_batch["toppings_container"]) >= \
                        self.small_pizza_components['toppingsCom']:
                    for key in order:
                        if key == "Small_Pizza":
                            for i, j in self.small_pizza_components.items():
                                total_quantity = j * order[key]
                                if i == "doughCom" and len(new_batch['dough_container']) >= total_quantity:
                                    for k in range(total_quantity):
                                        list_for_dough.append(new_batch['dough_container'].pop())
                                elif i == "sauceCom" and len(new_batch['sauce_container']) >= total_quantity:
                                    for k in range(total_quantity):
                                        list_for_sauce.append(new_batch['sauce_container'].pop())
                                elif i == "toppingsCom" and len(new_batch['toppings_container']) >= total_quantity:
                                    for k in range(total_quantity):
                                        list_for_toppings.append(new_batch['toppings_container'].pop())
            self.partial_batch_remaining['dough_container'] = new_batch['dough_container']
            self.partial_batch_remaining['sauce_container'] = new_batch['sauce_container']
            self.partial_batch_remaining['toppings_container'] = new_batch['toppings_container']

        used_ingredients['order_id'] = order['Order_ID']
        used_ingredients['small_pizza'] = order['Small_Pizza']
        used_ingredients['medium_pizza'] = order['Medium_Pizza']
        used_ingredients['large_pizza'] = order['Large_Pizza']
        used_ingredients['total_quantity'] = Ingredients.get_quantity(order)
        used_ingredients['dough_container'] = list_for_dough
        used_ingredients['sauce_container'] = list_for_sauce
        used_ingredients['toppings_container'] = list_for_toppings
        return used_ingredients
