import media
import fresh_tomatoes

link = "https://upload.wikimedia.org/wikipedia/en/6/6d/Evil_Dead_II_poster.jpg"

evil_dead_2 = media.Movie("Evil Dead 2", """Ash has to survive in a haunted
                          cabin in the woods""",
                          "https://upload.wikimedia.org/wikipedia/en/6/6d/Evil_Dead_II_poster.jpg",
                          "https://www.youtube.com/watch?v=XPOYmHqWeJE",
                          "Sam Raimi")


yojimbo = media.Movie("Yojimbo", """A Ronan is asked to help a town with two
                      waring gangs""",
                      "https://upload.wikimedia.org/wikipedia/en/8/8b/Yojimbo_%28movie_poster%29.jpg",
                      "https://www.youtube.com/watch?v=WzFq5hOlZ5s",
                      "Akira Kurosawa")


mad_max = media.Movie("Mad Max: Fury Road", """Mad Max helps Furiosa & several
                      female prisoners escape the Evil Immortan Joe""",
                      "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
                      "https://www.youtube.com/watch?v=hEJnMQG9ev8",
                      "George Miller")

shawshank_redemption = media.Movie("Shawshank Redemption", """A man has to
                                   survive prison after being falsey
                                   accused of murder""",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                   "https://www.youtube.com/watch?v=NmzuHjWmXOc",
                                   "Frank Darabont")

the_dark_knight = media.Movie("The Dark Knight", """Batman must procect Gotham
                              city from a mysterious new villian called The
                              Joker""",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                              "Christopher Nolan")

alien = media.Movie("Alien", """A group of people aboard a spaceship are
                    stalked by a mysterious alien creature""",
                    "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",
                    "https://www.youtube.com/watch?v=jQ5lPt9edzQ",
                    "Ridley Scott")

movies = [evil_dead_2, yojimbo, mad_max, shawshank_redemption, the_dark_knight,
          alien]
fresh_tomatoes.open_movies_page(movies)
