SELECT DISTINCT c.first_name, c.last_name, c.customer_id
FROM customers AS c
JOIN orders as o
on c.customer_id = o.FK_customer_id