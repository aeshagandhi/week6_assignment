/** Perform Basic Analysis - Write SQL queries to explore the dataset, 
including basic statistics and summary operations.
**/


SELECT * FROM university_rankings;

-- number of rows in data
SELECT COUNT(*) AS total_universities 
FROM university_rankings;

-- number of distinct years in data;
SELECT COUNT(DISTINCT year) AS distinct_years
FROM university_rankings;

-- number of countries represented
SELECT COUNT(DISTINCT country) AS distinct_countries
FROM university_rankings;


-- see country representation
SELECT country, COUNT(*) AS university_count
FROM university_rankings
GROUP BY country
ORDER BY university_count DESC;

-- average score for institutions in top 20 rankings
SELECT institution, AVG(score) AS average_score
FROM university_rankings
WHERE institution IN (
    SELECT institution
    FROM university_rankings
    WHERE world_rank <= 20
)
GROUP BY institution
HAVING COUNT(DISTINCT year) > 1
ORDER BY average_score DESC;

-- summarize world rank by country
SELECT country, AVG(world_rank) AS avg_world_rank, MIN(world_rank) AS best_world_rank
FROM university_rankings
GROUP BY country
ORDER BY best_world_rank ASC;


