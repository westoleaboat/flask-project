# # from datetime import datetime
# import os
# from flask import Flask, render_template, session, redirect, url_for, flash
# from flask_bootstrap import Bootstrap
# from flask_moment import Moment
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'hard string'
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#     'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# bootstrap = Bootstrap(app)
# moment = Moment(app)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Staring(64), unique=True)
#     users = db.relationship('User', backref='role', lazy='dynamic')

#     def __repr__(self):
#         return '<Role %r>' % self.name


# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, index=True)
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

#     def __repr__(self):
#         return '<User %r>' % self.username

# class NameForm(FlaskForm):
#     name = StringField('What is your name?', validators=[DataRequired()])
#     submit = SubmitField('Submit')

# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, User=User, Role=Role)

# @app.errorhandler(404) 
# def page_not_found(e):
#     return render_template('404.html'), 404


# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     '''
#     The name variable is now placed in the user session
#     as session['name'] so that it is remembered beyond the request.
#     '''
#     form = NameForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             user = User(username=form.name.data)
#             db.session.add(user)
#             db.session.commit()
#             session['known'] = False
#         else:
#             session['known'] = True
#         session['name'] = form.name.data
#         return redirect(url_for('index'))
#     return render_template('index.html', form=form, name=session.get('name'),
#                            known=session.get('known', False))


import os
import click
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

