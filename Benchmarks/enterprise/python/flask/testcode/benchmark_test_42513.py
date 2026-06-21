# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest42513():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return jsonify({"result": "success"})
