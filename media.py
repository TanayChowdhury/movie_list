import webbrowser
import fresh_tomatoes


"""Defines the class movie to show the attributes of the movies represented by
by the multiple instances of the class"""
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

""" The attributes corresponds to the following outcome.
        self.title = Title of the movie
        self.storyline = A breif description of the movie
        self.poster_image_url = Cover Image sourced from external urls
        self.trailer_youtube_url = A trailer sourced from youtube """

def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


""" Multiple instances of the Class Movie to represent the favorite movies;"""
toy_story = Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

interstellar = Movie("Interstellar",
                           "A group of astronauts who travel through a wormhole"
                           " in search of a new home for humanity.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

netaji = Movie("Netaji, The forgotten hero",
                     "The film depicts the life of the Indian independence leader"
                     " Subhas Chandra Bose",
                     "https://upload.wikimedia.org/wikipedia/en/f/f8/Bosefilm.jpg",
                     "https://www.youtube.com/watch?v=dfzCuNElusk")

lala_land = Movie("La La Land",
                        "A jazz pianist and an aspiring actress who meet and"
                        " fall in love in Los Angeles.",
                        "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
                        "https://www.youtube.com/watch?v=0pdqf4P9MB8")

inside_out = Movie("Inside Out",
                         "The film is set in the mind of a young girl named Riley"
                         " Andersen where five personified emotions; Joy, Sadness,"
                         " Anger, Fear and Disgust try to lead her through life",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=yRUAzGQ3nSY")

movies = [toy_story, avatar, interstellar, netaji, lala_land, inside_out]

fresh_tomatoes.open_movies_page(movies)
