# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import request, jsonify
import socket


def BenchmarkTest21259():
    header_value = request.headers.get('X-Custom-Header', '')
    parsed = urlparse(header_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = header_value
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})
