#!/usr/bin/env python3

import os


path = input("Please enter path")
if not os._exists(path):
    #os.makedirs(path)