# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def relay_value(value):
    return value

def BenchmarkTest63712():
    raw_body = request.get_data(as_text=True)
    data = relay_value(raw_body)
    if str(data) not in ('admin', 'user', 'guest', 'viewer'):
        return jsonify({'error': 'forbidden'}), 403
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
