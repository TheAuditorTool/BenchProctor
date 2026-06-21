# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest53058():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
