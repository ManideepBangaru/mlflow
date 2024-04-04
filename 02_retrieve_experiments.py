import mlflow
from mlflow_utils import get_mlflow_experiment

if __name__ == "__main__":
    # retrieve experiment
    experiment = get_mlflow_experiment(experiment_name="testing_mlflow2")

    print("Name : %s"%experiment.name)
    print("Experiment_id : %s"%experiment.experiment_id)
    print("Artifact Location : %s"%experiment.artifact_location)
    print("Tags : %s"%experiment.tags)
    print("Lifecycle_stage : %s"%experiment.lifecycle_stage)
    print("Creation timestamp : %s"%experiment.creation_time)