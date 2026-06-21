# SPDX-License-Identifier: Apache-2.0
import yaml
import json
import requests
from flask import jsonify


def BenchmarkTest61541():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    prefix = ''
    data = prefix + str(api_value)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
