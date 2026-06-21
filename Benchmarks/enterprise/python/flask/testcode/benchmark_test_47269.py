# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import base64
from flask import request, jsonify


def BenchmarkTest47269():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return '<script src="' + str(target_url) + '"></script>', 200, {'Content-Type': 'text/html'}
