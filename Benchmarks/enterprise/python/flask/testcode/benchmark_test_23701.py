# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import request, jsonify
import socket


def BenchmarkTest23701():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})
