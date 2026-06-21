# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest14765():
    origin_value = request.headers.get('Origin', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(origin_value),))
    return jsonify({"result": "success"})
