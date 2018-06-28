import datetime
from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pttzkoki364@localhost/dataLogger'
app.debug = True
db = SQLAlchemy(app)

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True) #user
    dKey = db.Column(db.String(80), unique=False) #user
    temperature = db.Column(db.String(80), unique=False)
    dtime = db.Column(db.String(120), unique=True)

    def __init__(self, dKey, temperature, dtime):
        self.dKey = dKey
        self.temperature = temperature
        self.dtime = dtime

    def __repr__(self):
        return '<Sensor %r' % self.dKey

@app.route('/')
def index():
    return "Hello World"

@app.route('/query', methods=['GET'])
# ex request http://127.0.0.1:5000/query?dKey=VdKey&temp=Vtemp
def query():
    dKey = request.args.get('dKey') #if key doesn't exist, returns None
    print(dKey)
    temperature = str(request.args['temp']) #if key doesn't exist, returns a 400, bad request error
    #dtime = request.args.get('dtime')
    dtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # return '''<h1>The language value is: {}</h1>
    #           <h1>The framework value is: {}</h1>
    #           <h1>The website value is: {}'''.format(language, framework, website)

    sensor = Sensor(dKey, temperature, dtime)
    db.session.add(sensor)
    db.session.commit()

    return "Data Logged!"
    # return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
