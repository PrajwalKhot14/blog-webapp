from flask import Flask, render_template, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c156f7e7f28ffd5594e1cae9a42c6303'


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/login")
def login():
    return render_template('login.html', title = 'Login')

@app.route("/register")
def register():
    return render_template('register.html', title = 'Register')


if __name__ == '__main__':
    app.run(debug=True)