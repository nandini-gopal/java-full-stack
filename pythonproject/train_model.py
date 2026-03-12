import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# ==============================
# Load CSVs
# ==============================
books = pd.read_csv(r"C:\Users\mundl\OneDrive\Documents\pythonproject\Books.csv", low_memory=False)
ratings = pd.read_csv(r"C:\Users\mundl\OneDrive\Documents\pythonproject\Ratings.csv", low_memory=False)

# Merge books with ratings
ratings_with_books = ratings.merge(books, on="ISBN", how="left")

# ==============================
# Filter active users (more than 200 ratings)
# ==============================
user_ratings_count = ratings_with_books.groupby("User-ID")["Book-Rating"].count()
active_users = user_ratings_count[user_ratings_count > 200].index

filtered_ratings = ratings_with_books[ratings_with_books["User-ID"].isin(active_users)].copy()  # <- add .copy()

# ==============================
# Filter popular books (more than 50 ratings)
# ==============================
book_ratings_count = filtered_ratings.groupby("Book-Title")["Book-Rating"].count()
popular_books = book_ratings_count[book_ratings_count > 50].index

final_ratings = filtered_ratings[filtered_ratings["Book-Title"].isin(popular_books)].copy()  # <- add .copy()

# ==============================
# Compute number of ratings and average ratings
# ==============================
final_ratings['num_ratings'] = final_ratings.groupby('Book-Title')['Book-Rating'].transform('count')
final_ratings['avg_ratings'] = final_ratings.groupby('Book-Title')['Book-Rating'].transform('mean')

# ==============================
# Create pivot table
# ==============================
pivot_table = final_ratings.pivot_table(
    index="Book-Title",
    columns="User-ID",
    values="Book-Rating"
).fillna(0)

# ==============================
# Compute similarity matrix
# ==============================
similarity_scores = cosine_similarity(pivot_table)

# ==============================
# Save pivot table and similarity scores
# ==============================
pickle.dump(pivot_table, open(r"C:\Users\mundl\OneDrive\Documents\pythonproject\pivot.pkl", "wb"))
pickle.dump(similarity_scores, open(r"C:\Users\mundl\OneDrive\Documents\pythonproject\model.pkl", "wb"))

# ==============================
# Save popular books for home page
# ==============================
popular_df = final_ratings.drop_duplicates('Book-Title').sort_values('num_ratings', ascending=False).head(20)
pickle.dump(popular_df, open(r"C:\Users\mundl\OneDrive\Documents\pythonproject\popular_books.pkl", "wb"))

print("✅ pivot.pkl, model.pkl, and popular_books.pkl created successfully!")
