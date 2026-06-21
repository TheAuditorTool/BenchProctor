# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11510():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
