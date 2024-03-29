drop table python_de.employees;

create table python_de.employees(
	id int auto_increment,
    first_name varchar(20),
    last_name varchar(20),
    dob date,
    department varchar(5) not null,
    phone_number varchar(15) unique,
    primary key(id)
);

insert into python_de.employees(first_name, last_name, dob, department, phone_number)
values 
('Paul', 'Brandon', '1978-03-12', 'Sales', '+41 456234'),
('Tina', 'Nailor', '1980-11-09', 'HR', '+41 987456'),
('John', 'Doe', '1995-07-14', 'IT', '+41 877245');