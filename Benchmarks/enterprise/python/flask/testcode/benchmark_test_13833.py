# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest13833():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(processed)})
    return jsonify({"result": "success"})
