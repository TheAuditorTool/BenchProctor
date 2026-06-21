# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest60072():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
