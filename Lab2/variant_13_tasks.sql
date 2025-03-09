--Вариант 13
--Задание 1: Создать представление по клиентам

CREATE VIEW dw.customer_view AS --представление
SELECT DISTINCT --устранение дубликатов, так как может быть множество заказов у одного клиента
    --выбираем идентификатор, имя, сегмент, географические данные клиента
    Customer_ID,
    Customer_Name,
    Segment,
    Country,
    City,
    State,
    Postal_Code,
    Region
FROM stg.orders;

SELECT * FROM dw.customer_view;

--Задание 2: Определить продажи по способам доставки
CREATE VIEW dw.sales_by_delivery_method AS
SELECT
    ship_mode,
    SUM(sales) AS total_sales --общая выручка для каждого способа доставки
FROM
    stg.orders
GROUP BY
    orders.ship_mode;

SELECT * FROM dw.sales_by_delivery_method;

--Задание 3: Рассчитать среднюю прибыль по городам
CREATE VIEW dw.avg_profit_by_city AS
SELECT
    city,
    AVG(profit) AS average_profit --среднее по всем заказам в городе
FROM
    stg.orders
GROUP BY
    city;
SELECT * FROM dw.avg_profit_by_city