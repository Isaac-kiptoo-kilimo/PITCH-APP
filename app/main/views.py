from flask import render_template
from . import main
from .. import db, login_manager
from ..models import User, Pitch,Comment, Category
from flask_login import login_user, current_user, logout_user, login_required

def make_pitches(pitches):

  new_pitches = []
  for pitch in pitches:
    user = User.query.filter_by(id=pitch.user_id).first()
    category = Category.query.filter_by(id=pitch.category_id).first()
    comments = Comment.query.filter_by(pitch_id=pitch.id).all()
    new_pitches.append({
      'id': pitch.id,
      'title': pitch.title,
      'content': pitch.content,
      'category': category,
      'user': user,
      'upvotes': pitch.upvotes,
      'downvotes': pitch.downvotes,
      'comments': len(comments)
    })
  return new_pitches

@main.route('/')
def index():
  categories = Category.query.order_by(Category.id.asc()).all()
  pitches = Pitch.query.order_by(Pitch.id.desc()).all()
  new_pitches = make_pitches(pitches)
  return render_template('pages/index.html',
  categories=categories, pitches=new_pitches)

@main.route('/pitches/categories/<string:category_id>')
def category_view(category_id):
  return render_template('pages/category.html')


@main.route('/pitches/view/<string:pitch_id>/')
def pitch_view(pitch_id):
  
  return render_template('pages/pitchview.html')


@main.route('/auth/login', methods=['GET','POST'])
def login():
  # form = LoginForm()
  # if form.validate_on_submit():
  #   user = User.query.filter_by(email=form.email.data).first()
  #   if user and bcrypt.check_password_hash(user.password, form.password.data):
  #     login_user(user, remember=form.remember.data)
  #     next_page = request.args.get('next')
  #     return redirect(next_page or url_for('main.index'))
  #   else:
  #     flash('Login Unsuccessful. Please check email and password', 'danger')
  return render_template('pages/auth/login.html', title='Login')


@main.route('/auth/signup', methods=['GET','POST'])
def signup():
  # form = SignupForm()
  # if form.validate_on_submit():
  #   hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
  #   user = User(username=form.username.data,
  #               email=form.email.data,
  #               password=hashed_password)
  #   db.session.add(user)
  #   db.session.commit()
  #   flash('Your account has been created! You are now able to log in', 'success')
  #   return redirect(url_for('main.login'))
  return render_template('pages/auth/signup.html', title='Sign Up')
