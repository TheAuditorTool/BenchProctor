# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest80961():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    session['user'] = str(data)
    return jsonify({"result": "success"})
