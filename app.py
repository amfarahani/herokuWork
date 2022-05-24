from flask import Flask
app2 = Flask(__name__)
@app2.route('/')
def hello():
   return 'Hello, World!'
if __name__ == '__name__':
    app2.run(debug=True)


