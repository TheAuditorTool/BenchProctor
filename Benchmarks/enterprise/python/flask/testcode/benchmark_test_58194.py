# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest58194():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
