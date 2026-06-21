# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest33959():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
