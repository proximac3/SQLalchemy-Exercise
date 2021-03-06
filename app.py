"""Blogly application."""

from flask import Flask, request, render_template, flash, redirect, session
from models import db, connect_db, Person, BlogPost, Tags, PostTags

from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blog_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'trisolarian879'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

db.create_all()


@app.route('/')
def users():
    """Show list of users"""
    persons = Person.query.all()
    
    return render_template('users.html', people=persons)


@app.route('/new')
def new_user_form():
    """New User FORM"""
    return render_template('new_user.html')

@app.route('/create', methods=['POST'])
def createUser():
    """Create new User """
    first_name = request.form['first']
    last_name = request.form['last']
    url = request.form['url']

    person = User(first_name=first_name, last_name=last_name, image_url=url)
    db.session.add(person)
    db.session.commit()

    return redirect(f"/details/{person.id}")


@app.route('/details/<int:person_id>')
def details(person_id):
    """Show details about a user"""
    person = Person.query.get_or_404(person_id)
    return render_template('details.html', new_user=person)

@app.route('/edit/<int:person_id>')
def edit_user(person_id):
    """Edit user details"""
    person = Person.query.get(person_id)
    return render_template('edit.html', person=person)


@app.route('/updated/<int:person_id>', methods=['POST'])
def updated(person_id):
    """Update user info"""
    first_name = request.form['first']
    last_name = request.form['last']
    image = request.form['url']

    person = User.query.get(person_id)

    person.first_name = first_name
    person.last_name = last_name
    person.image_url = image

    db.session.add(person)
    db.session.commit()

    return redirect(f'/details/{person.id}')


@app.route('/delete/<int:person_id>')
def delete(person_id):
    """Delete User Confirmation"""
    person = User.query.get(person_id)
    return render_template('delete.html', personId=person)


@app.route('/deleted/<int:person_id>', methods=['POST'])
def deleted(person_id):
    """Delete User"""
    person = User.query.get(person_id)
    db.session.delete(person)
    db.session.commit()
    return redirect('/')

@app.route('/createPost/<int:user_id>')
def createPost(user_id):
    """Create a new post form"""

    user = Person.query.get(user_id)
    return render_template('post.html', user=user)

@app.route('/addPost/<int:user_id>', methods=['POST'])
def addPost(user_id):
    """Add post"""
    title = request.form['title']
    content = request.form['content']
    user = int(user_id)

    newPost = BlogPost(title=title, content=content, user=user)
    db.session.add(newPost)
    db.session.commit()

    return redirect(f'/details/{user_id}')

@app.route('/post/details/<post_title>')
def postDetails(post_title):

    post = BlogPost.query.filter(BlogPost.title == post_title).first()

    return render_template('post_details.html', post=post)


@app.route('/tags')
def tag_lisyt():
    """ Show List of Tags"""
    tags = Tags.query.all()
    return render_template('tag_list.html', tags=tags)


@app.route('/tagform')
def tag_tag():
    """Load form to create new tag"""
    return render_template('tag_form.html')

@app.route('/createTag', methods=['POST'])
def create_tag():
    """Create  new Tag"""
    tag = request.form['tag']
    new_tag = Tags(name=f'{tag}')
    db.session.add(new_tag)
    db.session.commit()

    return redirect('/tags')

@app.route('/tag/details/<tag_id>')
def tag_details(tag_id):
    """ Show Tag Details """

    tag = Tags.query.get(tag_id)
    user = tag.tag_rel
    return render_template('tag_details.html', tag=tag)

@app.route('/tag/edit/<tag_id>')
def edit_tag(tag_id):
    """Loads edit template fortag"""
    tag = Tags.query.get(tag_id)
    return render_template('tag_edit.html', tag=tag)

@app.route('/change/<tag_id>', methods=['POST'])
def tag_change(tag_id):
    """Confirm tag change and redirect back to tags"""
    tag_name = request.form['tag']
    tag = Tags.query.get(tag_id)
    tag.name = tag_name

    db.session.add(tag)
    db.session.commit()
    return redirect('/tags')

@app.route('/delete/tag/<tag_id>')
def delete_tag(tag_id):
    """DELETE TAG"""
    tag = Tags.query.get(tag_id)

    db.session.delete(tag)
    db.session.commit()

    return redirect('/tags')

@app.route('/post')
def post_list():
    """SHOW LIST OF POST"""
    posts = BlogPost.query.all()
    return render_template('posts.html', posts=posts)