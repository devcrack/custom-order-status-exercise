# stdlib
import csv

order_sets = set()
hierarchy_status = {
    "PENDING": 100,
    "SHIPPED": 50,
    "CANCELLED": 0
}

def gen_orders_by_order_number(*args):
    [order_sets.add(k['order_number']) for k in args[0]]
    print(order_sets)

    orders = dict.fromkeys(list(order_sets))
    for num_order in order_sets:
        orders[num_order] = {}
        sub_items = []
        key_status = "CANCELLED"
        for row_data in args[0]:

            if row_data['order_number'] == num_order:
                sub_items.append(row_data["item_name"])
                status = row_data["status"]
                if hierarchy_status[status] > hierarchy_status[key_status]:
                    key_status = status
        orders[num_order]["items"] = sub_items
        orders[num_order]["status"] = key_status

    return orders


def get_orders_from_file(**kwargs):
    file = kwargs.get("file", None)
    import os
    print(os.getcwd())
    if not file:
        p = "files/data_orders.csv"
        loaded_data = [k for k in csv.DictReader(open(p))]
        return gen_orders_by_order_number(loaded_data)
