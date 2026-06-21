# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest75809():
    ua_value = request.headers.get('User-Agent', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(ua_value),))
    return jsonify({"result": "success"})
