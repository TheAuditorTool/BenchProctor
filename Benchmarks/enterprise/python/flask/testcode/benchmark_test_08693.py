# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import request, jsonify
import socket


def BenchmarkTest08693():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parsed = urlparse(json_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = json_value
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})
