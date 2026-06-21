# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import requests
from flask import jsonify
import pickle


@dataclass
class FormData:
    payload: str

def BenchmarkTest61200():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = FormData(payload=api_value).payload
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
