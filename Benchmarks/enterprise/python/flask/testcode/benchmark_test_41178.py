# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41178():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
