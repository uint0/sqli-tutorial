DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS blogs;
DROP TABLE IF EXISTS secrets;

-- BEGIN PUBLIC
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);

CREATE TABLE blogs (
    id INTEGER PRIMARY KEY,
    author_id INTEGER REFERENCES users(id),
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
-- END PUBLIC

CREATE TABLE secrets (
    id INTEGER PRIMARY KEY,
    secret TEXT
);

INSERT INTO users VALUES
(1, 'see-ql-eye', 'password23', 'admin'),
(2, 'bobby', 'correcthorsebatterystaple', 'user'),
(3, 'ypfp', 'wordpass', 'user'),
(4, 'risi', 'qiesolaa', 'user');

INSERT INTO blogs VALUES
(1, 1, 'This is a title', 'This is some content'),
(2, 2, 'My first blog', 'You weren\'t meant to find this :('),
(3, 1, 'Hello World', 'The sky is blue');

INSERT INTO secrets VALUES
(1, 'psst.');
