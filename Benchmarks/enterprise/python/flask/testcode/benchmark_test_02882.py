# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest02882():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
