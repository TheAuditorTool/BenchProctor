# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47292():
    referer_value = request.headers.get('Referer', '')
    data = '{}'.format(referer_value)
    eval(str(data))
    return jsonify({"result": "success"})
