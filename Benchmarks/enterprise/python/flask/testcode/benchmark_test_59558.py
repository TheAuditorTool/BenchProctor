# SPDX-License-Identifier: Apache-2.0
import os
import base64
from flask import jsonify
from app_runtime import db


def BenchmarkTest59558():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
