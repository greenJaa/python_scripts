#!/usr/bin/env python3

def list_of_files(path):
    import os
    return os.listdir(path)

path = input("Enter path")

print (type(path))
print("Files are:",list_of_files(path))