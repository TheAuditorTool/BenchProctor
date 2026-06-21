# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28563():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
