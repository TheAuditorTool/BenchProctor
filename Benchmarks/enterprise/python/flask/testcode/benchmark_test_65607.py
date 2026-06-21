# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65607():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
