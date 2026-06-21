# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33761():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
