# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70112():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    int(str(data))
    return jsonify({"result": "success"})
