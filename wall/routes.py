from wall import app
from flask import Flask, render_template, url_for, redirect, request
from wall.database import db
from wall.models import Stories, Replies
from wall.forms import StoryForm, ReplyForm
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
        # posts = Stories.query.filter(Stories.current_date == current_time).order_by(Stories.date_created.asc()).all() # Return all data from database sorting from date
        posts = Stories.query.order_by(Stories.date_created.asc()).all() # Return all data from database sorting from date
        return render_template('index.html', posts=posts, form=form) # pass the data into the html page
      
    return render_template('index.html')


@app.route('/read/<parentid>', methods=['POST', 'GET'])
def read(parentid):

    parentid = parentid
    form = ReplyForm(request.form)
    ct = datetime.datetime.utcnow()+datetime.timedelta(hours=8)
    current_time = ct.strftime("%b %d, %Y")

    if request.method == 'POST' and form.validate():

        x = datetime.datetime.utcnow()+datetime.timedelta(hours=8)
        posted = x.strftime("%b %d, %Y | %I:%M:%p")
        current = x.strftime("%b %d, %Y")

        parent = Stories.query.filter(Stories.public_id == parentid).order_by(Stories.date_created.asc()).first()

        reply = parent.reply_count + 1

        parent.reply_count = reply

        reply = Replies(public_id=str(uuid.uuid4()), parent_id=parentid, content=form.content.data, date_posted=posted, current_date=current)

        db.session.add(reply) # pushing data into database
        db.session.commit() # commit it to database
        return redirect('/read/' + parentid) # redirect back the page

    else:
        parent = Stories.query.filter(Stories.public_id == parentid).order_by(Stories.date_created.asc()).first() # Return all data from database sorting from date
        replies = Replies.query.filter(Replies.parent_id == parentid).order_by(Replies.date_created.asc()).all() # Return all data from database sorting from date
        return render_template('reply.html', replies=replies, parent=parent, form=form, parentid=parentid) # pass the data into the html page
      
    return render_template('reply.html')



# Deleting data
@app.route('/delete/<string:public_id>', methods=['POST', 'GET'])
def delete(public_id):
    pid = public_id

    try:
        story_to_delete = Stories.query.filter_by(public_id=pid).first() # get data by id

        db.session.delete(story_to_delete) # delete the data
        db.session.commit() # commit to the database
        return redirect('/') # redirect back to index page

    except:
        reply_to_delete = Replies.query.filter_by(public_id=pid).first() # get data by id
        replies = Replies.query.filter_by(public_id=pid).first()

        parent = Stories.query.filter(Stories.public_id == replies.parent_id).first()

        reply = parent.reply_count - 1

        parent.reply_count = reply

        db.session.delete(reply_to_delete) # delete the data
        db.session.commit() # commit to the database
        return redirect('/read/' + replies.parent_id) # redirect back to index page
        




@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 404

@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500