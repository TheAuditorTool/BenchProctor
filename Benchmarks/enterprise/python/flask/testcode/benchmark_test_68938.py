# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest68938():
    xml_value = request.get_data(as_text=True)
    parts = []
    for token in str(xml_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
