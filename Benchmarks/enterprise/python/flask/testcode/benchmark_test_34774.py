# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34774():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
