# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest07504():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    session['data'] = str(data)
    return jsonify({"result": "success"})
