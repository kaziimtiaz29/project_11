from flask import Flask, config,url_for,redirect,render_template
from application import app, db
from application.models import MEALS,Tables
from flask_wtf import FlaskForm
from flask.globals import request
from application.forms import Mealform,Tablesform

@app.route('/')
def index():
    _todos= MEALS.query.all()  
    return  render_template("index.html", meals=_todos)


@app.route('/add',methods=['GET','POST'])
def to_add():
    form = Mealform()
    if form.validate_on_submit():
        Meal_1= MEALS(meal_name= form.name_.data,category=form.category_.data,quantity=form.quantity_.data)
        db.session.add(Meal_1)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html", form=form)


@app.route('/addtable', methods=['GET','POST'])
def add_table():
    form = Tablesform()
    if form.validate_on_submit():
        Table_1= Tables(no_of_people= form.number_people.data,time_booked=form.time_booked.data, meal_id = form.meal_id.data)     
        db.session.add(Table_1)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("addtables.html", form=form)



@app.route('/delete/<int:n>')
def is_delete(n):
    job_6 = MEALS.query.get(n)
    db.session.delete(job_6)
    db.session.commit()
    #return 'deleted'
    return  redirect (url_for("index"))
@app.route('/delete_table/<int:n>')
def delete_table(n):
    job_7 = Tables.query.get(n)
    db.session.delete(job_7)
    db.session.commit()
    #return 'deleted'
    return  redirect (url_for("index"))


@app.route('/updatemeal/<int:n>',methods = ['GET','POST'])
def update(n):
    form = Mealform()
    meals_update= MEALS.query.get(n)
    if form.validate_on_submit():
        meals_update.meal_name = form.name_.data
        meals_update.category = form.category_.data
        meals_update.quantity = form.quantity_.data
        db.session.commit()
        return redirect(url_for("index"))
    if request.method == "GET":
        form.name_.data= meals_update.meal_name
        form.category_.data= meals_update.category
        form.quantity_.data = meals_update.quantity
    return render_template("update.html",form=form)

@app.route('/showtables')
def show_tables():
    all_tables= Tables.query.all()
    return render_template("tables.html", tables=all_tables)