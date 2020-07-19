-- BEGIN PUBLIC
-- Pretend this doesn't exist. I cbs removing the box.
-- END PUBLIC

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE flags (
    id INTEGER PRIMARY KEY,
    flag TEXT,
    score INTEGER
);

CREATE TABLE solves (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    flag_id INTEGER REFERENCES flag(id)
);

INSERT INTO users(id, username, password) VALUES
(1, 'leethacker', 'hunter3'),
(2, 'admin', 'password'),
(3, 'skiddy123', 'jasdfjkljsdafkljskljglkvlklkdsajfjowier');

INSERT INTO flags(id, flag, score) VALUES
(1, 'FLAG{yeah_no}', 10),
(2, 'FLAG{coming_up_with}', 25),
(3, 'FLAG{real_flags_is}', 50),
(4, 'FLAG{already_hard_enough}', 75),
(5, 'FLAG{im_not_coming_up}', 100),
(6, 'FLAG{with_fake_flags}', 125);

INSERT INTO solves(id, user_id, flag_id) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 2, 1),
(6, 2, 5);
