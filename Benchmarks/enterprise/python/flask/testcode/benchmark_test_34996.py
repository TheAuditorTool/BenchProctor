# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest34996():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
