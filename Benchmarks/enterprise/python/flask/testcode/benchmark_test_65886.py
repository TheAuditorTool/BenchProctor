# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest65886():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    session['user'] = str(data)
    return jsonify({"result": "success"})
