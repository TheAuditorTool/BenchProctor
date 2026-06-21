# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest70952():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
