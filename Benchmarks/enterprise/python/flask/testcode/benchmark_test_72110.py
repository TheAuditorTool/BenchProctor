# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72110():
    header_value = request.headers.get('X-Custom-Header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
