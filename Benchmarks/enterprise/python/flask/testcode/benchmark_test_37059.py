# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest37059():
    header_value = request.headers.get('X-Custom-Header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    requests.get(str(target_url))
    return jsonify({"result": "success"})
