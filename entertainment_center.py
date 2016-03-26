import media
import fresh_tomatoes
"""
create instances of media.Movie

"""
iron_man = media.Movie("Iron Man",
		       "https://www.youtube.com/"
                       "watch?v=8hYlB38asDY",
		       "https://upload.wikimedia.org/"
                       "wikipedia/en/7/70/Ironmanposter.JPG",
                       "A billionaire industrialist and genius"
                       " inventor, Tony Stark (Robert Downey Jr.), "
                       "is conducting weapons tests overseas, but "
                       "terrorists kidnap him to force him to build a "
                       "devastating weapon. Instead, he builds an armored "
                       "suit and upends his captors. Returning to America, "
                       "Stark refines the suit and uses it to combat crime "
                       "and terrorism.")

bat_man = media.Movie("Bat Man",
		      "https://www.youtube.com/watch?v=EXeTwQWrcwY",
		      "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                      "With the help of allies Lt. Jim Gordon (Gary Oldman) and DA Har"
                      "vey Dent (Aaron Eckhart), Batman (Christian Bale) has been able "
                      "to keep a tight lid on crime in Gotham City. But when a vile you"
                      "ng criminal calling himself the Joker (Heath Ledger) suddenly thr"
                      "ows the town into chaos, the caped Crusader begins to tread a fine"
                      "line between heroism and vigilantism.")
super_man = media.Movie("Super Man",
                        "https://www.youtube.com/watch?v=T6DJcgm3wNY",
                        "https://upload.wikimedia.org/wikipedia/en/8/85"
                        "/ManofSteelFinalPoster.jpg",
                        "With the imminent destruction of Krypton, their home planet, "
                        "Jor-El (Russell Crowe) and his wife seek to preserve their ra"
                        "ce by sending their infant son to Earth. The child's spacecra"
                        "ft lands at the farm of Jonathan (Kevin Costner) and Martha (D"
                        "iane Lane) Kent, who name him Clark and raise him as their own"
                        "son. Though his extraordinary abilities have led to the adult "
                        "Clark (Henry Cavill) living on the fringe of society, he finds"
                        "he must become a hero to save those he loves from a dire threat.")
"""
collect the movie instances into a list
"""
movies = [iron_man, bat_man, super_man]
"""
call fresh_tomatoes.open_movies_page to form the webside
"""
fresh_tomatoes.open_movies_page(movies)
