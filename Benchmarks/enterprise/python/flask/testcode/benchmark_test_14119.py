# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest14119():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = coalesce_blank(api_value)
    json.loads(data)
    return jsonify({"result": "success"})
