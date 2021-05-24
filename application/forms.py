from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import DateField, IntegerField


class Mealform(FlaskForm):
    name_ = StringField("Name of Dish")
    category_=StringField("category")
    quantity_= IntegerField("Quantity")
    submit = SubmitField("Add Meal")

class Tablesform(FlaskForm):
    number_people = IntegerField("number please")
    time_booked= DateField("YYYY-MM-DD")
    meal_id = IntegerField("meal_id")
    submit = SubmitField("Book")
