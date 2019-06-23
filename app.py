from flask import Flask, request
from flask_cors import CORS
import AnimeRecommender

app = Flask(__name__)
CORS(app)

def getList(user):
    return user

@app.route("/", methods=['GET'])
def sendList():
    try:
        #return str(getList(request.args['u']))
        return str(AnimeRecommender.get_recommendations(request.args['u']))
    except ValueError:
        return "Invalid username"

@app.route("/test/", methods=['GET'])
def testList():
    try:
        return "fma`google.ca~gintama`facebook.com~loli`bing.com~"
    except ValueError:
        return "test failed"

if __name__ == '__main__':
    app.run(debug=True)