# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest44505():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return jsonify({"result": "success"})
