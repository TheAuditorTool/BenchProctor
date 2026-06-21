# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest20690():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    session['data'] = str(data)
    return jsonify({"result": "success"})
