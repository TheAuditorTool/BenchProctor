# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify


def BenchmarkTest33139():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(graphql_var)
    data = collected
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requests.post('http://api.prod.internal/data', data=str(processed))
    return jsonify({"result": "success"})
