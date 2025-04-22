from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/post', methods=['POST'])
def add_post():
    new_post = request.get_json()
    with open("post.json", "r") as file:
        posts = json.load(file)
    posts.insert(0, new_post)

@app.route('/api/posts')
def get_posts():
    
    with open ('posts.json', 'r') as file:
        posts = json.load(file)
    return jsonify(posts)

if __name__ == '__main__':
    app.run(debug=True)