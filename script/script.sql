DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_seq;

DROP TABLE IF EXISTS registers;
DROP SEQUENCE IF EXISTS registers_seq;

CREATE TABLE users (
	id INT PRIMARY KEY NOT NULL,
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL,
	password VARCHAR(32) NOT NULL
);

CREATE SEQUENCE users_seq START 1 MINVALUE 1 INCREMENT 1;
ALTER TABLE users ALTER COLUMN id SET DEFAULT nextval('users_seq');

CREATE TABLE registers (
	id INT PRIMARY KEY NOT NULL,
	passwordDescription VARCHAR(255) NOT NULL,
	passwordContent VARCHAR(255) NOT NULL,
	id_user INT REFERENCES users(id)
);

CREATE SEQUENCE registers_seq START 1 MINVALUE 1 INCREMENT 1;
ALTER TABLE registers ALTER COLUMN id SET DEFAULT nextval('registers_seq');

INSERT INTO users (name, email, password) VALUES 
('usuario de teste', 'user@teste.com', '123'),
('usuario de teste 2', 'user2@teste.com', '1234'),
('usuario de teste 3', 'user3@teste.com', '12345'),
('usuario de teste 4', 'user4@teste.com', '123456');

INSERT INTO registers (passwordDescription, passwordContent, id_user) VALUES
('Senha do PassGuard', '123', 1),
('Senha do PassGuard', '1234', 2),
('Senha do PassGuard', '12345', 3),
('Senha do PassGuard', '123456', 4);