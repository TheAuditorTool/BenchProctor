# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest54661():
    field_value = request.form.get('field', '')
    data = coalesce_blank(field_value)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    requests.get(str(target_url))
    return jsonify({"result": "success"})
