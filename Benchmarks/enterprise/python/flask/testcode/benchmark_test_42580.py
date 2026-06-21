# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42580():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    int(str(data))
    return jsonify({"result": "success"})
