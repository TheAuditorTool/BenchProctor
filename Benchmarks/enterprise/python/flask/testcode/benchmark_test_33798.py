# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33798():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    eval(str(data))
    return jsonify({"result": "success"})
