# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51370():
    host_value = request.headers.get('Host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
