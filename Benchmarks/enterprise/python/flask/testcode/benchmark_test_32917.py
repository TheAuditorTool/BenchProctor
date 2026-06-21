# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest32917():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    session['data'] = str(data)
    return jsonify({"result": "success"})
