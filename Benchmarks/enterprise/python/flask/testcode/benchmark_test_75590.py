# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import socket
from app_runtime import db


def BenchmarkTest75590():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(db_value).split(',')
    data = ','.join(parts)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
