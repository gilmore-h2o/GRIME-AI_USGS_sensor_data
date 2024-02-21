# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:38:00 2024

@author: terryc
"""

import os
import pandas as pd

#
# This was written how I learned it in my Comp Sci class,
# let me know if this is at all correct.
#


class Concat:

    # Vars
    __folder_path = ''
    __dfs = []

    # Init
    def __init__(self, folder_path='', dfs=[]):
        self.set_folder_path(folder_path)
        self.set_dfs(dfs)

    # Getters
    def get_folder_path(self):
        return self.__folder_path

    def get_dfs(self):
        return self.__dfs

    # Setters
    def set_folder_path(self, folder_path):
        self.__folder_path = folder_path

    def set_dfs(self, dfs):
        self.__dfs = dfs

    # Helpers
    def reformat_file(self):
        # Initialize an empty list to store DataFrames
        self.set_dfs([])

        for filename in os.listdir((self.get_folder_path())):
            filename.lower()
            if filename.endswith('.txt'):
                file_path = os.path.join(self.get_folder_path(), filename)
                # import file and remove commented-out rows at the top of the original file
                df_temp = pd.read_csv(file_path, delimiter='\t', comment='#')
                self.get_dfs().append(df_temp)

    def concatenate_file(self):
        # Concatenate all DataFrames into a single DataFrame
        USGS_stage_df = pd.concat(self.get_dfs(), ignore_index=True)
        USGS_stage_df = USGS_stage_df[~USGS_stage_df['agency_cd'].astype(str).str.contains("5s")]

        # Outputs concatenated data to a CSV file in same directory that was accessed.
        self.output_csv(USGS_stage_df)

    def output_csv(self, USGS_stage_df):
        # Outputs USGS_stage_df to CSV. 'output.csv' should be changed to a var so it doesn't overwrite itself.
        USGS_stage_df.to_csv(self.get_folder_path() + '\\output.csv', index=False)

    # ToString
    def __str__(self):
        console = f'dfs: {self.get_dfs()}\npath: {self.get_folder_path()}'
        return console
