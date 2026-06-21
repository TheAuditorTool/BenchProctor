# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest69606():
    header_value = request.headers.get('X-Custom-Header', '')
    db.session.query(User).filter(User.id == header_value).all()
    return jsonify({"result": "success"})
