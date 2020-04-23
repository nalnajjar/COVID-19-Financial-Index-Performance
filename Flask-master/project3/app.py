# import necessary libraries

import os

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask_jsonpify import jsonify

#Create a engine for connecting to SQLite3.

kr = create_engine('sqlite:///static/db/korea.db')
uk = create_engine('sqlite:///static/db/uk.db')
usa = create_engine('sqlite:///static/db/usa.db')

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
api = Api(app)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/animation', methods=['GET', 'POST'])
def animation():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('animation.html')


#################################################
# MODEL Setup
#################################################
class Korean(Resource):
    def get(self):
        conn = kr.connect()
        query = conn.execute("select * from korea")
        result = {'kr': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

class USA(Resource):
    def get(self):
        conn = usa.connect()
        query = conn.execute("select * from usa")
        result = {'usa': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

class UK(Resource):
    def get(self):
        conn = uk.connect()
        query = conn.execute("select * from uk")
        result = {'uk': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

 

api.add_resource(Korean, '/api/kr')
api.add_resource(USA, '/api/usa')
api.add_resource(UK, '/api/uk')

if __name__ == '__main__':
     app.run()



