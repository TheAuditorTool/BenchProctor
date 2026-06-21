# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest75380():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = (lambda v: v.strip())(api_value)
    requests.get(str(data))
    return jsonify({"result": "success"})
