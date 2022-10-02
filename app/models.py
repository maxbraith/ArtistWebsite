from app import db


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    hometown = db.Column(db.String(120), index=True)
    artistToEvents = db.relationship('ArtistToEvent', backref='artist', lazy='dynamic')

    def __repr__(self):
        return '<Artist {}>'.format(self.name)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    date = db.Column(db.String(120), index=True)
    artistToEvents = db.relationship('ArtistToEvent', backref='event', lazy='dynamic')
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))

    def __repr__(self):
        return '<Event {}>'.format(self.name)


class ArtistToEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

    def __repr__(self):
        return '<AristToEvent {}>'.format(self.id)


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    address = db.Column(db.String(120), index=True)
    events = db.relationship('Event', backref='venue', lazy='dynamic')

    def __repr__(self):
        return '<Venue {}>'.format(self.name)
