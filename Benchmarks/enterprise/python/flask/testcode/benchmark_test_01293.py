# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01293():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    int(str(data))
    return jsonify({"result": "success"})
