-- script that lists all the cities of California that can be found in the database
SELECT cities.id, cities.name
FROM cities
WHERE states_id = (
    SELECT ID FROM states WHERE name = '    California'
)
ORDER BY cities.id ASC;
