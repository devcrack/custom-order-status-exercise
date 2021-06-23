# Custom Order Status 

You have a data source containing order-line(each order can have multiple 
order lines based on the number of products ordered under that specific order).
An order line item can be in one of the following three status:
PENDING, SHIPPED, CANCELLED. You want to determine the status of the overall 
order based on the statuses of each individual order line item for that order.
For example, if you have three items in order number 1234, and two of them are
marked "SHIPPED" but one is marked "PENDING" then the overall status is pending.
If all are marked "SHIPPED" then the status is "SHIPPED".


Data sets 
 - [csv file 1](./files/data_orders.csv)
 - [csv file 2](./files/data_orders_2.csv)

Expected result using [csv file 1](./files/data_orders.csv):

| order_number | status    |
|--------------|-----------|
| ORD_1567     | PENDING   |
| ORD_1234     | SHIPPED   |
| ORD_9834     | SHIPPED   |
| ORD_7654     | CANCELLED |


Expected result using [csv file 2](./files/data_orders.csv):

| order_number | status    |
|--------------|-----------|
| ORD_1567     | PENDING   |
| ORD_1234     | PENDING   |
| ORD_9834     | SHIPPED   |
| ORD_7654     | CANCELLED |


### Requirements: 
- python 3 
- [python 3rd-party](./requirements.txt)


## How to use

First cover the requirements. For this
install python3 and then create a virtual environment
and activate it, finally install dependencies 
([python 3rd-party](./requirements.txt))with:
```pip install -r requirements.txt```

To run the application, use the ```flask``` command or ```python -m flask```
OR **```flask run```**

Once you have running the applicattion use this endpoint
for execute the solution of the exercise:

{host}/custom-order-status/

Notes:
If you are running the project locally {host} usally is
http://127.0.0.1:5000 or http://localhost:5000
