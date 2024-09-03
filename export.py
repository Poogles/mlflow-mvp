"""This is the code to serialise and export our model.

In this case the model is saved to a directory and nothing more is done."""
import os

import mlflow

from model import MODEL_STORAGE_PATH, DummyModel

if __name__ == "__main__":
    # Save the model to a directory
    pyfunc_model_path = os.path.join(MODEL_STORAGE_PATH, "pyfunc_model")
    python_model = DummyModel()
    mlflow.pyfunc.save_model(path=pyfunc_model_path, python_model=python_model)
