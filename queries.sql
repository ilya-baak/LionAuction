DELETE FROM users WHERE firstname = 'Markus';
DELETE FROM users WHERE firstname = 'Jay';

DELETE FROM users WHERE firstname = 'email';

ALTER TABLE users RENAME COLUMN firstname TO username;
ALTER TABLE users RENAME COLUMN lastname TO password;