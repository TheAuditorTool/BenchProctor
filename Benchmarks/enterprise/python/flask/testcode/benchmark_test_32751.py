# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest32751():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
