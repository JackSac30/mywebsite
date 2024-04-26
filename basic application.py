from flask import Flask
app = Flask(__name__)

# Decorators add functionalities to existing functions ex: @example
# the home route can be accessed by / and /home
@app.route("/")
@app.route("/home")
def home():
    return "Hello, this is the home page"

# Create an about page
@app.route("/about")
def about():
    return "About page"

if __name__ == "__main__":
    app.run(debug=True)