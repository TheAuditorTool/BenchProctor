# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest03671():
    cookie_value = request.cookies.get('session_token', '')
    data = default_blank(cookie_value)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    requests.post('http://api.prod.internal/data', data=str(target_url))
    return jsonify({"result": "success"})
