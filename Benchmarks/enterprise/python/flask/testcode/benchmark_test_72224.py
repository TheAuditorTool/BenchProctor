# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest72224():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
