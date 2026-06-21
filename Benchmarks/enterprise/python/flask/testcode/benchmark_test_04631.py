# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest04631():
    referer_value = request.headers.get('Referer', '')
    session['data'] = str(referer_value)
    return jsonify({"result": "success"})
