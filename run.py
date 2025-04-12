import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

# Create app factory
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Replace with your database URI
    app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key for production

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Temporary in-memory storage for user profiles
    user_profiles = {}

    @app.route('/')
    def home():
        if 'username' not in session:
            return redirect(url_for('login'))
        return render_template('home.html', username=session['username'])

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            try:
                username = request.form['username']
                email = request.form['email']
                password = request.form['password']

                # Check if the username already exists
                if username in user_profiles:
                    flash("Username already exists. Please choose another one.", "error")
                    return redirect(url_for('signup'))
                
                # Save the user's data
                user_profiles[username] = {
                    'email': email,
                    'password': password
                }
                flash("Account created successfully!", "success")
                return redirect(url_for('login'))

            except KeyError:
                flash("All fields are required. Please try again.", "error")
                return redirect(url_for('signup'))

        return render_template('signup.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username') # type: ignore
            password = request.form.get('password')

            if username in user_profiles and user_profiles[username]['password'] == password:
                session['username'] = username  # Store username in session
                flash("Login successful!", "success")
                return redirect(url_for('home'))
            else:
                flash("Invalid username or password. Please try again.", "error")
                return redirect(url_for('login'))

        return render_template('login.html')

    @app.route('/profile', methods=['GET', 'POST'])
    def profile():
        if 'username' not in session:
            flash("Please log in to view your profile.", "error")
            return redirect(url_for('login'))

        username = session['username']
        user = user_profiles.get(username, {})  # Fetch user data

        if request.method == 'POST':
            # Update user email if changed
            user['email'] = request.form.get('email', user['email'])
            flash("Profile updated successfully!", "success")
            return redirect(url_for('profile'))

        return render_template('profile.html', user=user)

    @app.route('/users')
    def users():
        if 'username' not in session:
            flash("Please log in to view public profiles.", "error")
            return redirect(url_for('login'))
        
        # Display all user profiles
        public_profiles = [
            {'username': username, 'email': data['email']}
            for username, data in user_profiles.items()
        ]
        return render_template('users.html', profiles=public_profiles)

    @app.route('/logout')
    def logout():
        session.pop('username', None)
        flash("You have been logged out.", "info")
        return redirect(url_for('login'))

    return app

# Run the application
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)