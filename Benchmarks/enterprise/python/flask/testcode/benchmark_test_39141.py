# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest39141():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(forwarded_ip),))
    return jsonify({"result": "success"})
