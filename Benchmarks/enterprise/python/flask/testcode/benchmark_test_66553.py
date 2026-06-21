# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest66553():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
