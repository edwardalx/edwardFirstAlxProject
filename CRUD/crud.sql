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
INSERT INTO residents (first_name, other_names, phone_number, email)
VALUES 
('Ruth', 'Obaapa', 0243161162, 'ruth@mail.com'),
('Stephen', 'Akusika Ama', 0266185624, 'stephen@mail.com'),
('Webb', "Tip Toe", 0547112233, 'webbtip@mail.com'),
('Kofi', 'Ba Boni', 0836212111, 'baboni@mail.com');

SELECT * FROM edward_hostels.residents;

DESC residents


