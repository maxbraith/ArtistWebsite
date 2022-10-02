from flask import render_template, flash, redirect
from app import app, db
from app.forms import LoginForm
from app.models import Artist, Event, Venue, ArtistToEvent


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },

    ]
    return render_template('index.html', title='Ithaca Music', user=user, posts=posts)


@app.route('/Artists')
def Artists():
    user = {'username': 'Welcome'}
    posts = [
        {
            'body': "John Brown's Body"
        },
        {
            'body': 'Gunpoets'
        },
        {
            'body': 'Donna The Buffalo'
        },
        {
            'body': 'The Blind Spots'
        }
    ]
    return render_template('artists.HTML.html', title='Artists', user=user, posts=posts)


@app.route("/NewArtists", methods=['GET', 'POST'])
def NewArtists():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Artist submission requested: {}'.format(
            form.artistName.data))
        return render_template('artistInfo.html', title='New Artists', form=form)
    return render_template('NewArtists.html', title='New Artists', form=form)


@app.route("/JohnBrownsBody")
def JohnBrownsBody():
    user = {'username': 'JohnBrownsBody'}
    posts = {
            'body': 'Page Under Construction'
        }
    return render_template('GunPoets.html', title='John Browns Body', user=user, posts=posts)


@app.route("/Gunpoets")
def Gunpoets():
    user = {'username': 'Gunpoets'}
    posts = {
        'body': "Voice as a weapon, words as bullets, spreading the universal message of peace, love, and justice "
                "through music. Sure, there's a cynical cultural tendency to make certain assumptions when you "
                "hear the word \"gun\" associated with rap music, but this seven-member live hip-hop band from "
                "Ithaca, NY, runs contrary to that image with their positive message and uplifting performances. "
    }

    events = {
        'event1': "The Commons on Thursday 9/6",

        'event2': "Campus Center on Friday 9/7"
    }

    return render_template('GunPoets.html', title='Gunpoets', posts=posts, user=user, events=events)


@app.route("/DonnaTheBuffalo")
def DonnaTheBuffalo():
    user = {'username': 'DonnaTheBuffalo'}
    posts = {
            'body': 'Page Under Construction'
        }

    return render_template('Gunpoets.html', title='DonnaTheBuffalo', user=user, posts=posts)


@app.route("/TheBlindSpots")
def TheBlindSpots():
    user = {'username': 'TheBlindSpots'}
    posts = {
            'body': 'Page Under Construction'
        }

    return render_template('Gunpoets.html', title='TheBlindSpots', user=user, posts=posts)

@app.route('/populate_db')
def populate_db():

    reset_db()

    a1 = Artist(name='a1', hometown='Ithaca')
    a2 = Artist(name='a2', hometown='Cortland')
    a3 = Artist(name='a3', hometown='Cortland')
    a4 = Artist(name='a4', hometwon='Syracuse')
    a5 = Artist(name='a5', hometown='Ithaca')
    db.session.add_all([a1,a2,a3,a4,a5])
    db.session.commit()

    v1 = Venue(name='Ithaca Venue', address='Ithaca ST')
    v2 = Venue(name='Syracuse Venue', address='Syracuse DR')
    v3 = Venue(name='Cortland Venue', address='Cortland ST')
    db.session.add_all([v1,v2,v3])
    db.session.commit()

    e1 = Event(name='e1', date='August 4')
    e2 = Event(name='e2', date='January 3')
    e3 = Event(name='e3', date='February 9')
    e4 = Event(name='e4', date='March 27')
    e5 = Event(name='e5', date='November 12')
    e6 = Event(name='e6', date='October 5')
    e7 = Event(name='e7', date='July 30')
    db.session.add_all([e1,e2,e3,e4,e5,e6,e7])
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


