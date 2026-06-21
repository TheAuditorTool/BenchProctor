# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46501():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
