from flask import Flask, request, jsonify, render_template, redirect, url_for  
from pymongo import MongoClient
import csv
import os

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')  # Connecting to MongoDB
db = client['Db']  # Selecting database
users_collection = db['users']  # Selecting collection
register_collection = db['register']  # Selecting collection

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Register:
    def __init__(self, name, email, dob, cgpa, degree, stream, resume):
        self.name = name
        self.email = email
        self.dob = dob
        self.cgpa = cgpa
        self.degree = degree
        self.stream = stream
        self.resume = resume

# Print a message when MongoDB connection is established
if client is not None:
    print("Connected to MongoDB successfully!")

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, 'job_descriptions.csv')

# Load job descriptions from CSV file into a dictionary
job_descriptions = {}

try:
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row['Job Title']
            role = row['Role']
            salary = row['Salary Range']
            skills = row['skills']
            location = row['location']
            qualification = row['Qualifications']
            experience = row['Experience']
            company = row['Company']
            job_descriptions[title] = {
                'role': role,
                'salary': salary,
                'skills': skills,
                'location': location,
                'qualification': qualification,
                'experience': experience,
                'company': company
            }
except FileNotFoundError:
    print("Error: File not found. Please make sure the CSV file exists.")
except PermissionError:
    print("Error: Permission denied. Make sure you have necessary permissions to access the file.")

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return jsonify({'message': 'All fields are required'}), 400

        # Check if username already exists in MongoDB
        if users_collection.find_one({'username': username}):
            return jsonify({'message': 'Username already exists'}), 400

        # Insert user data into MongoDB
        users_collection.insert_one({'username': username, 'password': password})
        return redirect(url_for('login'))  # Redirect to registration page after signup
    else:
        return render_template('signup.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        dob = request.form.get('dob')
        cgpa = request.form.get('cgpa')
        degree = request.form.get('degree')
        stream = request.form.get('stream')
        resume = request.files['resume'].read()

        if not all([name, email, dob, cgpa, degree, stream, resume]):
            return jsonify({'message': 'All fields are required'}), 400

        # Insert registration data into MongoDB
        register_data = {
            'name': name,
            'email': email,
            'dob': dob,
            'cgpa': cgpa,
            'degree': degree,
            'stream': stream,
            'resume': resume
        }
        register_collection.insert_one(register_data)
        return redirect(url_for('home'))  # Redirect to home page after registration
    else:
        return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400

    # Query MongoDB for the user
    user = users_collection.find_one({'username': username, 'password': password})

    if user:
        return redirect(url_for('home'))  # Redirect to home page after successful login
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/logout')
def logout():
    # Perform logout actions here
    # For example, clear session data
    return redirect(url_for('home.html')) 

@app.route('/search')
def search():
    query = request.args.get('q')
    if query:
        results = {title: info for title, info in job_descriptions.items() if query.lower() in title.lower()}
    else:
        results = {}
    return render_template('search_results.html', query=query, results=results)

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print("An error occurred:", e) 