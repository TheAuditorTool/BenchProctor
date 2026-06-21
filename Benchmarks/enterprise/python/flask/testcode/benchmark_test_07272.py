# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07272():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
