# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest69133():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    session['data'] = str(data)
    return jsonify({"result": "success"})
