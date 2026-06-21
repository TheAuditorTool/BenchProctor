# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34108():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
