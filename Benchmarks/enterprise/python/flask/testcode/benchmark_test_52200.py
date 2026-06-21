# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest52200():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
