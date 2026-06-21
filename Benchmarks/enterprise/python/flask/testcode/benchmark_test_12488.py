# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest12488():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(forwarded_ip),))
    return jsonify({"result": "success"})
