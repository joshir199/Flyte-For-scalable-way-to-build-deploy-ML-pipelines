import pandas as pd
from sklearn.linear_model import LogisticRegression

def get_LogisticRegression_Model(data: pd.DataFrame, hyperparameters: dict) -> LogisticRegression:

    """
    Train a model on the wine dataset.
    :param data: training dataset
    :param hyperparameters: hyperparameters for the model
    :return: trained logistic regression model
    """

    features = data.drop("target", axis="columns")
    target = data["target"]
    return LogisticRegression(max_iter=3000, **hyperparameters).fit(features, target)