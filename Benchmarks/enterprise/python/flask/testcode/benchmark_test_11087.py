# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest11087():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = default_blank(forwarded_ip)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
