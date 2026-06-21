# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03975():
    referer_value = request.headers.get('Referer', '')
    raise RuntimeError('processing failed: ' + str(referer_value))
    return jsonify({"result": "success"})
