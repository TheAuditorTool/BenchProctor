# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import request, jsonify
import urllib.request


@dataclass
class FormData:
    payload: str

def BenchmarkTest25849():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
