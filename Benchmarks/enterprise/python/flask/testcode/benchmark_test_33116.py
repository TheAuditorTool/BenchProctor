# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33116():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
