--Select all data of the Client_List Table
SELECT *
FROM Client_List;

--Insert values into the Client_List Table in tree_crm database
INSERT INTO Client_List (Client_Name, Email_Address, Phone_Number, Client_Num)
VALUES
('Max','mymail@mail.com','123-456-7890','1212'),
('Manny','businessemail@mail.com','121-333-4444','555'),
('Benny','fakemail@mail.com','333-333-4444','777'),
('Gary','gmail@mail.com','321-098-5514','345'),
('Spongebob','pineapple@mail.com','456-333-0000','999'),
('Patrick','rocky@mail.com','000-000-0000','44'),
('Larry','muscles@mail.com','898-547-9090','333'),
('Daniel','byebye@mail.com','787-901-6489','3232');

--Update email of a Client_Name in Client_List Table
UPDATE Client_List
SET Email_Address = 'GaryBear@mail.com'
WHERE Client_Name = 'Gary';


--Delete a record in Client_List Table
DELETE FROM Client_List
WHERE Client_Name = 'Max';
