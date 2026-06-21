# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest21265():
    referer_value = request.headers.get('Referer', '')
    data = coalesce_blank(referer_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
