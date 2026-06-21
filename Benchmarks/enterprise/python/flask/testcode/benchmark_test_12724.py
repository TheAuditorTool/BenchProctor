# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest12724():
    secret_value = 'config_secret_test_abc123'
    pending = list(str(secret_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
