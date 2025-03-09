--Проверка количества записей:
SELECT COUNT(*) FROM stg.orders;
SELECT COUNT(*) FROM dw.sales_fact;
--Проверка целостности данных:
SELECT COUNT(*)
FROM dw.sales_fact f
         LEFT JOIN dw.shipping_dim s ON f.ship_id = s.ship_id
WHERE s.ship_id IS NULL;

-- Проверка корректности агрегатов
SELECT
    SUM(sales) as total_sales,
    SUM(profit) as total_profit
FROM stg.orders;
SELECT
    SUM(sales) as total_sales,
    SUM(profit) as total_profit
FROM dw.sales_fact;
