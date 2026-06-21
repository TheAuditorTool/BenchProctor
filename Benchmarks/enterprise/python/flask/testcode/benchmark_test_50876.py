# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50876():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    eval(str(data))
    return jsonify({"result": "success"})
