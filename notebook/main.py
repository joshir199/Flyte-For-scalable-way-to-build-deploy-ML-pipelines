from dataclasses import asdict
from dataclasses_json import dataclass_json
from flytekit.core.base_task import dataclass
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from typing import Optional

import flytekit.extras.sklearn
from flytekit import task, workflow


@dataclass_json
@dataclass
class Hyperparameters:
  C:float
  max_iter:Optional[int]=2500

@task
def get_data() -> pd.DataFrame:
    """Get the wine dataset."""
    return load_wine(as_frame=True).frame

@task
def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """Simplify the task from a 3-class to a binary classification problem."""
    return data.assign(target=lambda x: x["target"].where(x["target"] == 0, 1))

@task
def train_model(data: pd.DataFrame, hyperparameters: Hyperparameters) -> LogisticRegression:
    """Train a model on the wine dataset."""
    features = data.drop("target", axis="columns")
    target = data["target"]
    return LogisticRegression(**asdict(hyperparameters)).fit(features, target)


@workflow
def training_workflow(hyperparameters: Hyperparameters) -> LogisticRegression:
    """Put all of the steps together into a single workflow."""
    data = get_data()
    processed_data = process_data(data=data)
    return train_model(
        data=processed_data,
        hyperparameters=hyperparameters,
    )

if __name__=="__main__":
  value = training_workflow(hyperparameters=Hyperparameters(C=0.3, max_iter=2600))
  print("ans: ", value)