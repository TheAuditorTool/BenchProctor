# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest34163():
    upload_name = request.files['upload'].filename
    parsed = urlparse(upload_name)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = upload_name
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return jsonify({"result": "success"})
