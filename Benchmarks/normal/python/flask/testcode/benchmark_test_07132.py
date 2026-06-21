# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest07132():
    user_id = request.args.get('id', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(user_id),))
    return jsonify({"result": "success"})
