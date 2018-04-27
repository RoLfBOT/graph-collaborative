import numpy as np 
from recommender import Recommender
from dataset import Graph
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--movie_path", required = True, help = "Path to movies.csv directory")
ap.add_argument("-r", "--ratings_path", required = True, help = "Path to ratings.csv directory")

args = vars(ap.parse_args())

class User:
    userIdgen = 300
    
    def __init__(self, name):
        self.name = name
        self.userId = User.userIdgen + 1

