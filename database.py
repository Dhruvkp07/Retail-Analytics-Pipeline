import sqlite3
import pandas as pd

conn = sqlite3.connect("database/products.db")

query = """
SELECT
    category,
    SUM(rating_count) as total_reviews
FROM products
GROUP BY category
ORDER BY total_reviews DESC
"""

result = pd.read_sql(query, conn)

print(result)

conn.close()