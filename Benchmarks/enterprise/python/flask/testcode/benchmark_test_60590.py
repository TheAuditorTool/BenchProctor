# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest60590():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parsed = urlparse(json_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = json_value
    return redirect(str(target_url))
