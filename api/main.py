"""This is our model runner.

This will in relaity likely be a different application entirely. This will
load the model from file (likely remotely) and perform inference based upon
the inputs.
"""

import os
import sys

import mlflow
from fastapi import FastAPI
from pydantic import BaseModel

# These are hard coded here so we have no dependencies on the `model` module.
MODEL_STORAGE_PATH = "/tmp/test_model"
MODEL_NAME = "pyfunc_model"


app = FastAPI()


class Payload(BaseModel):
    version: str = "v1"
    input: str


@app.post("/model")
def run_model(payload: Payload) -> list[str]:
    loaded_model = app.extra.get(payload.version)
    if not app.extra.get(payload.version):
        pyfunc_model_path = os.path.join(
            MODEL_STORAGE_PATH, MODEL_NAME + "." + payload.version
        )

        # Load the model
        loaded_model = mlflow.pyfunc.load_model(model_uri=pyfunc_model_path)
        mlflow.pyfunc.get_model_dependencies(pyfunc_model_path)

        # Set the loaded model in the fastapi cache.
        app.extra[payload.version] = loaded_model

    # Run inference and print result.
    input_ = list(payload.input)
    print("input: ", input_)
    res = loaded_model.predict(input_)
    print(res)

    return res
