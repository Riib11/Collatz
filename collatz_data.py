import pickle
import collatz_calculator as cc

file_name = "collatz_data.txt"

def update(maxi=100000):
    cc.generate_tree(1,maxi)
    with open(file_name, 'wb') as f:
        pickle.dump(cc.tree, f)

def read():
    with open(file_name, 'rb') as f:
        return pickle.load(f)