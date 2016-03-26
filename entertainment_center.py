import media
import fresh_tomatoes

iron_man = media.Movie("Iron Man",
		       "https://www.youtube.com/watch?v=8hYlB38asDY",
		       "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG")

bat_man = media.Movie("Bat Man",
		      "https://www.youtube.com/watch?v=EXeTwQWrcwY",
		      "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg")
super_man = media.Movie("Super Man",
                        "https://www.youtube.com/watch?v=T6DJcgm3wNY",
                        "https://upload.wikimedia.org/wikipedia/en/8/85/ManofSteelFinalPoster.jpg")
movies = [iron_man, bat_man, super_man]
fresh_tomatoes.open_movies_page(movies)
