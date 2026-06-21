# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04067():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    eval(str(data))
    return jsonify({"result": "success"})
