# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import json


def BenchmarkTest01270():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    try:
        data = json.loads(api_value).get('value', api_value)
    except (json.JSONDecodeError, AttributeError):
        data = api_value
    json.loads(data)
    return jsonify({"result": "success"})
