DELETE FROM users WHERE firstname = 'Markus';
DELETE FROM users WHERE firstname = 'Jay';

DELETE FROM users WHERE firstname = 'email';

ALTER TABLE users RENAME COLUMN firstname TO username;
ALTER TABLE users RENAME COLUMN lastname TO password;

ALTER TABLE users ADD COLUMN hashedpass


SELECT hashedpass FROM users WHERE username='arubertelli0@nsu.edu';

ALTER TABLE users DROP COLUMN password;

ALTER TABLE users RENAME COLUMN hashedpass TO password;

SELECT sql FROM sqlite_master WHERE type='table' AND name='users';

CREATE TABLE users2 (username TEXT PRIMARY KEY,
                     password TEXT

);

INSERT INTO users2(username, password) SELECT username, password FROM users;

DROP TABLE users;

ALTER TABLE users2 RENAME TO users;

