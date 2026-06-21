# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest20751():
    ua_value = request.headers.get('User-Agent', '')
    data = ensure_str(ua_value)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(target_url)}
