# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:03:42 2024

@author: tgilmore10
"""

import pandas as pd
import os
from Concat import Concat

# Folder with data txt files.
folder_path = 'C:\\Users\\terryc\\Desktop\\data'


def main():
    concat(folder_path)


def concat(path):
    cat = Concat()
    cat.set_folder_path(path)
    cat.reformat_file()
    cat.concatenate_file()
    print(cat)


if __name__ == '__main__':
    main()