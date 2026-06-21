# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest36344():
    origin_value = request.headers.get('Origin', '')
    data = to_text(origin_value)
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
