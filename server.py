from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    data = response.json()

    return render_template("index.html", all_blogs = data)

@app.route('/post/<post_id>')
def get_post(post_id):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    post_found = all_posts[int(post_id) - 1]
    print(post_found)

    return render_template("post.html", post_id = post_id, post_found = post_found)



if __name__ == "__main__":
    app.run(debug=True)
