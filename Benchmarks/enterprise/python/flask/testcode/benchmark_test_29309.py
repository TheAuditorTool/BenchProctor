# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest29309():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
