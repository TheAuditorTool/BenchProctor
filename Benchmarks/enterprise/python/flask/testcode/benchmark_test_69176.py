# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69176():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    eval(str(data))
    return jsonify({"result": "success"})
