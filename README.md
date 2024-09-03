## MLflow models MVP example

This is intended to be viewed alongside the [MLflow docs](https://mlflow.org/docs/latest/models.html#mlflow-models).

### Installation

This demo is packaged using poetry.

```python
poetry install
```

### Exporting and running the model

To export our 'model' from the `build.py` file run...

```bash
# Export the model
% poetry run python export.py
```

You should now see a stored model on disk.

```bash
% ls -la /tmp/test_model/pyfunc_model
total 40
drwxr-xr-x  7 spegler  wheel  224  3 Sep 11:43 .
drwxr-xr-x  3 spegler  wheel   96  3 Sep 11:43 ..
-rw-r--r--  1 spegler  wheel  400  3 Sep 11:43 MLmodel
-rw-r--r--  1 spegler  wheel  149  3 Sep 11:43 conda.yaml
-rw-r--r--  1 spegler  wheel  112  3 Sep 11:43 python_env.yaml
-rw-r--r--  1 spegler  wheel   38  3 Sep 11:43 python_model.pkl
-rw-r--r--  1 spegler  wheel   46  3 Sep 11:43 requirements.txt
```

This can then be used 'downstream' by the `run.py`.

```bash
% poetry run python run.py test
3
% poetry run python run.py test
2
```
