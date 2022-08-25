CREATE TABLE list (
    l_id INT PRIMARY KEY,
    l_added_on DATE NOT NULL DEFAULT CURRENT_DATE,
    l_rank SERIAL,
    l_added_by VARCHAR (50) NOT NULL
);

CREATE TABLE movie (
    m_id serial PRIMARY KEY,
    m_title VARCHAR (100) NOT NULL,
    m_genre VARCHAR (50) NOT NULL DEFAULT 'N/A',
    m_year VARCHAR (6) NOT NULL DEFAULT 'N/A',
    m_plot VARCHAR (200) DEFAULT 'Not available',
    m_director VARCHAR (100) DEFAULT 'N/A',
    m_actor VARCHAR (200) DEFAULT 'N/A',
    m_score int NOT NULL,
    m_custom_input BOOL NOT NULL DEFAULT false,
    m_imdb VARCHAR (10) DEFAULT 'temp'
);
