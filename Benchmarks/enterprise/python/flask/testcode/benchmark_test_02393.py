# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest02393():
    user_id = request.args.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
