SELECT c.first_name, c.last_name, o.date, o.order_id, i.item_id, i.name, oi.quantitiy, i.current_price
FROM customers AS c
JOIN orders AS o
ON c.customer_id = o.FK_customer_id
JOIN order_item as oi
on o.order_id = oi.FK_order_id
JOIN items AS i
on oi.FK_item_id = i.item_id
ORDER BY c.customer_id
