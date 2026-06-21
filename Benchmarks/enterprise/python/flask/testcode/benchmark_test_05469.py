# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest05469():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    session['user'] = str(data)
    return jsonify({"result": "success"})
