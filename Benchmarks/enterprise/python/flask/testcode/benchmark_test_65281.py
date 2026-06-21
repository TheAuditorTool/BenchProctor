# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65281():
    header_value = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
