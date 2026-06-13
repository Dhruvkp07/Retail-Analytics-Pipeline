import sqlite3
import pandas as pd

conn = sqlite3.connect("database/products.db")

queries = {

    "Products by Category": """
    SELECT
        category,
        COUNT(*) as total_products
    FROM products
    GROUP BY category
    ORDER BY total_products DESC
    """,

    "Average Price by Category": """
    SELECT
        category,
        ROUND(AVG(price), 2) as average_price
    FROM products
    GROUP BY category
    ORDER BY average_price DESC
    """,

    "Total Reviews by Category": """
    SELECT
        category,
        SUM(rating_count) as total_reviews
    FROM products
    GROUP BY category
    ORDER BY total_reviews DESC
    """,

    "Top 5 Highest Rated Products": """
    SELECT
        title,
        rating_rate
    FROM products
    ORDER BY rating_rate DESC
    LIMIT 5
    """,

    "Top 5 Most Reviewed Products": """
    SELECT
        title,
        rating_count
    FROM products
    ORDER BY rating_count DESC
    LIMIT 5
    """,

    "Most Expensive Products": """
    SELECT
        title,
        price
    FROM products
    ORDER BY price DESC
    LIMIT 5
    """,

    "Category Rating Performance": """
    SELECT
        category,
        ROUND(AVG(rating_rate),2) as avg_rating
    FROM products
    GROUP BY category
    ORDER BY avg_rating DESC
    """
}

for title, query in queries.items():
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    result = pd.read_sql(query, conn)
    print(result)

conn.close()