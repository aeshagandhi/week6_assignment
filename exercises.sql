-- SQLite
SELECT * FROM university_rankings
LIMIT 10;

/** Exercise 1: The ranking committee has decided to publish new results for a new university in 2014. Insert this university into the database.
Institution: Duke Tech
Country: USA
World Rank: 350
Score: 60.5  **/

INSERT INTO university_rankings (institution, country, world_rank, score, year)
VALUES ('Duke Tech', 'USA', 350, 60.5, 2014);

-- confirm query results
SELECT * FROM university_rankings
WHERE institution = 'Duke Tech' AND year = 2014;


/** Exercise 2: A policy consultant has reached out to you with the following question. 
How many universities from Japan show up in the global top 200 in 2013? **/
SELECT COUNT(*) AS japan_count
FROM university_rankings
WHERE country = 'Japan' AND world_rank <= 200 AND year = 2013;

/** Exercise 3: The score for University of Oxford in 2014 was miscalculated. 
Increase its score by +1.2 points. Update the row to reflect this update.**/
UPDATE university_rankings
SET score = score + 1.2
WHERE institution = 'University of Oxford' AND year = 2014;

-- confirm query results
SELECT * FROM university_rankings
WHERE institution = 'University of Oxford' AND year = 2014;


/** Exercise 4: After reviewing, the ranking committee decided that universities with a score below 45 in 2015 should not have been included in the published dataset.
 Clean up the records to reflect this. **/
UPDATE university_rankings
DELETE FROM university_rankings
WHERE score < 45 AND year = 2015;

