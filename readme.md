# Run on Local
    mlflow server --host 0.0.0.0 -p 8889
    export MLFLOW_TRACKING_URI=http://127.0.0.1:8889

    python train.py

# Run mlflow

    mlflow server --host 0.0.0.0 -p 8889
    export MLFLOW_TRACKING_URI=http://127.0.0.1:8889
    
    mlflow run .
    mlflow models serve -m file:///mnt/d/work/mlflow/mlflow/examples/supply_chain_security/mlruns/0/2848e2593fc24c7cbcef69b5ad8ec148/artifacts/model -p 1234

# Test From PostMan


    http://127.0.0.1:1234/invocations

    {"dataframe_split": {"data":[[
    
    0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  
    0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  
    0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
    0.0,  0.0,  1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  
    0.0,  0.0,  1.0,  0.0
    
    ]]}}

    {
        "predictions": [
            "yes"
        ]
    }

    ----------------------------------------------------------------------

    {"dataframe_split": {"data":[[
    
    0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  
    0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  
    0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
    0.0,  0.0,  1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  
    0.0,  0.0,  0.0,  1.0
    
    ]]}}

    {
        "predictions": [
            "no"
        ]
    }

    ----------------------------------------------------------------------



# Test From Curl

## On Invocation

    curl -X POST -H "Content-Type:application/json"                     \
    --data "{\"dataframe_split\": {\"data\":[[                          \
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
        0.0,  0.0,  1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  
        0.0,  0.0,  1.0,  0.0]]}}"                                      \
    http://127.0.0.1:1234/invocations | jq

## On Gateway

    curl -X POST -H "Content-Type:application/json"                     \
    --data "{\"data\": {\"data\":[[\"Russian Federation\",\"yes\"]]}}"  \
    http://127.0.0.1:5000/gateway | jq

    {
        "predictions": [
            "no"
        ]
    }


    curl -X POST -H "Content-Type:application/json"                     \
    --data "{\"data\": {\"data\":[[\"Russian Federation\",\"no\"]]}}"  \
    http://127.0.0.1:5000/gateway | jq

    {
        "predictions": [
            "yes"
        ]
    }
    