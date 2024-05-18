from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('home.html')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sing_up():
    if request.method == "POST":
        FirstName = request.form.get('FirstName')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(FirstName) < 4:
            flash('First name must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters', category='error')
        else:
            flash('You have successfully registered', category='success')

    return render_template('sign_up.html')
