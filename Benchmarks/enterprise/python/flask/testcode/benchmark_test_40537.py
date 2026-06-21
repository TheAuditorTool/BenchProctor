# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import json
import socket


def BenchmarkTest40537():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    try:
        data = json.loads(api_value).get('value', api_value)
    except (json.JSONDecodeError, AttributeError):
        data = api_value
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
