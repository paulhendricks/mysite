from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)


# NOTE: IDs are used by the Disqus plug-in to distinguish betwixt pages.
# NOTE: When updating with a new blog post:
# 1. Create a new host method for it. Iterate the id.
# 2. Update the Blog link in frame.html to point to the most recent post.
# 3. Update the previously most recent Blog post to point to the new post as the new most recent one.
# These URLs are generated within Jinja2 using eg. href='{{request.url_root}}2015/10/31/this-website.html'.

# TODO: Automagically host blog posts using a list of posts and an iterative generator (url_for).
# TODO: Automagically host summaries of recent blog posts on the About page (using the same technique).

@app.route('/')
def home():
    return render_template('about.html')


@app.route('/2015/11/06/an-exercise-in-probability.html')
def first_post():
    return render_template('an_exercise_in_probability.html', id=1)


@app.route('/2015/10/31/this-website.html')
def second_post():
    return render_template('this_website.html', id=2)


@app.route('/2015/12/12/openness-versus-quality.html')
def third_post():
    return render_template('openness_versus_quality.html', id=3)


@app.route('/2015/12/26/watson.html')
def fourth_post():
    return render_template('watson.html', id=4)


@app.route('/2016/01/17/signpost-views.html')
def fifth_post():
    return render_template('signpost_views.html', id=5)


@app.route('/2016/01/17/signpost_views.html')
def redir():
    return redirect('/2016/01/17/signpost-views.html')

if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
