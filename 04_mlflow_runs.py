import mlflow

if __name__ == "__main__":
    # start run
    mlflow.start_run()
    
    # Machine learning code goes here 
    mlflow.log_param("learning rate", 0.01)

    # end run
    mlflow.end_run()