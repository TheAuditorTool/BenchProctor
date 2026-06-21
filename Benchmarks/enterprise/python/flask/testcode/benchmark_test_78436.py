# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78436():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
