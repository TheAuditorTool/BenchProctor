# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
import requests
from flask import jsonify


def BenchmarkTest10095():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(api_value)
    data = collected
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
