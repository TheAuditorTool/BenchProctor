# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import db, User


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest39913(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
