-- BEGIN PUBlIC
-- lol no
-- END PUBLIC

CREATE TABLE scenarios (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    criticality INTEGER
);

CREATE TABLE challenges (
    id INTEGER PRIMARY KEY,
    title TEXT,
    question TEXT,
    scenario INTEGER REFERENCES scenarios(id)
);

INSERT INTO scenarios VALUES
(1, 'Crocca Insurance', 'Insurance Provider', 1),
(2, 'Crocca Elections', 'Trust us please', 3),
(3, 'Crocca Hospital',  'State of the art medical care', 5),
(4, 'Crocca Challenge Writers',   'Where we keep all the dumb people', 7);

INSERT INTO challenges VALUES
(1, 'Insurance 1', 'Get me usernames', 1),
(2, 'Insurance 2', 'Get me passwords', 1),
(3, 'Elections 1', 'Get me votes', 2),
(4, 'Hospital 1', 'Get me medical data', 3),
(5, 'ChalWriters 1', 'Get me chals', 4),
(6, 'ChalWriters 2', 'Get me handles', 4);
