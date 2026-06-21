# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest51180():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    requests.get(str(target_url))
    return jsonify({"result": "success"})
