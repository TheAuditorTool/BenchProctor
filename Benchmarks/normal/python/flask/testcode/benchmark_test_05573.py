# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05573():
    header_value = request.headers.get('X-Custom-Header', '')
    prefix = ''
    data = prefix + str(header_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
