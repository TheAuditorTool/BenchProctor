# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest02032():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
