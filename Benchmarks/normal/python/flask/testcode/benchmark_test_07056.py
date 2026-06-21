# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest07056():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
