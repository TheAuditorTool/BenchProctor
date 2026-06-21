# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest68091():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    session['user'] = str(data)
    return jsonify({"result": "success"})
