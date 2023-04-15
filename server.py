from flask import Flask, request, jsonify
import requests
import json
from waitress import serve
import os

import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sharelib import maskOfficeHour

app = Flask(__name__)
host = os.environ.get('host_ml', '127.0.0.1')
port = os.environ.get('port_ml', '1234')
gateway_port = os.environ.get('gateway_port_ml', '6789')

# def createData(request_data):

#     print(request_data['data'])

#     test_df = pd.DataFrame(request_data['data'])
#     test_df.columns = ["mt.ads_country_dst","@timestamp"]
#     test_df = maskOfficeHour(test_df)
#     test_df = test_df.drop(['@timestamp'], axis=1)

#     X_new = X_transform.transform(test_df)
    
#     data = {
#         "data":
#         X_new.toarray().tolist()
#     }

#     return data

def createDataV2(request_country,request_timestamp):

    print(request_country + " " + request_timestamp)
    
    test_df = pd.DataFrame([[request_country,request_timestamp]],columns=['mt.ads_country_dst', '@timestamp'])
    test_df = maskOfficeHour(test_df)
    test_df = test_df.drop(['@timestamp'], axis=1)

    X_new = X_transform.transform(test_df)
    
    data = {
        "data":
        X_new.toarray().tolist()
    }

    return data

# @app.route('/v1/gateway', methods=['POST'])
# def get_invocations():
#     headers = {
#         "Content-Type": "application/json",
#     }

#     content = request.json
#     request_data = content['data']
#     content_data = createData(request_data)

#     try:
#         resp = requests.post(
#             url="http://%s:%s/invocations" % (host, port),
#             data=json.dumps({"dataframe_split": content_data}),
#             headers=headers,
#         )

#         print(resp.status_code)
#         return resp.json()

#     except Exception as e:
#         errmsg = "Caught exception attempting to call model endpoint: %s" % e
#         print(errmsg, end="")
#         return resp.json()
    

@app.route('/v2/gateway', methods=['POST'])
def get_invocationsV2():
    headers = {
        "Content-Type": "application/json",
    }

    content = request.json
    request_country = content['country']
    request_timestamp = content['timestamp']
    content_data = createDataV2(request_country,request_timestamp)

    try:
        resp = requests.post(
            url="http://%s:%s/invocations" % (host, port),
            data=json.dumps({"dataframe_split": content_data}),
            headers=headers,
        )

        print(resp.status_code)
        return resp.json()

    except Exception as e:
        errmsg = "Caught exception attempting to call model endpoint: %s" % e
        print(errmsg, end="")
        return resp.json()
    
if __name__ == '__main__':
    df = pd.read_csv("data/firewall-traffic.csv")
    df_country = df["mt.ads_country_dst"]
    df_OfficeHour = maskOfficeHour(df)
    df_categories = pd.concat([df_country, df_OfficeHour['is_OfficeHour']], axis=1, sort=False,)
    enc = OneHotEncoder(handle_unknown='ignore')
    X_transform = make_column_transformer((enc,['mt.ads_country_dst']),(enc,['is_OfficeHour']))
    X_transform.fit(df_categories)
    
    print("Server Ready On Port " + gateway_port)

    serve(app, host="0.0.0.0", port=gateway_port)
    