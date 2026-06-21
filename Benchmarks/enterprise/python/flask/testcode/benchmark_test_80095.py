# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest80095():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    session['user'] = str(data)
    return jsonify({"result": "success"})
