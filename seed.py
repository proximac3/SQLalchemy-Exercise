"""Seed files to make sample data"""

from models import Person, db, BlogPost
from app import app

db.drop_all()
db.create_all()

Person.query.delete()

sophon = Person(first_name='sophon', last_name='trisolarian', image_url='https://i.pinimg.com/originals/6b/bf/3e/6bbf3e6117619797781f4a827597af95.jpg')
luo = Person(first_name='luo', last_name='ji', image_url='https://sfoil.files.wordpress.com/2018/04/luo-ji1.jpg?resize=629%2C896')

cats = BlogPost(title='cats', content='cats are cute and adorable', user=1)
dogs = BlogPost(title='dogs', content='dogs are loyal', user=1)
penguins = BlogPost(title='penguin', content='penguins are the best', user=2)

db.session.add(sophon)
db.session.add(luo)
db.session.commit()


db.session.add(cats)
db.session.add(dogs)
db.session.add(penguins)
db.session.commit()

