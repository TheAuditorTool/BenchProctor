# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import request, jsonify
import socket


def BenchmarkTest30846():
    referer_value = request.headers.get('Referer', '')
    parsed = urlparse(referer_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = referer_value
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})
