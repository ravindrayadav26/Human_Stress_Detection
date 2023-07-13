# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st


@st.cache_resource()
def load_data():
    # This function returns the preprocessed data

    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('Stress.csv')

    # Rename the column names in the DataFrame.
    df.rename(columns={"t": "bt", }, inplace=True)

    # Perform feature and target split
    x = df[["gsr", "rr", "bt", "lm", "bo", "rem", "sh", "hr"]]
    y = df['sl']

    return df, x, y


@st.cache_resource()
def train_model(x, y):
    # This function trains the model and return the model and model score
    # Create the model
    model = DecisionTreeClassifier(
        ccp_alpha=0.0, class_weight=None, criterion='entropy',
        max_depth=4, max_features=None, max_leaf_nodes=None,
        min_impurity_decrease=0.0, min_samples_leaf=1,
        min_samples_split=2, min_weight_fraction_leaf=0.0,
        random_state=42, splitter='best'
    )
    # Fit the data on model
    model.fit(x, y)
    # Get the model score
    score = model.score(x, y)

    # Return the values
    return model, score


def detect(x, y, features):
    # Get model and model score
    model, score = train_model(x, y)
    # detect the value
    detection = model.predict(np.array(features).reshape(1, -1))

    return detection, score
