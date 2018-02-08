import webbrowser
import urllib
class Movie():
    """The documentation"""
    """init function to intialize a space for a movie that takes 5 paramters """
    """1)The movie it self with the self paramter
       2)The movie's name
       3)The movie's story Line
       4)The movie's poster
       5)The movie's trailer"""
    def __init__(self, movie_name, movie_story, movie_poster, movie_trailer):
        self.title = movie_name
        self.story =  movie_story
        self.poster_image_url  = movie_poster
        self.trailer_youtube_url = movie_trailer
        
    """ Function to open the trailer of a movie"""
    def show_trailer(self):
        webbrowser.open(self.trailer)
    """ Function to open image (poster) of a movie"""

    def show_poster(self):
        webbrowser.open(self.poster)
       
        
