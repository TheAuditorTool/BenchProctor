# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest33482():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
