-- Import the database dump from hbtn_0d_tvshows

SELECT genres.name AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres_id = tv_show_genres.genre_id
GROUP BY genre_id
ORDER BY number_of_shows DESC;
