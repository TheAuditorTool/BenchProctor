# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest02516():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    requests.get(str(target_url))
    return jsonify({"result": "success"})
