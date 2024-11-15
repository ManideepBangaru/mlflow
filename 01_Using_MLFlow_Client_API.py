# Loading libraries
from mlflow import MlflowClient
from pprint import pprint
from sklearn.ensemble import RandomForestRegressor

# Configuring the MLflow Tracking Client
client = MlflowClient(tracking_uri="http://127.0.0.1:8080")

# Searching experiments
all_experiments = client.search_experiments()
print(all_experiments)