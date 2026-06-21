# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77808():
    referer_value = request.headers.get('Referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    eval(str(data))
    return jsonify({"result": "success"})
