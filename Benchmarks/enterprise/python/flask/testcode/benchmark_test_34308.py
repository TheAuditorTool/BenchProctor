# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import jsonify


def BenchmarkTest34308(path_param):
    path_value = path_param
    parsed = urlparse(path_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = path_value
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return jsonify({"result": "success"})
