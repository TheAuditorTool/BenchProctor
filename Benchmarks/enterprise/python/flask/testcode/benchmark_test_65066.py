# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65066():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
