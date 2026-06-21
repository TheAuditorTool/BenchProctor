# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest07755():
    upload_name = request.files['upload'].filename
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(upload_name),))
    return jsonify({"result": "success"})
