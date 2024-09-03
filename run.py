"""This is our model runner.

This will in relaity likely be a different application entirely. This will
load the model from file (likely remotely) and perform inference based upon
the inputs.
"""
import os
import sys

import mlflow

# These are hard coded here so we have no dependencies on the `model` module.
MODEL_STORAGE_PATH = "/tmp/test_model"
MODEL_NAME = "pyfunc_model"


if __name__ == "__main__":

    # Save the model to a directory
    pyfunc_model_path = os.path.join(MODEL_STORAGE_PATH, MODEL_NAME)

    # Load the model
    loaded_pyfunc_model = mlflow.pyfunc.load_model(model_uri=pyfunc_model_path)

    # Run inference and print result.
    res = loaded_pyfunc_model.predict(sys.argv[1])
    print(res)
