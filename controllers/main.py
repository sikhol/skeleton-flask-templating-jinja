
import os
import sys
from flask import jsonify,render_template,send_file, request,flash, redirect ,url_for,session,send_file, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

from sqlalchemy.orm import sessionmaker
import argparse
from datatables import ColumnDT, DataTables
import time
import datetime
from datetime import datetime
from helpers.forms import RegisterForm, LoginForm, addBarangForm
import json
from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextAreaField, IntegerField
from wtforms.widgets import TextArea
from sqlalchemy.exc import InvalidRequestError
from flask_login import login_required, current_user,logout_user

from config.settings import db

from model.Models import Users, Users_Barang, Users_Barang


index = Blueprint('index', __name__)


@index.route('/create',methods=['GET','POST'])
@login_required
def create():
    try:
        #your code
        return render_template('add-file.html')
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()


@index.route('/update/<int:id>/', methods = ['GET', 'POST'])
@login_required
def update(id):
    try:
        #your code
        return render_template('edit.html')
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()

@index.route('/delete/<id>/', methods = ['GET', 'POST'])
@login_required
def delete(id):
    try:
        #your code
        return redirect(url_for('index.result'))

    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()

@index.route('/', methods=['GET', 'POST'])
def login():
    try:
        #your code
        return render_template('login.html', form=form)

    except InvalidRequestError:
        db.session.rollback()
        raise
    finally:
        db.session.close()

@index.route('/register/', methods = ['GET', 'POST'])
def register():
    try:
        #your code
        return render_template('register.html', form = form)
    except :
        db.session.rollback()
        raise
    finally:
        db.session.close()

@index.route('/logout/')
@login_required
def logout():
    try:
        logout_user()
        return redirect(url_for('index.login'))
    except :
        db.session.rollback()
        raise
    finally:
        db.session.close()





