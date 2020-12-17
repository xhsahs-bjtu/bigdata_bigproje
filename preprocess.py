import numpy as np
import pandas as pd
import matplotlib as plt
import os
import csv
class DataSets:
    def __init__(self,path,set_name:str):
        DataSets.num=+1
        self.set_name=set_name
        self.df=self.concat(path,set_name)
    def concat(self,path,set_name):
        df_list = []
        files = os.listdir(path)
        for file in files:
            file_path = os.path.join(path, file)
            df = pd.read_csv(file_path, header=None)
            df_list.append(df)
        result = pd.concat(df_list)
        result.to_csv(os.path.join("resource",set_name+".csv" ), index=False)
        return result
if __name__ == '__main__':
    val_set=DataSets("resource\\val", "val_set")
    train_set = DataSets("resource\\train", "train_set")
    test_set=DataSets("resource\\test","test_set")

