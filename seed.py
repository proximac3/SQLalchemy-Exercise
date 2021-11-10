"""Seed files to make sample data"""

from models import Person, db, BlogPost, Tags, PostTags
from app import app

db.drop_all()
db.create_all()

Person.query.delete()

#perosn
sophon = Person(first_name='sophon', last_name='trisolarian', image_url='https://i.pinimg.com/originals/6b/bf/3e/6bbf3e6117619797781f4a827597af95.jpg')
luo = Person(first_name='luo', last_name='ji', image_url='https://sfoil.files.wordpress.com/2018/04/luo-ji1.jpg?resize=629%2C896')

#post
cats = BlogPost(title='cats', content='cats are cute and adorable', user=1)
dogs = BlogPost(title='dogs', content='dogs are loyal', user=1)
penguins = BlogPost(title='penguin', content='penguins are the best', user=2)

#Tags
cat_tag = Tags(name='cats')
dog_tag = Tags(name='dogs')

#post Tgas
dog_post = PostTags(post_title='dogs', tag_name='dogs')
cat_post = PostTags(post_title='cats', tag_name='cats')

#adding Person      
db.session.add(sophon)
db.session.add(luo)
db.session.commit()

#addiong post 
db.session.add(cats)
db.session.add(dogs)
db.session.add(penguins)
db.session.commit()

#adding tags
db.session.add(cat_tag)
db.session.add(dog_tag)
db.session.commit()

#adding post tags
db.session.add(dog_post)
db.session.add(cat_post)
db.session.commit()

