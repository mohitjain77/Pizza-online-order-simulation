import random  # importing random function


class Ingredients:

    def __init__(self, dough_stock=120, sauce_stock=80, toppings_stock=180):
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

    def storage_capacity_remaining(self, order, batch):
        """
        type batch: dictionary containing list of ingredient ids.
        type order: dictionary containing quantities of pizzas required.
        """
        used_ingredients = {}
        list_for_dough = []
        list_for_sauce = []
        list_for_toppings = []
        if len(batch["dough_container"]) >= self.large_pizza_components['doughCom'] and \
                len(batch["sauce_container"]) >= self.large_pizza_components[
            'sauceCom'] and len(batch["toppings_container"]) >= \
                self.large_pizza_components['toppingsCom']:
            for key in order:
                if key == "Large_Pizza":
                    for i, j in self.large_pizza_components.items():
                        total_quantity = j * order[key]
                        if i == "doughCom" and len(batch['dough_container']) >= total_quantity:
                            for k in range(total_quantity):
                                list_for_dough.append(batch['dough_container'].pop())
                        elif i == "sauceCom" and len(batch['sauce_container']) >= total_quantity:
                            for k in range(total_quantity):
                                list_for_sauce.append(batch['sauce_container'].pop())
                        elif i == "toppingsCom" and len(batch['toppings_container']) >= total_quantity:
                            for k in range(total_quantity):
                                list_for_toppings.append(batch['toppings_container'].pop())

            if len(batch["dough_container"]) >= self.medium_pizza_components['doughCom'] and \
                    len(batch["sauce_container"]) >= self.medium_pizza_components[
                'sauceCom'] and len(batch["toppings_container"]) >= \
                    self.medium_pizza_components['toppingsCom']:
                for key in order:
                    if key == "Medium_Pizza":
                        for i, j in self.medium_pizza_components.items():
                            total_quantity = j * order[key]
                            if i == "doughCom" and len(batch['dough_container']) >= total_quantity:
                                for k in range(total_quantity):
                                    list_for_dough.append(batch['dough_container'].pop())
                            elif i == "sauceCom" and len(batch['sauce_container']) >= total_quantity:
                                for k in range(total_quantity):
                                    list_for_sauce.append(batch['sauce_container'].pop())
                            elif i == "toppingsCom" and len(batch['toppings_container']) >= total_quantity:
                                for k in range(total_quantity):
                                    list_for_toppings.append(batch['toppings_container'].pop())

                if len(batch["dough_container"]) >= self.small_pizza_components[
                    'doughCom'] and \
                        len(batch["sauce_container"]) >= self.small_pizza_components[
                    'sauceCom'] and len(batch["toppings_container"]) >= \
                        self.small_pizza_components['toppingsCom']:
                    for key in order:
                        if key == "Small_Pizza":
                            for i, j in self.small_pizza_components.items():
                                total_quantity = j * order[key]
                                if i == "doughCom" and len(batch['dough_container']) >= total_quantity:
                                    for k in range(total_quantity):
                                        list_for_dough.append(batch['dough_container'].pop())
                                elif i == "sauceCom" and len(batch['sauce_container']) >= total_quantity:
                                    for k in range(total_quantity):
                                        list_for_sauce.append(batch['sauce_container'].pop())
                                elif i == "toppingsCom" and len(batch['toppings_container']) >= total_quantity:
                                    for k in range(total_quantity):
                                        list_for_toppings.append(batch['toppings_container'].pop())
                else:
                    return None

        used_ingredients['order_id'] = order['Order_ID']
        used_ingredients['small_pizza'] = order['Small_Pizza']
        used_ingredients['medium_pizza'] = order['Medium_Pizza']
        used_ingredients['large_pizza'] = order['Large_Pizza']
        used_ingredients['total_quantity'] = Ingredients.get_quantity(order)
        used_ingredients['dough_container'] = list_for_dough
        used_ingredients['sauce_container'] = list_for_sauce
        used_ingredients['toppings_container'] = list_for_toppings
        return used_ingredients
