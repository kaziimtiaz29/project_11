from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import MEALS, Tables   
#from application import routes

class TestBase(TestCase):
        def create_app(self):
                app.config.update(SQLALCHEMY_DATABASE_URI= 'sqlite:///',
                        SECRET_KEY='TEST_SECRET_KEY',
                        DEBUG=True,
                        WTF_CSRF_ENABLED=False
                        )
                return app
        def setUp(self):
                """
                Will be called before every test
                """
                # Create table
                db.create_all()

                # Create test registree
                sample1 = MEALS(meal_name="burger,fries",category="fast food",quantity = 3)
                sample2 = Tables (no_of_people=2,time_booked=1970-10-21,meal_id=1)
                # save users to database
                db.session.add(sample1)
                db.session.commit()

        def tearDown(self):
                """
                Will be called after every test
                """

                db.session.remove()
                db.drop_all()

class TestViews(TestBase):

    def test_addmeal_get(self):    
        response = self.client.get(url_for('to_add'))
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b'burger,fries', response.data)
    def test_addtable_get(self):
        response = self.client.get(url_for('add_table'))
        self.assertEqual(response.status_code, 200)
    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
    def test_table_get(self):
        response = self.client.get(url_for('show_tables'))
        self.assertEqual(response.status_code, 200)
    def test_update_get(self):
        response = self.client.get(url_for('update',n=1))
        self.assertEqual(response.status_code, 200)


class TestAdd(TestBase):
  def test_add_post(self):
        response = self.client.post(
            url_for('to_add'),
             data = dict(name_="MrMan",category_="asd",quantity_=2),
        follow_redirects=True
        )
        
        #print(response.data)
        self.assertIn(b'MrMan',response.data)


  def test_update_post(self):
        response = self.client.post(
            url_for('update',n=1),
             data = dict(name_="mark",category_="asd",quantity_=2),
        follow_redirects=True
        )
        
        #print(response.data)
        self.assertIn(b'mark',response.data)



  def test_add_table_post(self):
        response = self.client.post(
            url_for('add_table'),
             data = dict(number_people=5,time_booked=1999-11-21,meal_id=1),
        follow_redirects=True
        )
        
        #print(response.data)
        self.assertIn(b'5' ,response.data)
  def test_add_table1_post(self):
        response = self.client.post(
            url_for('add_table'),
             data = dict(number_people=5,time_booked=1999-11-21,meal_id=1),
        follow_redirects=True
        )
        
        #print(response.data)
        self.assertIn(b"5" ,response.data)

