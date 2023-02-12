CREATE TABLE customers(
    customer_id INT NOT NULL,
    customer_name character varying(255) NOT NULL,
    customer_date DATE,
    PRIMARY KEY (customer_id)
);

INSERT INTO customers (customer_id, customer_name, customer_date) VALUES
(1, 'Post Malon', '2023-02-21'),
(2, 'Ricky Jervais', '2023-02-22'),
(3, 'Dacathlon Shop', '2023-02-23'),
(4, 'New WG', '2023-02-24'),
(5, 'Berling Wohnung', '2023-02-25');

