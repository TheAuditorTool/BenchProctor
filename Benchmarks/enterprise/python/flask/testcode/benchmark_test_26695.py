# SPDX-License-Identifier: Apache-2.0
import yaml
import requests
from flask import jsonify


def BenchmarkTest26695():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = ' '.join(str(api_value).split())
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
