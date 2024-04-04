import mlflow
from typing import Any

def create_mlflow_experiment(experiment_name:str, artifact_location:str, tags:dict[str,Any]) -> str:
    """
    create a new mlflow experiment with the given name and artifact location.
    """
    try:
        experiment_id = mlflow.create_experiment(
            name = experiment_name, artifact_location=artifact_location, tags=tags
        )
    except Exception as e:
        print(e)
        print(f"Experiment {experiment_name} already exists")
        experiment_id = mlflow.get_experiment_by_name(experiment_name).experiment_id
    
    return experiment_id


def get_mlflow_experiment(experiment_id:str=None, experiment_name:str=None)->mlflow.entities.Experiment:
    """
    Retrieve the mlflow experiment with the given id or name

    Parameters:
    ----------
    experiment_id : str
    experiment_name : str

    Returns:
    -------
    experiment : mlflow.entities.Experiment

    Returns the mlflow experiment with given id or name
    """

    if experiment_id is not None:
        experiment = mlflow.get_experiment(experiment_id)
    elif experiment_name is not None:
        experiment = mlflow.get_experiment_by_name(experiment_name)
    else:
        raise ValueError("Either experiment_id or experimen_name must be provided")
    
    return experiment