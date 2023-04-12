# Run on Local WSL Ubuntu 20.04 
## need python 3.9
    
    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.9
    python3.9 --version

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3.9 get-pip.py

    pip3.9 install -r requirements.txt
    
    ### please load firewall-traffic.csv to folder data
    python3.9 train.py

        mlflow ui
        export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
    or 
        mlflow server --host 0.0.0.0 -p 8889
        export MLFLOW_TRACKING_URI=http://127.0.0.1:8889

# Run mlflow

    mlflow server --host 0.0.0.0 -p 8889
    export MLFLOW_TRACKING_URI=http://127.0.0.1:8889
    
    mlflow run .
    mlflow models serve -m file:///mnt/d/work/mlflow/mlflow/examples/supply_chain_security/mlruns/0/2848e2593fc24c7cbcef69b5ad8ec148/artifacts/model -p 1234

    mlflow models serve -m mlflow-artifacts:/5/8911fc4e3a514e969cac16d157b008ed/artifacts/model -p 1236

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
    
    curl -X POST -H "Content-Type:application/json"                     \
    --data "{\"dataframe_split\": {\"data\":[[                          \
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
        0.0,  0.0,  1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  
        0.0,  0.0,  1.0,  0.0]]}}"                                      \
    http://nginx-auth-test.tdg-int.net/invocations -u 'ingress_user:xxxxxxxxxxxxxxxxxxxxxx' | jq
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
    

## Docker Rum

    docker run --name mlflow-api -p 6543:5000 -e MODEL_URI=gs://mlflow_gke_test_20230314/5/8911fc4e3a514e969cac16d157b008ed/artifacts/model -e SERVING_PORT=5000 -e GOOGLE_APPLICATION_CREDENTIALS="/data/app/secret/gcp.json" -v /mnt/d/firework/gcr-authen-json/gcp-dmp-devops.json:/data/app/secret/gcp.json mlflow_serving:v1

## Docker Rum into container

    docker run -it --entrypoint bash --name mlflow-api -p 6543:5000 -e MODEL_URI=gs://mlflow_gke_test_20230314/5/8911fc4e3a514e969cac16d157b008ed/artifacts/model -e SERVING_PORT=5000 -e GOOGLE_APPLICATION_CREDENTIALS="/data/app/secret/gcp.json" -v /mnt/d/firework/gcr-authen-json/gcp-dmp-devops.json:/data/app/secret/gcp.json mlflow_serving:v1