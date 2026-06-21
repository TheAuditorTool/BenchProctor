# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest05759():
    raw_body = request.get_data(as_text=True)
    parsed = urlparse(raw_body)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = raw_body
    requests.get(str(target_url))
    return jsonify({"result": "success"})
