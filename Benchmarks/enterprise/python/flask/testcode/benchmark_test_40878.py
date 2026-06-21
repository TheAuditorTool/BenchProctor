# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40878():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
