import pandas as pd
import numpy as np
import urllib.request
from PIL import Image
import re
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error


def limpiar_memory(train,memory_type):
    for type in memory_type:
        memory_lst = []
        for item in train["Memory"]:
            if type in item:
                try:
                    match = re.search(r'\d+(GB|TB)(?=\s'+f'{type})', item).group(0)
                    if "GB" in match:
                        memory_lst.append(int(match.replace("GB", "")))
                    elif "TB" in match:
                        memory_lst.append(int(match.replace("TB", ""))*1000)
                    else:
                        memory_lst.append(int(match))
                except:
                    memory_lst.append(0)
            else:
                memory_lst.append(0)
        train[type.replace(" ","_")] = pd.Series(memory_lst)
    return train


def limpiar_data(train,drop_columns):
    data_df = train.copy()
    data_df.drop(["laptop_ID", 
                # "Product", 
                # "Weight"
                ], axis=1, inplace=True)

    res_lst = list(data_df["ScreenResolution"])
    resolutions = []
    for item in res_lst:
        match = re.search(r'(\d+x\d+)', item)
        if match:
            resolutions.append(match.group(0))
    data_df["Resolution"] = pd.Series(resolutions)
    data_df["Product"] = data_df["Product"].str.split(" ").str[0]
    data_df["Cpu_Provider"] = data_df["Cpu"].str.split(" ").str[0]
    data_df["Gpu_Provider"] = data_df["Gpu"].str.split(" ").str[0]
    data_df["GHz"]  = data_df["Cpu"].str.split(" ").str[-1].str.replace("GHz", "").astype(float)
    data_df["Weight"] = data_df["Weight"].str.replace("kg", "").astype(float)
    data_df["Ram"] = data_df["Ram"].str.replace("GB", "").astype(float)
    data_df["OpSys"].replace('Mac OS X', 'macOS X', inplace=True)
    data_df["OpSys_provider"] = data_df["OpSys"].str.split(" ").str[0]

    memory_type = ["SSD", "HDD", "Flash Storage", "Hybrid"]
    data_df = limpiar_memory(data_df,memory_type)

    ml_data_df = data_df.copy()
    ml_data_df.drop(["Memory",
                    "Cpu",
                    "Gpu",
                    "ScreenResolution",
                    ], 
                    axis=1, inplace=True)

    cat_lst = ["TypeName", 
            "Company", 
            "OpSys", 
            "Cpu_Provider", 
            "Gpu_Provider",
            "OpSys_provider",
            "Resolution",
            "Product"
            ]

    for cat in cat_lst:
        company = list(enumerate(ml_data_df[cat].unique().tolist(), start=1))
        company_dict = {company[i][1] : company[i][0] for i in range(len(company))}
        ml_data_df[cat] = ml_data_df[cat].map(company_dict)
    ml_data_df.drop(drop_columns, axis=1, inplace=True)
    return ml_data_df, data_df