# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest75722():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    if api_value:
        data = api_value
    else:
        data = ''
    requests.get(str(data))
    return jsonify({"result": "success"})
