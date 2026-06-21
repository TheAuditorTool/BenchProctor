# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest76688():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parsed = urlparse(forwarded_ip)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = forwarded_ip
    return redirect(str(target_url))
