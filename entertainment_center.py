import media
import fresh_tomatoes
'''
The media.py file contains the Movie class which we're going to use along the file.

The fresh_tomatoes.py file will create the .html with our Movie objects
'''

t1 = media.Movie('Shawshank Redemption',
                        'Two imprisoned men bond over a number of years,\
                         finding solace and eventual redemption \
                         through acts of common decency.',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_UY1200_CR88,0,630,1200_AL_.jpg',
                        'https://www.youtube.com/watch?v=6hB3S9bIaco')


t2 = media.Movie('The Godfather',
                        'The aging patriarch of an organized crime \
                        dynasty transfers control of his clandestine \
                        empire to his reluctant son.',
                        'https://s-media-cache-ak0.pinimg.com/736x/40/b4/21/40b421c7cfe1b3059d5e50d79e968270.jpg',
                        'https://www.youtube.com/watch?v=sY1S34973zA')


t3 = media.Movie('The Godfather part II',
                        'The early life and career of Vito Corleone \
                        in 1920s New York is portrayed while his son, \
                        Michael, expands and tightens his grip on the \
                        family crime syndicate.',
                        'https://s-media-cache-ak0.pinimg.com/originals/24/0a/b7/240ab70cb2503acf8be581e6509f4c0b.jpg',
                        'https://www.youtube.com/watch?v=qJr92K_hKl0')


t4 = media.Movie('The Dark Knight',
                        'When the menace known as the Joker wreaks \
                        havoc and chaos on the people of Gotham, \
                        the caped crusader must come to terms with \
                        one of the greatest psychological tests of \
                        his ability to fight injustice.',
                        'http://www.impawards.com/2008/posters/dark_knight_ver12_xlg.jpg',
                        'https://www.youtube.com/watch?v=EXeTwQWrcwY')


t5 = media.Movie('12 Angry Men',
                        'A jury holdout attempts to prevent a \
                        miscarriage of justice by forcing his \
                        colleagues to reconsider the evidence.',
                        'http://www.impawards.com/1957/posters/twelve_angry_men.jpg',
                        'https://www.youtube.com/watch?v=fSG38tk6TpI')


t6 = media.Movie('Schindlers List',
                        'In German-occupied Poland during World \
                        War II, Oskar Schindler gradually becomes \
                        concerned for his Jewish workforce after\
                         witnessing their persecution by the Nazi Germans.',
                        'http://fontmeme.com/images/Schindler%E2%80%99s-List-Poster.jpg',
                        'https://www.youtube.com/watch?v=JdRGC-w9syA')

t7 = media.Movie('Pulp Fiction',
                        'The lives of two mob hit men, a boxer, \
                        a gangsters wife, and a pair of diner \
                        bandits intertwine in four tales of \
                        violence and redemption.',
                        'http://www.impawards.com/1994/posters/pulp_fiction.jpg',
                        'https://www.youtube.com/watch?v=s7EdQ4FqbhY')

t8 = media.Movie('The Lord of the Rings: The Return of the King',
                        'Gandalf and Aragorn lead the World of \
                        Men against Saurons army to draw his gaze \
                        from Frodo and Sam as they approach Mount \
                        Doom with the One Ring.',
                        'http://www.impawards.com/2003/posters/lord_of_the_rings_the_return_of_the_king.jpg',
                        'https://www.youtube.com/watch?v=r5X-hFf6Bwo')

t9 = media.Movie('Il buono, il brutto, il cattivo',
                        'A bounty hunting scam joins two men in an \
                        uneasy alliance against a third in a race to \
                        find a fortune in gold buried in a remote cemetery.',
                        'http://cdn3.volusion.com/qpggq.ugjpw/v/vspfiles/photos/3659-2.jpg',
                        'https://www.youtube.com/watch?v=UHctLmLIrpQ')

t10 = media.Movie('Fight Club',
                        'An insomniac office worker, looking for a way \
                        to change his life, crosses paths with a \
                        devil-may-care soap maker, forming an underground \
                        fight club that evolves into something much, much more.',
                        'https://ok2disconnectportfolio.files.wordpress.com/2012/02/fight-club-hi-res-poster-vertical-a31.jpg',
                        'https://www.youtube.com/watch?v=SUXWAEX2jlg')



movies=[t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
fresh_tomatoes.open_movies_page(movies)
