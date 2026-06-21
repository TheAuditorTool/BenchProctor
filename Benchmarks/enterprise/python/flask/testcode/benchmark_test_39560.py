# SPDX-License-Identifier: Apache-2.0
from flask import session
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest39560():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    session['data'] = str(data)
    return jsonify({"result": "success"})
