# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest31851():
    multipart_value = request.form.get('multipart_field', '')
    data = ensure_str(multipart_value)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    requests.post('http://api.prod.internal/data', data=str(target_url))
    return jsonify({"result": "success"})
