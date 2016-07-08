import webbrowser

class Movie():
    def __init__(self, movie_title, storyline, poster, trailer_youtube):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
