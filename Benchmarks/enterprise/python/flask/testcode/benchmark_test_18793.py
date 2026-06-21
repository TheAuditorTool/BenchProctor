# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest18793(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
