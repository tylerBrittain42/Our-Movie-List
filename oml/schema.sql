DROP TABLE IF EXISTS movie_list;
DROP TABLE IF EXISTS users_list;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS movie;
DROP TABLE IF EXISTS list;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name CHAR(30) UNIQUE NOT NULL,
    password CHAR(30) NOT NULL DEFAULT 'pass'
);

CREATE TABLE movie(
    id SERIAL PRIMARY KEY,
    title CHAR(100) NOT NULL,
    genre CHAR(50) DEFAULT 'n/a',
    year CHAR(4) DEFAULT 'n/a',
    director CHAR(1000) DEFAULT 'n/a',
    actor CHAR(200) DEFAULT 'n/a',
    imdb CHAR(10) DEFAULT 'n/a',
    score float4 DEFAULT -1,
    plot text DEFAULT 'n/a',
    custom_input BOOLEAN DEFAULT FALSE
);

CREATE TABLE list(
    id SERIAL PRIMARY KEY,
    name CHAR(80)
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

