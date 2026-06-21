# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13695():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    int(str(data))
    return jsonify({"result": "success"})
