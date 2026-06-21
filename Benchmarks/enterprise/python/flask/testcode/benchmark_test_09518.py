# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest09518():
    upload_name = request.files['upload'].filename
    db.execute('SELECT * FROM users WHERE id = ' + str(upload_name))
    return jsonify({"result": "success"})
