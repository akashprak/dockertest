from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET'])
@app.route('/home', methods = ['GET'])
def home():
    return '<h1> Test message: This app has now been deployed on AWS EC2 using github actions </h1>'

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)