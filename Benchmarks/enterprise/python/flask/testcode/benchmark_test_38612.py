# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest38612():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
