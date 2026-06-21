# SPDX-License-Identifier: Apache-2.0
import yaml
import requests
from flask import jsonify


def BenchmarkTest19801():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    def normalize(value):
        return value.strip()
    data = normalize(api_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
