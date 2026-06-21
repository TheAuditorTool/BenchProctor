# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import pickle


def BenchmarkTest61552():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    pending = list(str(api_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
