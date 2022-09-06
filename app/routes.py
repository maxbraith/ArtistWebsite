from flask import render_template
from app import app


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


@app.route("/NewArtists")
def NewArtists():
    user = {'username': 'Miguel'}
    posts = [
        {
            'body': 'Page Under Construction'
        }
    ]
    return render_template('NewArtists.html', title='New Artists', user=user, posts=posts)


@app.route("/JohnBrownsBody")
def JohnBrownsBody():
    user = {'username': 'Miguel'}
    posts = [
        {
            'body': 'Page Under Construction'
        }
    ]
    return render_template('JohnBrownsBody.html', title='John Browns Body', user=user, posts=posts)


@app.route("/Gunpoets")
def Gunpoets():
    user = {'username': 'Miguel'}
    posts = [
        {
            'body': 'Page Under Construction'
        }
    ]
    return render_template('GunPoets.html', title='Gunpoets', user=user, posts=posts)


@app.route("/DonnaTheBuffalo")
def DonnaTheBuffalo():
    user = {'username': 'Miguel'}
    posts = [
        {
            'body': 'Page Under Construction'
        }
    ]
    return render_template('DonnaTheBuffalo.html', title='DonnaTheBuffalo', user=user, posts=posts)


@app.route("/TheBlindSpots")
def TheBlindSpots():
    user = {'username': 'Max'}
    posts = [
        {
            'body': 'Page Under Construction'
        }
    ]
    return render_template('TheBlindSpots.html', title='TheBlindSpots', user=user, posts=posts)