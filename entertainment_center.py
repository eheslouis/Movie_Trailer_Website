import media
import fresh_tomatoes

# class instantiating section for each movie:
nemo = media.Movie("Nemo",
                   "After his son is captured in the Great "
                   "Barrier Reef and taken to Sydney, a timid "
                   "clownfish sets out on a journey to bring him home.",
                   "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg", # noqa
                   "https://www.youtube.com/watch?v=wZdpNglLbt8") # noqa


avatar = media.Movie("Avatar",
                     "a marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", # noqa
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4") # noqa


dirty_dancing = media.Movie("Dirty Dancing",
                            "Spending the summer at a Catskills resort "
                            "with her family, Frances 'Baby' Houseman falls "
                            "in love with the camp's dance instructor, "
                            "Johnny Castle.",
                            "https://upload.wikimedia.org/wikipedia/en/0/00/Dirty_Dancing.jpg", # noqa
                            "https://www.youtube.com/watch?v=HFK_i5r1WJk") # noqa

ratatouille = media.Movie("Ratatouille",
                          "A rat who can cook makes an unusual alliance "
                          "with a young kitchen worker at a famous restaurant.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", # noqa
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk") # noqa

hunger_games = media.Movie("The Hunger Games",
                           "Katniss Everdeen voluntarily takes her younger "
                           "sister's place in the Hunger Games, a televised "
                           "competition in which two teenagers from each of "
                           "the twelve Districts of Panem are chosen at "
                           "random to fight to the death.",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", # noqa
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY") # noqa

now_U_C_me = media.Movie("Now you see me",
                         "An FBI agent and an Interpol detective track a "
                         "team of illusionists who pull off bank heists "
                         "during their performances and reward their "
                         "audiences with the money.",
                         "https://upload.wikimedia.org/wikipedia/en/c/c7/Now_You_See_Me_Poster.jpg", # noqa
                         "https://www.youtube.com/watch?v=8MHDYZJWLXA") # noqa

# appending movies into a list:
movies = [nemo, avatar,dirty_dancing, ratatouille, hunger_games, now_U_C_me]

# calling the external rendering function:
fresh_tomatoes.open_movies_page(movies)
