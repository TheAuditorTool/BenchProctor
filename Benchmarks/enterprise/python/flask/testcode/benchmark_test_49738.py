# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import os
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest49738():
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return jsonify({"result": "success"})
