DROP TABLE IF EXISTS playlist;

CREATE TABLE playlist(
    id SERIAL PRIMARY KEY,
    song_name VARCHAR(255),
    artist_name VARCHAR(255),
    video VARCHAR(255)
    
);