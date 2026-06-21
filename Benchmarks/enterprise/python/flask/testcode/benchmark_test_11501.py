# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest11501():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requests.post('http://api.prod.internal/data', data=str(processed))
    return jsonify({"result": "success"})
