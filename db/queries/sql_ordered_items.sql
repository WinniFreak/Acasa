SELECT i.name, oi.quantity, i.current_price
FROM items AS i 
JOIN order_item AS oi
ON i.item_id = oi.FK_item_id
WHERE oi.FK_order_id = 1
