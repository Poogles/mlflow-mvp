"""This is the code to serialise and export our model.

In this case the model is saved to a directory and nothing more is done."""

import os

import mlflow

MODEL_STORAGE_PATH = "/tmp/test_model"


def predict_v1(model_input: list[str]) -> list[str]:
    """This uppercases every input char and outputs a new list."""
    import numpy as np
    return [i.upper() for i in model_input]


def predict_v2(model_input: list[str]) -> list[str]:
    """This spongebobCases every input char and outputs a new list."""
    import numpy as np
    return [t.upper() if (i % 2 == 0) else t.lower() for i, t in enumerate(model_input)]


if __name__ == "__main__":
    pyfunc_model_path_v1 = os.path.join(MODEL_STORAGE_PATH, "pyfunc_model.v1")
    mlflow.pyfunc.save_model(
        path=pyfunc_model_path_v1,
        python_model=predict_v1,
        input_example=["a"],
        pip_requirements=["numpy==2.1.0"],
    )

    pyfunc_model_path_v2 = os.path.join(MODEL_STORAGE_PATH, "pyfunc_model.v2")
    mlflow.pyfunc.save_model(
        path=pyfunc_model_path_v2,
        python_model=predict_v2,
        input_example=["a"],
        pip_requirements=["numpy==2.1.1"],
    )
