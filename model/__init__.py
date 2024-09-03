"""This is our 'model'."""
import os
import numpy as np

import mlflow
from mlflow.models import set_model

MODEL_STORAGE_PATH = "/tmp/test_model"
MODEL_NAME = "pyfunc_model"


class DummyModel(mlflow.pyfunc.PythonModel):
    def predict(self, context, model_input: str):
        """Predict a random string index based upon the len(model_input)."""
        return np.random.randint(0, len(model_input))


# Set up model inheritance correctly.
set_model(DummyModel())
