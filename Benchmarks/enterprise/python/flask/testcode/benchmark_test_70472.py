# SPDX-License-Identifier: Apache-2.0
import os
import base64
from flask import jsonify
from app_runtime import db


def BenchmarkTest70472():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return jsonify({"result": "success"})
