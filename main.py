import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://fakestoreapi.com/products"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

df["rating_rate"] = df["rating"].apply(lambda x: x["rate"])
df["rating_count"] = df["rating"].apply(lambda x: x["count"])

df = df.drop("rating", axis=1)

df.to_csv("data/products_cleaned.csv", index=False)

print(df.head())
print("\n")
print(df.info())

print("\nAverage Price:")
print(df["price"].mean())

highest_rated = df.loc[df["rating_rate"].idxmax()]

print("\nHighest Rated Product:")
print(highest_rated["title"])
print(highest_rated["rating_rate"])

print("\nProducts Per Category:")
print(df["category"].value_counts())

category_counts = df["category"].value_counts()

category_counts.plot(kind="bar")

plt.title("Products Per Category")
plt.xlabel("Category")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("charts/category_distribution.png")

print("Chart Saved Successfully")

top_products = df.nlargest(5, "rating_rate")

plt.figure(figsize=(10,5))

plt.bar(top_products["title"], top_products["rating_rate"])

plt.title("Top 5 Rated Products")
plt.xlabel("Product")
plt.ylabel("Rating")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("top_rated_products.png")

print("Top Rated Products Chart Saved")