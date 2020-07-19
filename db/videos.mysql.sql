-- BEGIN PUBLIC
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    postcode TEXT NOT NULL
);

CREATE TABLE videos (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL
);

CREATE TABLE rentals (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    video_id INTEGER REFERENCES videos(id),
    period INTEGER,
    payment TEXT NOT NULL
);
-- END PUBLIC

INSERT INTO users VALUES
(1, 'admin', 'youcanreally',     2000),
(2, 'videos', 'tellhowquickly',  2000),
(3, 'user', 'igotsickof',        2083),
(4, 'wowwhatasecretusernameowo', 'comingupwithdata', 2129);

INSERT INTO videos VALUES
(1, 'MyVideo1'),
(2, 'CaseConsistency1'),
(3, 'Whatis_astyleGuide?');

INSERT INTO rentals VALUES
(1, 1, 1, 5, 'card:1287398237498298'),
(2, 2, 3, 2, '3rdparty:myaccount@paypal'),
(3, 3, 1, 14, 'note:wowGreatDBDesignRightHere');
