# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest53868():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    session['data'] = str(data)
    return jsonify({"result": "success"})
