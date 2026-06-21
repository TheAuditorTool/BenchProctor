# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest49277():
    secret_value = 'config_secret_test_abc123'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
