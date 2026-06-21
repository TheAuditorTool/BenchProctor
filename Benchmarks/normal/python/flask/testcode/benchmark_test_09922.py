# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest09922():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return jsonify({"result": "success"})
