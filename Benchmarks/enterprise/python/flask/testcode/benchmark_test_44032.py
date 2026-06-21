# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from dataclasses import dataclass
from flask import request, jsonify
import socket


@dataclass
class FormData:
    payload: str

def BenchmarkTest44032():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = FormData(payload=forwarded_ip).payload
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})
