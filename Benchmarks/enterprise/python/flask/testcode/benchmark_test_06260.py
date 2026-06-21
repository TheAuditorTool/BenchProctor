# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest06260():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
