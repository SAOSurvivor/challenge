INSERT INTO public.address (street, house_no, city, pin_code, country)
VALUES ('Street', '1', 'Berlin', '10115', 'Germany'),
       ('Street', '10', 'Paris', '75001', 'France'),
       ('Street', '2', 'Hamburg', '20144', 'Germany'),
       ('Street', '20', 'Brussels', '1000', 'Belgium'),
       ('Street', '3', 'Munich', '80331', 'Germany'),
       ('Street', '5', 'Madrid', '28013', 'Spain'),
       ('Street', '4', 'Cologne', '50667', 'Germany'),
       ('Street', '9', 'Amsterdam', '1016', 'Netherlands'),
       ('Street', '5', 'Stuttgart', '70173', 'Germany'),
       ('Street', '15', 'Copenhagen', '1050', 'Denmark');


INSERT INTO public.shipment (tracking_number, carrier, sender_address_id, receiver_address_id, article_name, article_quantity, article_price, sku, status)
VALUES ('TN12345678', 'DHL', 1, 2, 'Laptop', 1, 800, 'LP123', 'in-transit'),
       ('TN12345678', 'DHL', 1, 2, 'Mouse', 1, 25, 'MO456', 'in-transit'),
       ('TN12345679', 'UPS', 3, 4, 'Monitor', 2, 200, 'MT789', 'inbound-scan'),
       ('TN12345680', 'DPD', 5, 6, 'Keyboard', 1, 50, 'KB012', 'delivery'),
       ('TN12345680', 'DPD', 5, 6, 'Mouse', 1, 25, 'MO456', 'parcelshop,delivery'),
       ('TN12345681', 'FedEx', 7, 8, 'Laptop', 1, 900, 'LP345', 'transit'),
       ('TN12345681', 'FedEx', 7, 8, 'Headphones', 1, 100, 'HP678', 'transit'),
       ('TN12345682', 'GLS', 9, 10, 'Smartphone', 1, 500, 'SP901', 'scanned'),
       ('TN12345682', 'GLS', 9, 10, 'Charger', 1, 20, 'CH234', 'scanned');
