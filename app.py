from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to Lele Ride!</h1>
    <p>Amharic: እንኳን ደህና መጡ ወደ Lele Ride!</p>
    <p>Tigrinya: ሰላም ተገንዘብ Lele Ride!</p>
    """

if __name__ == '__main__':
    app.run(debug=True)Add starter code for app.py
