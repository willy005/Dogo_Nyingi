from flask import Flask, render_template, url_for, flash, redirect
from secretkey import secret_key
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key()
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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account Created Successfully', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '1234':
            flash('You have been logged in well', 'success')
            return redirect(url_for('home'))
        else:
            flash('Log in unsuccessful please check your email or password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
