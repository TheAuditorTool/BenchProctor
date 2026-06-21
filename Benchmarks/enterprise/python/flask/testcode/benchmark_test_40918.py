# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import socket
from app_runtime import db


def BenchmarkTest40918():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    s = socket.create_connection((str(db_value), 80))
    s.close()
    return jsonify({"result": "success"})
