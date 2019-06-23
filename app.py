from flask import Flask, request
from flask_cors import CORS
#import AnimeRecommender

app = Flask(__name__)
CORS(app)

def getList(user):
    return user

@app.route("/", methods=['GET'])
def sendList():
    try:
        return str(getList(request.args['u']))
        #return str(AnimeRecommender.get_recommendations(request.args['u']))
    except ValueError:
        return "Lol big dumb"

if __name__ == '__main__':
    app.run(debug=True)