# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest64464():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    session['data'] = str(data)
    return jsonify({"result": "success"})
