# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42350():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    exec(str(data))
    return jsonify({"result": "success"})
