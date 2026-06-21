# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest60341():
    ua_value = request.headers.get('User-Agent', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(ua_value),))
    return jsonify({"result": "success"})
