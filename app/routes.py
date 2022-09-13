from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


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
        flash('Artist submission requested {}'.format(
            form.artistName.data))
        return render_template('artistInfo.html', title='New Artists', form=form)
    return render_template('NewArtists.html', title='New Artists', form=form)


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

    return render_template('GunPoets.html', title='Gunpoets', posts=posts, events=events)


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
