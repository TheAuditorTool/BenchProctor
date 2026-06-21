# SPDX-License-Identifier: Apache-2.0
from flask import session
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest78634():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    session['user'] = str(data)
    return jsonify({"result": "success"})
