Techido Career Guidance Using ML
Techido Career Guidance Using ML is a web application designed to help users explore job opportunities, register their profiles, and receive career recommendations based on their skills and qualifications. Built with Flask, MongoDB, and machine learning (ML) components, it provides a user-friendly interface for job seekers to sign up, log in, search for jobs, and manage their profiles.
Features

User Authentication: Secure sign-up and login with password hashing using bcrypt.
Profile Registration: Users can submit their personal details (name, email, CGPA, degree, etc.) and upload resumes.
Job Search: Search for jobs based on titles, with details like role, salary, skills, and qualifications loaded from a CSV file.
Session Management: Tracks logged-in users with Flask sessions.
Responsive UI: Simple, styled templates for login, signup, and other pages.

Prerequisites
Before running the application, ensure you have the following installed:

Python 3.8+: Download from python.org.
MongoDB: Install and run MongoDB Community Edition (mongodb.com).
Git: For cloning the repository (git-scm.com).
A web browser (e.g., Chrome, Firefox).

Installation

Clone the Repository:
git clone https://github.com/<your-username>/Techido_Career_Guidance_Using_ML.git
cd Techido_Career_Guidance_Using_ML


Set Up a Virtual Environment (Optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install flask pymongo bcrypt


Start MongoDB:

Ensure MongoDB is running on the default port (localhost:27017):mongod


If MongoDB is not installed, follow the MongoDB installation guide.


Static Files: Ensure static/home.png exists in the static/ folder. If missing, create a placeholder image or remove the <img> tag in templates/login.html:<div class="image-container">
    <!-- Remove image -->
</div>


Templates: Verify all templates (login.html, signup.html, home.html, register.html, about.html, jobs.html, skills.html, profile.html, search_results.html) are in the templates/ folder. Placeholder templates are provided in the Templates section below.



Running the Application

Clear MongoDB Users Collection (Recommended for first run):

Run this script to clear invalid password data from the users collection:from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['Db']
users_collection = db['users']
users_collection.delete_many({})
print("Cleared users collection")




Start the Flask Server:
python app.py


The application will run on http://localhost:5000.
Check the terminal for logs like:Connected to MongoDB successfully!
* Running on http://127.0.0.1:5000




Access the Application:

Open http://localhost:5000 in a web browser.
Sign Up: Go to /signup to create a new user (e.g., username: testuser, password: testpass).
Login: Log in with the same credentials at /.
Explore other routes: /home, /register, /jobs, /skills, /profile, /about, /search.



Usage

Sign Up: Create an account at /signup with a unique username and password.
Login: Log in at / to access protected routes.
Register Profile: Complete your profile at /register with personal details and a resume (PDF).
Search Jobs: Use the search bar on /home or visit /search?q=<query> (e.g., /search?q=Software) to find jobs.
Logout: Click the logout link to end the session.

Project Structure
Techido_Career_Guidance_Using_ML/
├── app.py                  # Main Flask application
├── job_descriptions.csv    # CSV file with job data
├── static/
│   └── home.png           # Image for login page
├── templates/
│   ├── login.html         # Login page
│   ├── signup.html        # Sign-up page
│   ├── home.html          # Home page
│   ├── register.html      # Profile registration
│   ├── about.html         # About page
│   ├── jobs.html          # Jobs page
│   ├── skills.html        # Skills page
│   ├── profile.html       # Profile page
│   ├── search_results.html # Search results page
└── README.md              # This file

Templates
If templates are missing, use these placeholders in the templates/ folder:
signup.html
<!DOCTYPE html>
<html>
<head>
    <title>Sign Up</title>
    <style>
        body { display: flex; justify-content: center; align-items: center; height: 100vh; background: linear-gradient(-135deg, #c850c0, #4158d0); }
        .form { width: 300px; padding: 20px; border: 2px solid white; border-radius: 8px; color: white; }
        input { width: 100%; padding: 8px; margin: 10px 0; }
        button { width: 100%; padding: 10px; background: #c850c0; border: none; color: white; cursor: pointer; }
        a { color: white; }
    </style>
</head>
<body>
    <div class="form">
        <h1>Sign Up</h1>
        <form method="POST" action="/signup">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <button type="submit">Sign Up</button>
            <p>Already have an account? <a href="/">Login</a></p>
        </form>
    </div>
</body>
</html>

home.html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Career Guidance</h1>
    <p>Hello, {{ session.username }}!</p>
    <a href="/register">Register</a> | <a href="/jobs">Jobs</a> | <a href="/skills">Skills</a> | <a href="/profile">Profile</a> | <a href="/about">About</a> | <a href="/logout">Logout</a>
    <form action="/search">
        <input type="text" name="q" placeholder="Search jobs...">
        <button type="submit">Search</button>
    </form>
</body>
</html>

register.html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST" action="/register" enctype="multipart/form-data">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <label for="dob">Date of Birth:</label>
        <input type="date" id="dob" name="dob" required>
        <label for="cgpa">CGPA:</label>
        <input type="text" id="cgpa" name="cgpa" required>
        <label for="degree">Degree:</label>
        <input type="text" id="degree" name="degree" required>
        <label for="stream">Stream:</label>
        <input type="text" id="stream" name="stream" required>
        <label for="resume">Resume (PDF):</label>
        <input type="file" id="resume" name="resume" accept=".pdf" required>
        <button type="submit">Register</button>
    </form>
    <a href="/home">Back to Home</a>
</body>
</html>

about.html
<!DOCTYPE html>
<html>
<head>
    <title>About</title>
</head>
<body>
    <h1>About</h1>
    <p>This is a career guidance platform.</p>
    <a href="/home">Back to Home</a>
</body>
</html>

jobs.html
<!DOCTYPE html>
<html>
<head>
    <title>Jobs</title>
</head>
<body>
    <h1>Jobs</h1>
    <p>List of available jobs.</p>
    <a href="/home">Back to Home</a>
</body>
</html>

skills.html
<!DOCTYPE html>
<html>
<head>
    <title>Skills</title>
</head>
<body>
    <h1>Skills</h1>
    <p>Enter your skills for job recommendations.</p>
    <a href="/home">Back to Home</a>
</body>
</html>

profile.html
<!DOCTYPE html>
<html>
<head>
    <title>Profile</title>
</head>
<body>
    <h1>Profile</h1>
    <p>Your profile details.</p>
    <a href="/home">Back to Home</a>
</body>
</html>

search_results.html
<!DOCTYPE html>
<html>
<head>
    <title>Search Results</title>
</head>
<body>
    <h1>Search Results for "{{ query }}"</h1>
    {% if results %}
        <ul>
        {% for title, info in results.items() %}
            <li>
                <h3>{{ title }}</h3>
                <p>Role: {{ info.role }}</p>
                <p>Salary: {{ info.salary }}</p>
                <p>Skills: {{ info.skills }}</p>
                <p>Location: {{ info.location }}</p>
                <p>Qualifications: {{ info.qualification }}</p>
                <p>Experience: {{ info.experience }}</p>
                <p>Company: {{ info.company }}</p>
            </li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No results found.</p>
    {% endif %}
    <a href="/home">Back to Home</a>
</body>
</html>

Troubleshooting

Login Error: "Invalid password format in database":

Cause: Invalid password hashes in MongoDB.
Fix: Clear the users collection:from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['Db']
users_collection = db['users']
users_collection.delete_many({})
print("Cleared users collection")


Sign up again at /signup.


Missing job_descriptions.csv:

Ensure job_descriptions.csv exists in the project root with the correct columns.


TemplateNotFound Error:

Verify all templates are in templates/. Use the placeholders above if missing.


Static File (home.png) 404:

Add home.png to static/ or remove the <img> tag in login.html.


Chrome Error: "Unchecked runtime.lastError":

Test in Incognito Mode (Ctrl+Shift+N).
Disable extensions at chrome://extensions/.
Clear cache at chrome://settings/clearBrowserData.
Try Firefox or Edge.


MongoDB Connection Error:

Ensure MongoDB is running (mongod).
Check the connection string: mongodb://localhost:27017/.



Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make changes and commit (git commit -m "Add feature").
Push to your fork (git push origin feature-branch).
Open a Pull Request.

# Contact
   Email    - vigneshpandiya21@gmail.com
   linkedIn - https://www.linkedin.com/in/vignesh-pandiya-099b30296/



![image](https://github.com/user-attachments/assets/c32ae837-fa31-4b89-afbd-9541e00c9a46)
![image](https://github.com/user-attachments/assets/cc27f606-f6e2-442b-86d5-5cde23aa1b70)
![image](https://github.com/user-attachments/assets/71af5142-4a22-4f64-a709-cc8924088c96)
![image](https://github.com/user-attachments/assets/6a41a16a-0843-406c-9615-cd47ff6f4ee2)
![image](https://github.com/user-attachments/assets/ac9418cd-392c-481c-a3c3-5f845005a7ee)


