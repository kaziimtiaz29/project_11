from application import db

class MEALS(db.Model):
    meal_id = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20),nullable=True)
    quantity = db.Column(db.Integer,nullable=True)
    tables = db.relationship('Tables', backref='meals') 

class Tables(db.Model):
    table_no = db.Column(db.Integer, primary_key=True)
    no_of_people = db.Column(db.Integer, nullable=False)
    time_booked = db.Column(db.DateTime, nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('MEALS.meal_id'),nullable=False)