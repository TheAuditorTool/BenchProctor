# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33217():
    header_value = request.headers.get('X-Custom-Header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
