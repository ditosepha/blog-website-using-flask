from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)



all_blogs = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
blog_objects = []

for blogs in all_blogs:
    blog_obj = Post(id=blogs['id'], title=blogs['title'], subtitle=blogs['subtitle'], body=blogs['body'])
    blog_objects.append(blog_obj)


@app.route('/')
def home():
    return render_template("index.html", blogs=blog_objects)

@app.route('/post/<int:index>')
def posts(index):
    requested_blog = None
    for blog_post in blog_objects:
        if blog_post.id == index:
            requested_blog = blog_post
    return render_template('post.html', blog=requested_blog)


if __name__ == "__main__":
    app.run(debug=True)























# @app.route('/')
# def home():
#     response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
#     all_blogs = response.json()
#     print(all_blogs)
#     return render_template("index.html", blogs=all_blogs)

# @app.route('/post/<id>')
# def posts(id):



# if __name__ == "__main__":
#     app.run(debug=True)


