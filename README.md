# week6_assignment
Explain your steps and findings in a README.md file. 

## Setup ##
1. Install SQLite Extension.
2. Download and Connect to University Database through SQLite.
3. Create .sql files for writing queries.
4. In VSCode, Command + Shift + P --> SQLite: Run Query to see outputs



## Data Analysis / Exploration ##
The following exploration was done on the university databases data:
1. Number of rows in dataset: 2201
2. Distinct years represented: 4
3. Distinct countries represented: 59
4. Country representation and counts: The top 5 countries in the data are USA, China, Japan, UK, Germany
5. Average score for institutions in the top 20 rankings: Harvard has an average score of 100.0, with Stanford having 95.3.
6. Viewing world rank by country, to see each country's average world rank versus best world ranking, seein that USA and UK schools have both achieved ranks of 1 and 3, which makes sense and the best rank a school in Japan has received is 13. This query uses min aggregation to find the best rankings achieved. 



## CRUD Operations ##
1. Inserting Duke Tech as an university in 2014 with world rank 350 and score 60.5. All other column values are filled with no values.
2. There are 6 universities from Japan that show up in the global top 200 in 2013.
3. The database is updated to reflect the new calculation for the University of Oxford 2014 score.
4. The database is updated to reflect where score < 45 AND year = 2015.


