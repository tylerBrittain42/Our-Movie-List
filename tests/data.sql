DROP TABLE IF EXISTS movie_list;
DROP TABLE IF EXISTS users_list;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS movie;
DROP TABLE IF EXISTS list;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE movie(
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT DEFAULT 'n/a',
    year TEXT DEFAULT 'n/a',
    director TEXT DEFAULT 'n/a',
    actor TEXT DEFAULT 'n/a',
    imdb TEXT DEFAULT 'n/a',
    score float4 DEFAULT -1,
    plot text DEFAULT 'n/a',
    custom_input BOOLEAN DEFAULT FALSE
);

CREATE TABLE list(
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE users_list(
    u_id INT NOT NULL,
    l_id INT NOT NULL,
    PRIMARY KEY (u_id, l_id),
    FOREIGN KEY (u_id)
        REFERENCES users(id),
    FOREIGN KEY (l_id)
        REFERENCES list(id)
);

CREATE TABLE movie_list(
    m_id INT NOT NULL,
    l_id INT NOT NULL,
    PRIMARY KEY(m_id, l_id),
    FOREIGN KEY (m_id)
        REFERENCES movie(id),
    FOREIGN KEY (l_id) 
        REFERENCES list(id)
);


INSERT INTO users (name, password)
VALUES
  ('test', 'pbkdf2:sha256:260000$E7cFv4DtMdFEoDuT$749d25fafcb8181e6ac0f0bc111fb7056646ba2f3b7bf762b07e7070e7c1078a'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');
  