# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest64028():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
