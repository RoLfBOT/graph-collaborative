import numpy as np 
# from recommender import Recommender
# from dataset import Graph
# from search import searchTrie
import argparse
import operator

# ap = argparse.ArgumentParser()
# ap.add_argument("-m", "--movie_path", required = True, help = "Path to movies.csv directory")
# ap.add_argument("-r", "--ratings_path", required = True, help = "Path to ratings.csv directory")

# args = vars(ap.parse_args())

class User:
    
    f = open("user.txt", 'r')
    userIdgen = int(f.read())
    f.close()
    
    def __init__(self, name, userId = None, new = True):
        self.name = name

        if(new):
            self.userId = User.userIdgen + 1
            User.userIdgen = User.userIdgen + 1
            
            f = open('user.txt', 'w')
            f.seek(0)
            f.write(str(User.userIdgen))
            f.truncate()
            f.close()

        else:
            self.userId = userId

    def rateMovie(self, movie):
        print(movie + "-- rate on a scale of 1 - 5: ")
    
    # def searchMovie(self, searchTrieObj):


def main():
    
    print("")
    print("Are you a new user [y/n]: ")

    a = str(input())

    if(a == 'y' or a == 'Y'):  
        print("Enter your name: ")
        name = str(input())
        user = User(name)
    
    else:
        print("Enter your userId: ")
        print("Enter your name: ")
        name = str(input())
        userId = int(input())
        user = User(name, userId, new = False)

    


if __name__ == '__main__':
    main()
