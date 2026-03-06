-- Import the database dump from hbtn_0d_tvshows

SELECT genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows_id = tv_show_genres.tv_show_id
JOIN genres ON tv_show_genres.genre_id = genres_id
WHERE tv_shows.title = 'Dexter'
ORDER BY genre.name ASC;
