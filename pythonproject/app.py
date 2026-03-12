from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load files
similarity = pickle.load(open("model.pkl", "rb"))
pivot_table = pickle.load(open("pivot.pkl", "rb"))
books = pickle.load(open("books.pkl", "rb"))

def recommend(book_name):
    index = np.where(pivot_table.index == book_name)[0][0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in scores:
        title = pivot_table.index[i[0]]
        image = books[books['Book-Title'] == title]['Image-URL-L'].values[0]
        data.append((title, image))

    return data

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []

    if request.method == "POST":
        book_name = request.form.get("book")
        if book_name in pivot_table.index:
            recommendations = recommend(book_name)

    return render_template(
        "index.html",
        book_list=pivot_table.index,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)
