# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest71311():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    ctx = RequestContext(secret_value)
    data = ctx.payload
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
