# Goal:
# to track movies user wants to watch, then already watched movies
# i may create GUI later
# create list of movies
# user adds movies to the list
# user removes from the entire lists
# user marks as watched
def greetings():
    username = input("Enter your username: ")
    return f'Hello {username}, welcome to my movie watchlist tracker!'
print(greetings())
want_to_watch =[]
def movie_title():
    while True:
        movie_name = input('Enter the name of the movie/series you want to watch: ')
        print('(print quit if you want to exit the "Wish To Watch" cart)')
        if movie_name.lower().strip() == 'quit':
            break
        elif movie_name in want_to_watch:
            print('There is already such movie/series in your watchlist')
        else:
            want_to_watch.append(movie_title)
movie_title()
print(want_to_watch)