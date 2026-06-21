# SPDX-License-Identifier: Apache-2.0
import requests
import json
from flask import jsonify


def BenchmarkTest53822():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = json.loads(api_value).get('value', '')
    requests.get(str(data))
    return jsonify({"result": "success"})
