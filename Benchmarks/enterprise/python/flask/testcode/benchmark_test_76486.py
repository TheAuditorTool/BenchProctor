# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session
from app_runtime import db, User


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest76486():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
