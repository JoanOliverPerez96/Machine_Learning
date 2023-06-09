import pandas as pd
import urllib.request
from PIL import Image
import numpy as np

from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVR

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV

from sklearn import model_selection
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures


from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, r2_score, mean_squared_error, mean_absolute_error, precision_score, roc_auc_score

import matplotlib.pyplot as plt
import seaborn as sns
