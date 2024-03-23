from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__, static_folder='static')

# Define routes and other configurations here

@app.route('/')
def index():
    return render_template('index.html')

# Add more routes as needed

if __name__ == '__main__':
    app.run(debug=True)
