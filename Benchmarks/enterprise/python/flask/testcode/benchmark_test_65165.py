# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest65165():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    parsed = urlparse(graphql_var)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = graphql_var
    requests.get(str(target_url))
    return jsonify({"result": "success"})
