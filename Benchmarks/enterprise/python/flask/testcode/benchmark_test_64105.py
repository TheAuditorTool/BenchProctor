# SPDX-License-Identifier: Apache-2.0
import yaml
import requests
from flask import jsonify


def BenchmarkTest64105():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    parts = []
    for token in str(api_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
