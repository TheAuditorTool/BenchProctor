# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest10855():
    origin_value = request.headers.get('Origin', '')
    data = coalesce_blank(origin_value)
    session['user'] = str(data)
    return jsonify({"result": "success"})
