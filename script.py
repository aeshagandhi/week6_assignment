import sqlite3
import pandas as pd

def main():
    # Connect to the SQLite database
    conn = sqlite3.connect("university_database.db")
    cursor = conn.cursor()

    print("\n****** Data Exploration ***********")
    # view full data
    df_all = pd.read_sql_query("SELECT * FROM university_rankings;", conn)
    print("Full data:\n", df_all.head())

    # count total universities
    total_universities = pd.read_sql_query(
        "SELECT COUNT(*) AS total_universities FROM university_rankings;", conn
    )
    print("\nTotal universities:\n", total_universities)

    # count distinct years
    distinct_years = pd.read_sql_query(
        "SELECT COUNT(DISTINCT year) AS distinct_years FROM university_rankings;", conn
    )
    print("\nDistinct years:\n", distinct_years)

    # count distinct countries
    distinct_countries = pd.read_sql_query(
        "SELECT COUNT(DISTINCT country) AS distinct_countries FROM university_rankings;", conn
    )
    print("\nDistinct countries:\n", distinct_countries)

    # country representation
    country_counts = pd.read_sql_query(
        """
        SELECT country, COUNT(*) AS university_count
        FROM university_rankings
        GROUP BY country
        ORDER BY university_count DESC;
        """, conn
    )
    print("\nUniversity count by country:\n", country_counts)

    # average score for institutions in top 20
    avg_score_top20 = pd.read_sql_query(
        """
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
        """, conn
    )
    print("\nAverage score for top 20 institutions:\n", avg_score_top20)

    # summarize world rank by country
    country_rank_summary = pd.read_sql_query(
        """
        SELECT country, AVG(world_rank) AS avg_world_rank, MIN(world_rank) AS best_world_rank
        FROM university_rankings
        GROUP BY country
        ORDER BY best_world_rank ASC;
        """, conn
    )
    print("\nWorld rank summary by country:\n", country_rank_summary)

    # preview top 10 rows
    top10 = pd.read_sql_query("SELECT * FROM university_rankings LIMIT 10;", conn)
    print("\nTop 10 rows:\n", top10)

    print("\n****** CRUD Operations / Exercises ***********")

    # Exercise 1: Insert new university 
    cursor.execute("""
        INSERT INTO university_rankings (institution, country, world_rank, score, year)
        VALUES ('Duke Tech', 'USA', 350, 60.5, 2014);
    """)
    conn.commit()

    # Confirm insert
    duke_check = pd.read_sql_query(
        """
        SELECT * FROM university_rankings
        WHERE institution = 'Duke Tech' AND year = 2014;
        """, conn
    )
    print("\nInserted Duke Tech:\n", duke_check)

    # Exercise 2: Japan universities in top 200 (2013) 
    japan_top200_2013 = pd.read_sql_query(
        """
        SELECT COUNT(*) AS japan_count
        FROM university_rankings
        WHERE country = 'Japan' AND world_rank <= 200 AND year = 2013;
        """, conn
    )
    print("\nJapan universities in top 200 (2013):\n", japan_top200_2013)

    # Exercise 3: Fix Oxford's score in 2014 
    cursor.execute("""
        UPDATE university_rankings
        SET score = score + 1.2
        WHERE institution = 'University of Oxford' AND year = 2014;
    """)
    conn.commit()

    oxford_check = pd.read_sql_query(
        """
        SELECT * FROM university_rankings
        WHERE institution = 'University of Oxford' AND year = 2014;
        """, conn
    )
    print("\nUpdated Oxford 2014 score:\n", oxford_check)

    # Exercise 4: Remove under-45 scorers in 2015 
    cursor.execute("""
        DELETE FROM university_rankings
        WHERE score < 45 AND year = 2015;
    """)
    conn.commit()

    # Verify deletion
    deleted_rows_check = pd.read_sql_query(
        """
        SELECT COUNT(*) AS remaining_2015_under_45
        FROM university_rankings
        WHERE score < 45 AND year = 2015;
        """, conn
    )
    print("\nRemaining 2015 records with score < 45:\n", deleted_rows_check)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
