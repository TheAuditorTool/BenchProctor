# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest66249():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    session['user'] = str(data)
    return jsonify({"result": "success"})
