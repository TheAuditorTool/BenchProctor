# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest22454():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    session['user'] = str(data)
    return jsonify({"result": "success"})
