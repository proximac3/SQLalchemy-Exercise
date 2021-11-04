from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blog_db'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True
app.debug = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserTestCase(TestCase):
    """ Test View for user"""

    def setUp(self):
        """ Create a sample new user"""
        User.query.delete()

        user = User(first_name='V', last_name='Anonymous', image_url='https://images.unsplash.com/photo-1582266255765-fa5cf1a1d501?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1170&q=80')

        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        """ Clear up any foiled transactions"""
        db.session.rollback()


    def test_testUserList(self):
        with app.test_client() as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('Anonymous', html)

    def test_userDetails(self):
        with app.test_client() as client:
            response = client.get('/details/1')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('V', html)