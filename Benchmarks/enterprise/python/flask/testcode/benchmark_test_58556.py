# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58556():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    eval(str(data))
    return jsonify({"result": "success"})
