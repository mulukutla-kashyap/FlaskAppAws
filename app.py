from flask import Flask
from flask_restx import Api, Resource
import os
from werkzeug.contrib.fixers import ProxyFix

flask_app = Flask(__name__)
flask_app.wsgi_app = ProxyFix(flask_app.wsgi_app)

api = Api(app=flask_app,
          version="1.0",
          title="Fun Stuff",
          description="some fun utility functions like spinning the dice, getting names for your Dog etc. ")


@api.route("/test")
class GetHelloWorld(Resource):
    def get(self):
        '''
        Just return Hello World

        This API will give you a resonse hello world'''

        return {
            "response": "hello world!!"
        }


def main():
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host='127.0.0.1', port=port)


if __name__ == '__main__':
    main()
