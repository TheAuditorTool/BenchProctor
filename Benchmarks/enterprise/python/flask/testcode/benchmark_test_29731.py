# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29731():
    header_value = request.headers.get('X-Custom-Header', '')
    data = (lambda v: v.strip())(header_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
