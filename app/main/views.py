from flask import render_template,request,redirect,url_for, flash
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
  category = Category.query.filter_by(id=category_id).first()
  categories = Category.query.order_by(Category.id.asc()).all()
  print("category", category)
  if category:
    pitches = Pitch.query.filter_by(category_id=category.id).all()
    new_pitches = make_pitches(pitches)
    return render_template('pages/category.html',categories=categories, category=category, pitches=new_pitches)
  else:
    flash('Category not found', 'warning')
    return redirect(url_for('main.index'))

@main.route('/pitches/view/<string:pitch_id>/')
@login_required
def pitch_view(pitch_id):
  pitch = Pitch.query.filter_by(id=pitch_id).first()
  if pitch:
    comments = Comment.query.filter_by(pitch_id=pitch.id).all()
    new_comments = []
    for comment in comments:
      user = User.query.filter_by(id=comment.user_id).first()
      new_comments.append({
        'id': comment.id,
        'content': comment.content,
        'user': user,
        'created_at': comment.created_at
      })
    user = User.query.filter_by(id=pitch.user_id).first()
  
    return render_template('pages/pitchview.html',pitch=pitch, comments=new_comments, user=user)
  else:
    flash('Pitch not found', 'warning')
    return redirect(url_for('main.index'))

@main.route('/pitches/view/<string:pitch_id>/comments/add/', methods=['GET', 'POST'])
@login_required
def add_comment(pitch_id):
  pitch = Pitch.query.filter_by(id=pitch_id).first()
  if request.method == 'POST':
    content = request.form['comment']
    if pitch:
      comment = Comment(pitch_id=pitch.id, user_id=current_user.id, content=content)
      db.session.add(comment)
      db.session.commit()
      flash('Comment added', 'success')
      return redirect(url_for('main.pitch_view', pitch_id=pitch.id))
    else:
      flash('Pitch not found', 'warning')
      return redirect(url_for('main.index'))
  return redirect(url_for('main.pitch_view', pitch_id=pitch.id))

@main.route('/pitches/view/<string:pitch_id>/upvote/', methods=['GET', 'POST'])
@login_required
def upvote_pitch(pitch_id):
  pitch = Pitch.query.filter_by(id=pitch_id).first()
  if pitch:
    pitch.upvotes += 1
    db.session.commit()
    flash('Pitch upvoted', 'success')
    return redirect(request.referrer)
  else:
    flash('Pitch not found', 'warning')
    return redirect(url_for('main.index'))

    
@main.route('/pitches/view/<string:pitch_id>/downvote/', methods=['GET', 'POST'])
@login_required
def downvote_pitch(pitch_id):
  pitch = Pitch.query.filter_by(id=pitch_id).first()
  if pitch:
    pitch.downvotes -= 1
    db.session.commit()
    flash('Pitch downvoted', 'success')
    return redirect(request.referrer)
  else:
    flash('Pitch not found', 'warning')
    return redirect(url_for('main.index'))

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
