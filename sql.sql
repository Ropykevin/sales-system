SELECT DATE(created_at) AS date,
SUM((selling_price - buying_price) * sales.quantity) AS profit
FROM sales
JOIN products ON products.product_id = sales.product_id
GROUP BY
    date
ORDER BY
    date;
