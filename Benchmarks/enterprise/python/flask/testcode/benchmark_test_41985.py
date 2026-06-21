# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
from app_runtime import db


def BenchmarkTest41985():
    upload_name = request.files['upload'].filename
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return jsonify({"result": "success"})
