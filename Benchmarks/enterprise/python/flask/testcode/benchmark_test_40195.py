# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40195():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
