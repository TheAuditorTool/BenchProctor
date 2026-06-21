# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest05621():
    origin_value = request.headers.get('Origin', '')
    data = default_blank(origin_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
