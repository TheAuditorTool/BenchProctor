# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest60641():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(secret_value)
    data = collected
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
