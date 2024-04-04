import mlflow

if __name__ == '__main__':
    # create a mlflow experiment
    mlflow.create_experiment(
            name = "testing_mlflow1",
            artifact_location = "testing_mlflow1_artifacts",
            tags = {"env":"dev","version":"1.0.0"},
    )