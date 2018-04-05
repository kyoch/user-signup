from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


def get_current_watchlist():
    # returns user's current watchlist--hard coded for now
    return [ "Star Wars", "Minions", "Freaky Friday", "My Favorite Martian" ]

# a form for crossing off watched movies
# (first we build a dropdown from the current watchlist items)
   # crossoff_options = ""
   # for movie in get_current_watchlist():
   #     crossoff_options += '<option value="{0}">{0}</option>'.format(movie)

    
    return render_template('edit.html',movie = movie)



@app.route("/crossoff", methods=['POST'])

def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']

    if crossed_off_movie not in get_current_watchlist():
        # the user tried to cross off a movie that isn't in their list,
        # so we redirect back to the front page and tell them what went wrong
        error = "'{0}' is not in your Watchlist, so you can't cross it off!".format(crossed_off_movie)

        # redirect to homepage, and include error as a query parameter in the URL
        return redirect("/?errorMsg=" + error)

    # if we didn't redirect by now, then all is well
    
    return render_template('crossoff.html',crossed_off_movie = crossed_off_movie)


movies = [ ] # create an empty movie list

@app.route("/add", methods=['POST', 'GET'])
def add_movie():

    if request.method == 'POST':
        new_movie = request.form['new-movie']
        movies.append(new_movie)
    
    # TODO 
    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site

    # TODO 
    # if the user typed nothing at all, redirect and tell them the error

    if new_movie.strip() == "":
        error = "Please specify the name of the movie you want to add."
        return redirect("/?error=" + error)

    # TODO 
    # if the user wants to add a terrible movie, rviedirect and tell them not to add it b/c it sucks
    if new_movie in terrible_movies:
        error = "Trust me, you don't want to add '{0}' to your watchlist.".format(new_movie)
        return redirect("/?error=" + error)
        
    return render_template('add-confirmation.html', new_movie=new_movie)

    
    
 

@app.route("/")
def index():

    # if we have an error, make a <p> to display it
    error_m = request.args.get("error")
    #if error:
     #   error_esc = cgi.escape(error, quote=True)
    #    error_element = '<p class="error">' + error_esc + '</p>'
    #else:
    #    error_element = ''

  
    # combine all the pieces to build the content of our response
    return render_template('edit.html',watchlist = get_current_watchlist(), error = error_m)


app.run()
