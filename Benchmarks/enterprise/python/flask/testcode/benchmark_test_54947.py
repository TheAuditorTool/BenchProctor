# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest54947():
    referer_value = request.headers.get('Referer', '')
    data = default_blank(referer_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
