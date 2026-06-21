# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest72517():
    origin_value = request.headers.get('Origin', '')
    parsed = urlparse(origin_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = origin_value
    return '<script src="' + str(target_url) + '"></script>', 200, {'Content-Type': 'text/html'}
