# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from dataclasses import dataclass
from flask import request, jsonify
import socket


@dataclass
class FormData:
    payload: str

def BenchmarkTest04234():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return jsonify({"result": "success"})
