from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import artistForm, loginForm, RegistrationForm, eventForm, venueForm
from app.models import Artist, Event, Venue, ArtistToEvent, User
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Ithaca Music')


@app.route('/Artists')
def Artists():
    a = Artist.query.all()
    return render_template('artists.HTML.html', title='Artists', artists=a)


@app.route("/NewArtists", methods=['GET', 'POST'])
@login_required
def NewArtists():
    form = artistForm()
    if form.validate_on_submit():
        flash('Artist submission requested: {}'.format(
            form.artistName.data))
        newArtist = Artist(name=form.artistName.data, hometown=form.hometown.data)
        db.session.add(newArtist)
        db.session.commit()
        return render_template('artistInfo.html', title='New Artists', form=form)
    return render_template('NewArtists.html', title='New Artists', form=form)


@app.route('/NewEvents', methods=['GET', 'POST'])
@login_required
def NewEvents():
    form = eventForm()
    form.venue.choices = [(v.id, v.name) for v in Venue.query.all()]
    form.a2e.choices = [(a.id, a.name) for a in Artist.query.all()]
    if form.validate_on_submit():
        flash('Event submission request: {}'.format(
            form.eventName.data))
        newEvent = Event(name=form.eventName.data, date=form.date.data, venue_id=form.venue.data)
        db.session.add(newEvent)
        db.session.commit()

        for id in form.a2e.data:
            ate = ArtistToEvent(artist_id=id, event_id=newEvent.id)
            db.session.add(ate)
            db.session.commit()
        return redirect("index")
    return render_template('newEvent.html', title='New Event', form=form)

@app.route('/NewVenues', methods=['GET', 'POST'])
@login_required
def NewVenues():
    form = venueForm()
    if form.validate_on_submit():
        flash('Venue submission request: {}'.format(
            form.venueName.data))
        newVenue = Venue(name=form.venueName.data, address=form.address.data)
        db.session.add(newVenue)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("newVenue.html", title='New Venue', form=form)






@app.route('/populate_db')
def populate_db():

    reset_db()


    a1 = Artist(name='a1', hometown='Ithaca')
    a2 = Artist(name='a2', hometown='Cortland')
    a3 = Artist(name='a3', hometown='Cortland')
    a4 = Artist(name='a4', hometown='Syracuse')
    a5 = Artist(name='a5', hometown='Ithaca')
    db.session.add_all([a1,a2,a3,a4,a5])
    db.session.commit()

    v1 = Venue(name='Ithaca Venue', address='Ithaca ST')
    v2 = Venue(name='Syracuse Venue', address='Syracuse DR')
    v3 = Venue(name='Cortland Venue', address='Cortland ST')
    db.session.add_all([v1,v2,v3])
    db.session.commit()

    dt = datetime(2022, 11, 1)
    dt2 = datetime(2022, 1, 3)
    dt3 = datetime(2022, 2, 9)
    dt4 = datetime(2022, 3, 27)
    dt5 = datetime(2022, 9, 12)
    dt6 = datetime(2022, 8, 5)
    dt7 = datetime(2022, 7, 30)
    e1 = Event(name='e1', date=dt, venue_id=1)
    e2 = Event(name='e2', date=dt2, venue_id=3)
    e3 = Event(name='e3', date=dt3, venue_id=3)
    e4 = Event(name='e4', date=dt4, venue_id=2)
    e5 = Event(name='e5', date=dt5, venue_id=1)
    e6 = Event(name='e6', date=dt6, venue_id=2)
    e7 = Event(name='e7', date=dt7, venue_id=3)
    db.session.add_all([e1,e2,e3,e4,e5,e6,e7])
    db.session.commit()

    ate1 = ArtistToEvent(artist_id=1, event_id=3)
    ate2 = ArtistToEvent(artist_id=2, event_id=2)
    ate3 = ArtistToEvent(artist_id=3, event_id=4)
    ate4 = ArtistToEvent(artist_id=4, event_id=1)
    ate5 = ArtistToEvent(artist_id=5, event_id=7)
    ate6 = ArtistToEvent(artist_id=1, event_id=6)
    ate7 = ArtistToEvent(artist_id=4, event_id=5)
    ate8 = ArtistToEvent(artist_id=3, event_id=3)
    db.session.add_all([ate1,ate2,ate3,ate4,ate5,ate6,ate7,ate8])
    db.session.commit()

    flash("Database has been populated")
    return render_template('base.html', title='Home')


@app.route('/reset_db')
def reset_db():
    flash("Resetting database: deleting old data and repopulating with dummy data")
    # clear all data from all tables
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()

@app.route('/artist/<name>')
def artist(name):
    a = Artist.query.filter(Artist.name==name).first_or_404()

    return render_template('GunPoets.html', title=a.name, artist=a)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("User registered.")
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)








