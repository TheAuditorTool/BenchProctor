# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest13189():
    upload_name = request.files['upload'].filename
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(upload_name)))
    return jsonify({"result": "success"})
