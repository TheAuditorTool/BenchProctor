# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest01628():
    referer_value = request.headers.get('Referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
