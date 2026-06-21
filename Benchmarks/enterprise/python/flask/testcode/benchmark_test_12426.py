# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import db, User


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest12426():
    field_value = request.form.get('field', '')
    data = handle(field_value)
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
