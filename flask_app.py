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

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'

db.create_all()

#Persons.query.all()
#Persons.query.count()
#Persons.query.filter_by(name='Amy')
#Persons.query.filter(Persons.name == 'Amy')
#Persons.query.get(1) <- gets by primary key


#db.session.query(Person) <=> Person.query
#session.query(Person).join(Team)

#db.session.add(person)
#db.session.add_all([person1, person2])
#db.session.rollback()
#db.session.commit()

@app.route('/')
def index():
    person = Persons.query.first()
    return 'Hello, ' + person.name


if __name__ == "__main__":  
    app.run(debug=True)