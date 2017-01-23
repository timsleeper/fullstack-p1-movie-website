import webbrowser

class Movie():
    '''
    The Movie class contains the movie objects that are going to be displayed.

    Each movie contains:
        Movie.title = The movie title
        Movie.storyline = Short plot description of the movie
        Movie.poster = URL containing a movie poster image
        Movie.trailer_youtube_url = URL with youtube trailer
    '''
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)