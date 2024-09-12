## MLflow models MVP example

This is intended to be viewed alongside the [MLflow docs](https://mlflow.org/docs/latest/models.html#mlflow-models).

### Installation

This demo is packaged using poetry, both 'parts' are packaged seperately.

```python
poetry install
```

### Exporting and running the model

To export our 'models' from the `model` directory run...

```bash
# Export the models
% cd model && poetry run python export.py
```

You should now see a pair of stored models on disk.

```bash
% ls -la /tmp/test_model/
total 0
drwxr-xr-x    4 spegler  wheel   128 11 Sep 17:57 .
drwxrwxrwt  117 root     wheel  3744 12 Sep 07:46 ..
drwxr-xr-x    9 spegler  wheel   288 11 Sep 17:57 pyfunc_model.v1
drwxr-xr-x    9 spegler  wheel   288 11 Sep 17:57 pyfunc_model.v2
```

You can now run the API to serve the models.

```bash
% cd ../api && poetry run fastapi dev
...
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

The above message shows when the API is running and ready to serve traffic.

To test the models, run the following in another terminal window.

```bash
# Try v1 of the model.
% curl -H "Content-type: application/json" -d'{"version":"v1","input":"potato"}' http://127.0.0.1:8000/model
["P","O","T","A","T","O"]
# Try v2 of the model.
% curl -H "Content-type: application/json" -d'{"version":"v2","input":"potato"}' http://127.0.0.1:8000/model
["P","o","T","a","T","o"]
```

### Thoughts

1. Initial loading of the MLflow libraries takes some time, but once they're
	in the python VM it's relatively quick to load a model (proportional to
	the size of the model).
2. Currently this doesn't manage dependencies independely between the `api` and
	`model` modules.