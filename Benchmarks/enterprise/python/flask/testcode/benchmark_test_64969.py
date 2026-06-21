# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import socket
from app_runtime import db


def BenchmarkTest64969():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
