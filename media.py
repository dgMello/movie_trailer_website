import webbrowser


# This class takes in several inputs regarding movie information and
# creates movie objects.
# That output movies with that information.


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_director):
        # This is the main method of the Movie class.  It initilies with 6
        # inputs and creates 5 instance variables.
        # Inputs are: self, movie_title, movie_storyline, poster_image,
        # trailer_youtube,movie_director
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = movie_director

    def show_trailer(self):
        # This method of the Movie class input is the instance variable
        # trailer_youtube_url and outputs an web browser.
        webbrowser.open(self.trailer_youtube_url)
