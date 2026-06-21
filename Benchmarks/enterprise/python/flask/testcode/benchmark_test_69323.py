# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest69323():
    header_value = request.headers.get('X-Custom-Header', '')
    data = default_blank(header_value)
    processed = data[:64]
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
