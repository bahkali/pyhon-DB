from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Jerico05@localhost:5433/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Persons(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column( db.String(), nullable=False)

    # def __init__(self, name):
    #     self.name = name


db.create_all()


@app.route('/')
def index():
    person = Persons.query.first()
    return 'Hello, ' + person.name


if __name__ == "__main__":
    
    app.run(debug=True)