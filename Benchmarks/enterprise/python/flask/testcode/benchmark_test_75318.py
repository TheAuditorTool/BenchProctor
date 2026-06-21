# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest75318():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    session['user'] = str(data)
    return jsonify({"result": "success"})
