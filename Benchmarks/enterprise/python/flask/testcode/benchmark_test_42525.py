# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42525():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
