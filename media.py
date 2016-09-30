import webbrowser

class Movie():
    """ Stores information pertaining to movies. """

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url, year, rating):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.year = year
        self.rating = rating
        self.web_display = "{} ({})".format(title, year)

    def show_trailer(self):
        webbrowser.open(self.trailer)

    def check_rating(self):
        if self.rating in Movie.VALID_RATINGS:
            return "This film is rated {}".format(self.rating)
        else:
            return "Warning: this film does not have a valid rating."
        

