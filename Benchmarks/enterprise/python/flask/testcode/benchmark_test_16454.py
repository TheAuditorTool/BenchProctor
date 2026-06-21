# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest16454():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    session['data'] = str(data)
    return jsonify({"result": "success"})
