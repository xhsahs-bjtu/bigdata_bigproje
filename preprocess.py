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
        # types=[]
        files = os.listdir(path)
        # print(files)
        for file in files:
            type = file[file.find(".") - 1]  # ECG type
        #     types.append(type)
        # print(set(types))
            file_path = os.path.join(path, file)
            df = pd.read_csv(file_path, header=None)
            df["type"]=type
            df_list.append(df)
        result = pd.concat(df_list)
        result.to_csv(os.path.join("resource",set_name+".csv" ), index=False)
        return result
if __name__ == '__main__':
    # val_set=DataSets("resource\\val", "val_set_")
    train_set = DataSets("resource\\train", "train_set_")
    test_set=DataSets("resource\\test","test_set_")

