--SHOW DATABASES;
--CREATE DATABASE edward_hostels;
USE edward_hostels;
/*CREATE TABLE residents(
id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
other_names VARCHAR(50) NOT NULL,
phone_number INT(11),
email VARCHAR(50) NOT NULL
);
*/
ALTER TABLE residents ADD age INT(2) NOT NULL;
INSERT INTO residents (first_name, other_names, phone_number, email, age)
VALUES 
('Ray', 'Man', 0243142162, 'ray@mail.com', 26),
('Simpsom', 'Kwame', 0266152624, 'kwame@mail.com', 32),
('Robin', "Rudd", 0547112413, 'rob_rudd@mail.com', 28),
('Afia', 'Ba Boni', 0836212111, 'afiababoni@mail.com', 31);

UPDATE edward_hostels.residents 
SET age = CASE
     WHEN id = 1 THEN 21
     WHEN id = 2 THEN 25 
     WHEN id = 3 THEN 30 
     WHEN id = 4 THEN 27
     ELSE age
END
WHERE id IN (1, 2, 3, 4); 


CREATE TABLE residents_payment(
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    rent_start_date DATE NOT NULL,
    duration INT NOT NULL,
    rent_end_date DATE,
    customer_id INT,
    Foreign Key (customer_id) REFERENCES residents(id)
);

ALTER TABLE residents_payment
RENAME COLUMN time_duration TO duration;

ALTER TABLE residents_payment
CHANGE COLUMN duration time_duration INT;

ALTER TABLE residents_payment
MODIFY COLUMN duration INT NOT NULL;

ALTER TABLE residents_payment
MODIFY payment_id INT AUTO_INCREMENT;

ALTER TABLE residents_payment
DROP  Foreign Key fk_customer_id;

ALTER TABLE residents_payment
MODIFY customer_id INT AUTO_INCREMENT;

ALTER TABLE residents_payment
ADD CONSTRAINT fk_customer_id FOREIGN KEY (payment_id) REFERENCES residents(id);

ALTER TABLE residents_payment
DROP customer_id


INSERT INTO residents_payment (rent_start_date, duration)
VALUES
('2024-09-23', 1),
('2023-08-05', 3),
('2025-07-21', 2),
('2023-04-03', 1);

SELECT * FROM edward_hostels.residents;

DESC residents_payment

SHOW CREATE TABLE residents_payment

SELECT * FROM edward_hostels.residents
ORDER BY id ASC

SELECT * FROM edward_hostels.residents
WHERE phone_number LIKE "%21%"
ORDER BY id ASC

UPDATE residents  SET age = age+1 
WHERE phone_number LIKE "%21%" AND other_names LIKE "% %";
SELECT AVG(age) FROM residents;
SELECT COUNT(first_name) FROM residents;

SELECT first_name FROM residents
WHERE age > (SELECT AVG(age) FROM residents);

