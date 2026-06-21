# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest00966():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
