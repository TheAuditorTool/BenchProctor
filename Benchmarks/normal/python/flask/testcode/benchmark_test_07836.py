# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest07836(path_param):
    path_value = path_param
    data = unquote(path_value)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return jsonify({"result": "success"})
