from application.models import MEALS
from flask.helpers import url_for
from selenium import webdriver
from flask_testing import LiveServerTestCase
from application import app, db
from application.models import MEALS,Tables
from urllib.request import urlopen
class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db" # change to a test sqlite database
        app.config['LIVESERVER_PORT'] =5050
        app.config['SECRET_KEY'] = "1234"
        app.config['DEBUG']= True
        app.config['TESTING']= True
        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless') # must be headless

        self.driver = webdriver.Chrome(options=chrome_options) 

        db.create_all() # create schema before we try to get the page
        self.driver.get(f'http://localhost:5050/')

    def tearDown(self):
        self.driver.quit()
        db.drop_all()
    def test_server_is_up_to_and_running(self):
        response=urlopen("http://localhost:5050/")
        self.assertEqual(response.code, 200)
    
class Testviews(TestBase):
        def test_navigation(self):
           self.driver.find_element_by_xpath ("/html/body/a[2]").click()
           self.assertIn(url_for("to_add"), self.driver.current_url)
        
        # def test_adding(self):
        #     self.driver.find_element_by_xpath ("/html/body/a[2]").click()
        #     self.driver.find_element_by_xpath('//*[@id="name_"]').send_keys("burgers")
        #     self.driver.find_element_by_xpath('//*[@id="category_"]').send_keys("fastfood")
        #     self.driver.find_element_by_xpath('//*[@id="quantity_"]').send_keys("4")
        #     self.driver.find_element_by_xpath('//*[@id="submit_"]').click()
        #     meals= MEALS.query.first()
        #     self.assertEqual(meals.name_,"burgers")
            
