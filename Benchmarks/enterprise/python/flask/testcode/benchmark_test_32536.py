# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import pickle


def BenchmarkTest32536():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = (lambda v: v.strip())(api_value)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
