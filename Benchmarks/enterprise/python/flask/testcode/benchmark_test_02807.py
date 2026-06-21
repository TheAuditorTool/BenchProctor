# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest02807():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    session['data'] = str(data)
    return jsonify({"result": "success"})
