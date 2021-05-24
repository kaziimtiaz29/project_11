# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask, config,url_for,redirect,render_template
# from flask.globals import request
# #from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.fields.core import DateField, IntegerField
from application import app
# app = Flask(__name__)

# #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# #app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://mysql_user:mysql_password>@mysql_instance_ip>:3306/<mysql_db>'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:1234@35.189.79.75:3306/project1'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY']='1234'
# db = SQLAlchemy(app)
# class MEALS(db.Model):
#     meal_id = db.Column(db.Integer, primary_key=True)
#     meal_name = db.Column(db.String(20), nullable=False)
#     category = db.Column(db.String(20),nullable=True)
#     quantity = db.Column(db.Integer,nullable=False)
#     tables = db.relationship('Tables', backref='meals') 

# class Tables(db.Model):
#     table_no = db.Column(db.Integer, primary_key=True)
#     no_of_people = db.Column(db.Integer, nullable=False)
#     time_booked = db.Column(db.DateTime, nullable=False)
#     meal_id = db.Column(db.Integer, db.ForeignKey('MEALS.meal_id'),nullable=False)



# class Mealform(FlaskForm):
#     name_ = StringField("Name of Dish")
#     category_=StringField("category")
#     quantity_= IntegerField("Quantity")
#     submit = SubmitField("Add Meal")

# class Tablesform(FlaskForm):
#     number_people = IntegerField("number please")
#     time_booked= DateField("time")
#     meal_id = IntegerField("meal_id")
#     submit = SubmitField("Book")


# @app.route('/')
# def index():
#     _todos= MEALS.query.all()  
#     return  render_template("index.html", meals=_todos)


# @app.route('/add',methods=['GET','POST'])
# def to_do1():
#     form = Mealform()
#     if form.validate_on_submit():
#         Meal_1= MEALS(meal_name= form.name_.data,category=form.category_.data,quantity=form.quantity_.data)
        
#         db.session.add(Meal_1)
#         db.session.commit()
#         return redirect(url_for("index"))
#     return render_template("add.html", form=form)


# @app.route('/addtable', methods=['GET','POST'])
# def add_table():
#     form = Tablesform()
#     if form.validate_on_submit():
#         Table_1= Tables(no_of_people= form.number_people.data,time_booked=form.time_booked.data, meal_id = form.meal_id.data)     
#         db.session.add(Table_1)
#         db.session.commit()
#         return redirect(url_for("index"))
#     return render_template("addtables.html", form=form)



# @app.route('/delete/<int:n>')
# def is_delete(n):
#     job_6 = MEALS.query.get(n)
#     db.session.delete(job_6)
#     db.session.commit()
#     #return 'deleted'
#     return  redirect (url_for("index"))

# @app.route('/updatemeal/<int:n>',methods = ['GET','POST'])
# def update(n):
#     form = Mealform()
#     meals_update= MEALS.query.get(n)
#     if form.validate_on_submit():
#         meals_update.meal_name = form.name_.data
#         meals_update.category = form.category_.data
#         meals_update.quantity = form.quantity_.data
#         db.session.commit()
#         return redirect(url_for("index"))
#     if request.method == "GET":
#         form.name_.data= meals_update.meal_name
#         form.category_.data= meals_update.category
#         form.quantity_.data = meals_update.quantity
#     return render_template("update.html",form=form)

# @app.route('/showtables')
# def show_tables():
#     all_tables= Tables.query.all()
#     return render_template("tables.html", tables=all_tables)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')