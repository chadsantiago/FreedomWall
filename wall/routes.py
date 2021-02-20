from wall import app
from flask import Flask, render_template, url_for, redirect, request
from wall.database import db
from wall.models import Stories
from wall.forms import StoryForm
import datetime
import uuid



@app.route('/', methods=['POST', 'GET'])
def home():

    form = StoryForm(request.form)
    ct = datetime.datetime.utcnow()+datetime.timedelta(hours=8)
    current_time = ct.strftime("%b %d, %Y")

    if request.method == 'POST' and form.validate():

        x = datetime.datetime.utcnow()+datetime.timedelta(hours=8)
        posted = x.strftime("%b %d, %Y | %I:%M:%p")
        current = x.strftime("%b %d, %Y")

        story = Stories(public_id=str(uuid.uuid4()), content=form.content.data, date_posted=posted, current_date=current)

        db.session.add(story) # pushing data into database
        db.session.commit() # commit it to database
        return redirect('/') # redirect back to index page

    else:
        posts = Stories.query.filter(Stories.current_date == current_time).all() # Return all data from database sorting from date
        return render_template('index.html', posts=posts, form=form) # pass the data into the html page
      
    return render_template('index.html')


# Deleting data
@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    story_to_delete = Stories.query.get_or_404(id) # get data by id

    try:
        db.session.delete(story_to_delete) # delete the data
        db.session.commit() # commit to the database
        return redirect('/') # redirect back to index page

    except:
        return 'There was an error deleting your post'

@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 404

@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500