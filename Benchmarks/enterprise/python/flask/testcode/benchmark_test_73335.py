# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import db, User


def BenchmarkTest73335():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
