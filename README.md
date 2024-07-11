Ребята, привет!
Я очень рад, что мои руки дошли до вас (именно в тот момент как вы дропнули вакансию, у меня магическим образом пропало свободное время)
Запуск скрипта через main.py

Ответы на второе тестовое
1)
SELECT ticket_client
FROM tickets
WHERE csat < 3;

2)
SELECT ticket_id
FROM tickets
WHERE text LIKE '%отлично%'
ORDER BY csat DESC;

3)
SELECT 
    o.order_client_id AS frequent_customer, 
    MAX(o.price) AS max_sum
FROM 
    orders o
JOIN 
    clients c ON o.order_client_id = c.client_id
WHERE 
    o.place IN ('Теремок', 'Вкусно и точка') 
    AND o.price BETWEEN 2000 AND 10000
GROUP BY 
    o.order_client_id
HAVING 
    COUNT(o.order_id) > 5;

4)
SELECT 
    o.*, 
    c.name, 
    c.age, 
    c.city, 
    t.csat, 
    t.text, 
    t.date
FROM 
    orders o
JOIN 
    clients c ON o.order_client_id = c.client_id
JOIN 
    tickets t ON t.ticket_order_id = o.order_id
LIMIT 1000;
