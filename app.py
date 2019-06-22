from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Wilfred',
        'title': 'Go home',
        'content': 'I am good',
        'date_posted': 'July 28 2019'
    },
    {
        'author': 'Kid',
        'title': 'Go home',
        'content': 'I am good',
        'date_posted': 'July 27 2019'
    }
]
@app.route('/')
@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html',title='About page')


if __name__ == '__main__':
    app.run(debug=True)
