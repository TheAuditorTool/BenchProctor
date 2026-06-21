# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest73510():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
