from dataset import Graph
import numpy as np 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--movie_path", required = True, help = "Path to movies.csv directory")
ap.add_argument("-r", "--ratings_path", required = True, help = "Path to ratings.csv directory")

args = vars(ap.parse_args())




