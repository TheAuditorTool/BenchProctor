# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest01996():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
