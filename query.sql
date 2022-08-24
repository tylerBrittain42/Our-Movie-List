CREATE TABLE list (
    l_id INT PRIMARY KEY,
    l_added_on DATE NOT NULL DEFAULT CURRENT_DATE,
    l_rank SERIAL,
    l_added_by VARCHAR (50) NOT NULL
);

CREATE TABLE movie (
    m_id serial PRIMARY KEY,
    m_genre VARCHAR (50) NOT NULL DEFAULT 'N/A',
    m_score int NOT NULL,
    m_custom_input BOOL NOT NULL DEFAULT false,
    m_imdb VARCHAR (10) DEFAULT 'N/A'
);

