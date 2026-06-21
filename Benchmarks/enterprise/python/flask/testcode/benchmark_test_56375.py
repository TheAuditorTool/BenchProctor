# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56375():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
