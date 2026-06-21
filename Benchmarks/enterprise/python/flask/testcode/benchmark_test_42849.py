# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest42849():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    session['user'] = str(data)
    return jsonify({"result": "success"})
