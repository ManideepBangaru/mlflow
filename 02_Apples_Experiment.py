# Loading libraries
from mlflow import MlflowClient

# Configuring the MLflow Tracking Client
client = MlflowClient(tracking_uri="http://127.0.0.1:5000")

# # Provide an Experiment description that will appear in the UI
# experiment_description = (
#     "This is the grocery forecasting project. "
#     "This experiment contains the produce models for apples."
# )

# # Provide searchable tags that define characteristics of the Runs that
# # will be in this Experiment
# experiment_tags = {
#     "project_name": "grocery-forecasting",
#     "store_dept": "produce",
#     "team": "stores-ml",
#     "project_quarter": "Q3-2023",
#     "mlflow.note.content": experiment_description,
# }

# # Create the Experiment, providing a unique name
# produce_apples_experiment = client.create_experiment(
#     name="Apple_Models", tags=experiment_tags
# )

# Searching based on tags
# Use search_experiments() to search on the project_name tag key

apples_experiment = client.search_experiments(
    filter_string="tags.`project_name` = 'grocery-forecasting'"
)

print(vars(apples_experiment[0]))