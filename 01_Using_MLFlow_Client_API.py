# Loading libraries
from mlflow import MlflowClient
from pprint import pprint
from sklearn.ensemble import RandomForestRegressor

# Configuring the MLflow Tracking Client
client = MlflowClient(tracking_uri="http://127.0.0.1:5000")

# Searching experiments
all_experiments = client.search_experiments()
print(all_experiments)

# default experiment search
default_experiment = [
    {"name": experiment.name, 
     "lifecycle_stage": experiment.lifecycle_stage
     }
    for experiment in all_experiments
    if experiment.name == "Default"
][0]

pprint(default_experiment)