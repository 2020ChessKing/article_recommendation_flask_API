from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

# Get Data
csv_array_data = []

with open("articles.csv", encoding="utf-8") as file:
    csv_data = csv.reader(file)

    for rows in file:
        csv_array_data.append(rows)

headers = "id" + csv_array_data[0]
all_articles = csv_array_data[1:]

liked_articles = []
disliked_articles = []

@app.route('/get-articles')
def get_articles():
    return jsonify({
        "data": all_articles,
        "status": "success"
    })


@app.route('/like-article', methods=['POST'])
def like_article(all_articles=all_articles, liked_articles=liked_articles):
    article = all_articles[0]
    all_articles = all_articles[1:]

    liked_articles.append(article)

    return jsonify({
        "status": "success",
    })

@app.route('/dislike-article', methods=['POST'])
def dislike_article(all_articles=all_articles, disliked_articles=disliked_articles):
    article = all_articles[0]
    all_articles = all_articles[1:]

    disliked_articles.append(article)

    return jsonify({
        "status": "success",
    })

if __name__ == '__main__':
    app.debug = True
    app.run()
