# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79246():
    referer_value = request.headers.get('Referer', '')
    data = '{}'.format(referer_value)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
