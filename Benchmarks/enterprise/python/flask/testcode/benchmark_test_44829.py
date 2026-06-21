# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest44829():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
