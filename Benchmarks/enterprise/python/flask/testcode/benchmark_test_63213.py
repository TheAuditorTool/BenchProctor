# SPDX-License-Identifier: Apache-2.0
from flask import session
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest63213():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
