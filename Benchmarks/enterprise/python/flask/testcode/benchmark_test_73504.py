# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest73504():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    reader = make_reader(api_value)
    data = reader()
    requests.get(str(data))
    return jsonify({"result": "success"})
