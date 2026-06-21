# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import json


def BenchmarkTest03598():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
