import secrets # for picture saving
import os # for picture saving
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from app import app, db, bcrypt, mail
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message





# posts = [
#     {
#         'author':'Zubair',
#         'title':'Blog Post 1',
#         'content':'First post content',
#         'date_posted':'April 20 2023'
#     },
#     {
#         'author':'Hamza',
#         'title':'Blog Post 2',
#         'content':'Second post content',
#         'date_posted':'April 21 2023'
#     }
# ]

