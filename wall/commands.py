import click
from wall.database import db
from wall.models import Stories, Replies


# create database
def create_db():
    db.create_all()

def drop_db():
    db.drop_all()

def create_model():
    Replies.__table__.create(db.engine)

def drop_model():
    Replies.__table__.drop(db.engine)


def init_app(app):
    for command in [create_db, drop_db, create_model, drop_model]:
        app.cli.add_command(app.cli.command()(command))