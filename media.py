import webbrowser

#Movie Template Class
class Movie():
    """This is the file media.py it's the Movie class"""
    #Ratings Constant
    VALID_RATINGS = ["G", "PG", "PG-13","R"]

    #constructor
    def __init__(self, title, storyline, img, trailer):
        self.title               = title
        self.storyline           = storyline
        self.poster_image_url    = img
        self.trailer_youtube_url = trailer

    #opens up movie trailer on youtube
    def show_trailer(self):
        print("The show_trailer method is called")
        webbrowser.open(self.trailer_url)
