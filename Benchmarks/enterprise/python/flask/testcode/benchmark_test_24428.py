# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24428():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
