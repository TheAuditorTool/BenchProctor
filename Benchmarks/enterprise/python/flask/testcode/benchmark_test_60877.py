# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest60877():
    field_value = request.form.get('field', '')
    parsed = urlparse(field_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = field_value
    requests.get(str(target_url))
    return jsonify({"result": "success"})
