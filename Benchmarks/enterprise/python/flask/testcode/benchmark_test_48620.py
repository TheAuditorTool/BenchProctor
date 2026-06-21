# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest48620():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
