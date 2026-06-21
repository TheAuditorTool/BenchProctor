# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest44495():
    upload_name = request.files['upload'].filename
    data = default_blank(upload_name)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return jsonify({"result": "success"})
