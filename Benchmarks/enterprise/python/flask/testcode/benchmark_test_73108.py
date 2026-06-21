# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest73108():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    session['data'] = str(data)
    return jsonify({"result": "success"})
