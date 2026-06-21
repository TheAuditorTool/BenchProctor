# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest11623():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return jsonify({"result": "success"})
