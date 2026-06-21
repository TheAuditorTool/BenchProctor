# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import jsonify


def BenchmarkTest80221():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    if api_value:
        data = api_value
    else:
        data = ''
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    requests.get(str(target_url))
    return jsonify({"result": "success"})
