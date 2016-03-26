
## define the Movie Class
class Movie():
	## now need 4 parameters to make an instance
	def __init__(self, movie_title,
                     movie_trailer_youtube_url,
                     movie_poster_image_url,
                     movie_description):
		
                self.title = movie_title
                self.trailer_youtube_url = movie_trailer_youtube_url
                self.poster_image_url = movie_poster_image_url
                self.description = movie_description
                ##  new feature
