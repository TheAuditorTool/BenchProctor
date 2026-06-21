# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63525():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
