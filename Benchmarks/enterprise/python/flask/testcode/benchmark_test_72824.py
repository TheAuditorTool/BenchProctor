# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72824():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
