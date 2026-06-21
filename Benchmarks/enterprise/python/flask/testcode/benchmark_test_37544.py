# SPDX-License-Identifier: Apache-2.0
import json
import requests
from flask import jsonify
import pickle


def BenchmarkTest37544():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = json.loads(api_value).get('value', '')
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
