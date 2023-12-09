import pandas as pd

def get_preprocessed_dataset(data: pd.DataFrame) -> pd.DataFrame :
    """
    Simplify the task from a 3-class to a binary classification problem.
    original (178 instances) = class_0 (59), class_1 (71), class_2 (48)
    preprocessed (130 instances) = class_0 (59), class_1 (71)
    """
    newdata = data.assign(target=lambda x: x["target"].where(x["target"] == 0, 1))
    return newdata