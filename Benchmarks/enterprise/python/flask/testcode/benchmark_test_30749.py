# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30749():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
