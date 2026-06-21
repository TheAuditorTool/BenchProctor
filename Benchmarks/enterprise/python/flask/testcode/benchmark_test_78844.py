# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest78844():
    multipart_value = request.form.get('multipart_field', '')
    parsed = urlparse(multipart_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = multipart_value
    requests.get(str(target_url))
    return jsonify({"result": "success"})
