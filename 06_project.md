# Project 6 (ACASA - OOP)



When the application starts. It will show following menu

~~~
Welcome to Acasa Restaurant
___________________________

1. New Order -> Speisekarte
2. Show all Order from the DB


~~~

## 1. New Order
the application should offer the user the dishes (Menu).
The user chosse his/her wishes and then the user will be asked about first name , last name.
Then the application will enter his data in the DB, if they dont exist.
Then the application will show the receipt to the user and store the order in the DB

## 2. Show all Orders from the DB
The application will get all order from the DB grouped by the users.

~~~
Thomas Meier
------------
1. Order on 22.01.2023
----------------------
1. Pizza Margherita 5€
2. Pizza Thunfisch 5€

2. Order on 23.02.2023
----------------------
1. Pizza Margherita 5€
2. Pizza Thunfisch 5€


Sara Meier
------------
1. Order on 22.01.2023
----------------------
1. Pizza Margherita 5€
2. Pizza Thunfisch 5€

2. Order on 23.02.2023
----------------------
1. Pizza Margherita 5€
2. Pizza Thunfisch 5€


~~~

# DB Design
1. The DB should be as possible optimized
2. The Food Menu is pre-defined. Stored by Hand in the DB.


**Tables**
1. Category
2. Dishes
3. Customers
4. Order Master
5. Order Details

# Delivery
Everyone should deliver the project solution individually.
Deadline: 27.02.2023 Afternoon

1. Recommended SQLite DB
2. If MySQL is used, then please dump the database as well and put it in the delivery zip file

