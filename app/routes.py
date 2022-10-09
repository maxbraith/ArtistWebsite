from flask import render_template, flash, redirect
from app import app, db
from app.forms import artistForm
from app.models import Artist, Event, Venue, ArtistToEvent


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Ithaca Music')


@app.route('/Artists')
def Artists():
    a = Artist.query.all()
    return render_template('artists.HTML.html', title='Artists', artists=a)


@app.route("/NewArtists", methods=['GET', 'POST'])
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

    e1 = Event(name='e1', date='August 4', venue_id=1)
    e2 = Event(name='e2', date='January 3', venue_id=3)
    e3 = Event(name='e3', date='February 9', venue_id=3)
    e4 = Event(name='e4', date='March 27', venue_id=2)
    e5 = Event(name='e5', date='November 12', venue_id=1)
    e6 = Event(name='e6', date='October 5', venue_id=2)
    e7 = Event(name='e7', date='July 30', venue_id=3)
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







