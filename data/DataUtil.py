import pandas as pd
from sklearn.datasets import load_wine


def showDatasetValues(data: pd.DataFrame):
    """
    To know about data and print it
    :param data: dataset
    :return: print few rows of dataset
    """
    with pd.option_context('display.max_rows', 5, 'display.max_columns', 5):
        print(data)


def getWineData() -> pd.DataFrame :
    """
    To load data and send it for training pipeline
    :return: dataset in dataframe format
    """
    data = load_wine(as_frame=True).frame
    showDatasetValues(data)
    return data

