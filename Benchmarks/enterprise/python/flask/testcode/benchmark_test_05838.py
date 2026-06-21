# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import request, jsonify


def BenchmarkTest05838():
    xml_value = request.get_data(as_text=True)
    parsed = urlparse(xml_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = xml_value
    requests.get(str(target_url))
    return jsonify({"result": "success"})
