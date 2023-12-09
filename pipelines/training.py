import pandas as pd
from sklearn.linear_model import LogisticRegression

import flytekit.extras.sklearn
from flytekit import task, workflow
from data import DataUtil
from model import ClassificationModel
from helper import Utils


"""
In Flyte, tasks are the most basic unit of compute and serve as the building blocks for more complex applications. 
A task is a function that takes some inputs and produces an output. It can also be without any input or outputs.
"""
@task
def get_data() -> pd.DataFrame:
    """Get the wine dataset."""
    return DataUtil.getWineData()

@task
def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """Get preprocessed data for binary classification problem."""
    return Utils.get_preprocessed_dataset(data)

@task
def train_model(data: pd.DataFrame, hyperparameters: dict) -> LogisticRegression:
    """Train a model on the wine dataset."""
    model = ClassificationModel.get_LogisticRegression_Model(data, hyperparameters)
    return model


"""
A workflow is also defined as a Python function, and it specifies the flow of data 
between tasks and, more generally, the dependencies between tasks
"""
@workflow
def run_training_workflow(hyperparameters: dict) -> LogisticRegression:
    """Putting all the steps together into a single workflow."""
    data = get_data()
    processed_data = process_data(data=data)
    return train_model(
        data=processed_data,
        hyperparameters=hyperparameters,
    )


"""
A task is a pure Python function, while a workflow is actually a DSL 
that only supports a subset of Python’s semantics.
"""