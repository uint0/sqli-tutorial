-- BEGIN PUBLIC
-- No help this time :'(
-- END PUBLIC

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);
CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    name TEXT,
    user_id INTEGER REFERENCES users(id),
    balance INTEGER
);
CREATE TABLE cards (
    user_id INTEGER REFERENCES users(id),
    card_number TEXT NOT NULL
);

INSERT INTO users VALUES
(1, 'iamauser', 'password123'),
(2, 'quoccabank', 'heheullneverfindme'),
(3, 'quoccabankisdumb', 'lmao');

INSERT INTO accounts VALUES
(1, 'myaccount', 1, 1000),
(2, 'netbank', 2, 9000),
(3, 'quoccastash', 3, 10239);

INSERT INTO cards(user_id, card_number) VALUES
(1, '0000 0000 0000 0000'),
(1, '9192 2849 2123 2039'),
(2, '1929 3920 1020 0000');
